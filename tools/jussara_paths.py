# -*- coding: utf-8 -*-
"""
Árvore de pastas das passagens Jussara (Twine → Ren'Py).

Layout:
  <pasta>/<slug>.rpy
  <pasta>/continua/<filho>.rpy          — um único próximo passo (ou ▶)
  <pasta>/escolhas/<botão>/<filho>/     — ramo de menu (subpasta = próximo nó)
  _cruzamentos/<slug>.rpy               — atalho documentado (cópia ou stub)
  _sistema/                             — game over global
"""
from __future__ import annotations

import json
import os
import re
import unicodedata

from generate_jussara_passagens import (
    EXTERNAL,
    MANUAL_SLUG,
    ascii_slug,
    is_nav_link,
)

from jussara_roots import find_jussara_dir, passagens_root_rel

ROOT = find_jussara_dir()
JSON_IN = os.path.join(os.path.dirname(__file__), "jussara_passagens.json")
PATHS_JSON = os.path.join(os.path.dirname(__file__), "jussara_passagem_paths.json")

SYSTEM_SLUGS = frozenset(
    {
        "game_over_continuar",
        "game_over_continuar_alt",
        "sim",
        "nao",
        "sim_ponto",
        "nao_ponto",
    }
)


def choice_folder_name(link_name: str, child_slug: str) -> str:
    if is_nav_link(link_name):
        return child_slug
    s = unicodedata.normalize("NFKD", link_name)
    s = s.encode("ascii", "ignore").decode("ascii").lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")[:60]
    return s or child_slug


def load_passages():
    with open(JSON_IN, encoding="utf-8") as f:
        raw = json.load(f)
    name_to_slug = {}
    slug_count = {}
    passages = []
    for i, p in enumerate(raw):
        pid = p.get("pid", i + 1)
        base = ascii_slug(p["name"], pid)
        if base in slug_count:
            slug_count[base] += 1
            slug = f"{base}_{slug_count[base]}"
        else:
            slug_count[base] = 0
            slug = base
        name_to_slug[p["name"]] = slug
        passages.append(
            {
                "pid": int(pid),
                "name": p["name"],
                "slug": slug,
                "links": p.get("links", []),
                "text": p.get("text", ""),
            }
        )
    return passages, name_to_slug


def link_to_slug(link_name: str, name_to_slug: dict) -> str | None:
    if link_name in EXTERNAL:
        return None
    if link_name in name_to_slug:
        return name_to_slug[link_name]
    return ascii_slug(link_name)


def build_graph(passages, name_to_slug):
    by_slug = {p["slug"]: p for p in passages}
    children: dict[str, list[tuple[str, str]]] = {s: [] for s in by_slug}
    parents: dict[str, list[str]] = {s: [] for s in by_slug}

    for p in passages:
        slug = p["slug"]
        for lk in p["links"]:
            child = link_to_slug(lk, name_to_slug)
            if not child or child not in by_slug:
                continue
            children[slug].append((lk, child))
            parents[child].append(slug)

    return by_slug, children, parents


def tree_parent_from_belem(by_slug, children):
    """Pai de cada nó = caminho mais curto desde belem (evita loops Twine)."""
    if "belem" not in by_slug:
        return {}

    from collections import deque

    tree_parent: dict[str, tuple[str, str]] = {}
    depth = {"belem": 0}
    q = deque(["belem"])

    while q:
        u = q.popleft()
        for lk, v in children.get(u, []):
            if v not in by_slug:
                continue
            nd = depth[u] + 1
            if v not in depth or nd < depth[v]:
                depth[v] = nd
                tree_parent[v] = (u, lk)
                q.append(v)

    return tree_parent


def child_folder(parent_folder: str, link_name: str, child_slug: str, child_has_choices: bool) -> str:
    if child_has_choices:
        return os.path.join(
            parent_folder,
            "escolhas",
            choice_folder_name(link_name, child_slug),
        )
    if is_nav_link(link_name):
        return os.path.join(parent_folder, "continua")
    # Um único desfecho: ficheiro irmão na mesma pasta (ou em continua/ se for seta ▶).
    return parent_folder


def assign_tree(passages, name_to_slug):
    by_slug, children, parents = build_graph(passages, name_to_slug)
    tree_parent = tree_parent_from_belem(by_slug, children)

    paths: dict[str, str] = {}
    cross_parents: dict[str, list[str]] = {}

    # Filhos na árvore canónica (um pai por nó)
    tree_children: dict[str, list[tuple[str, str]]] = {}
    for child, (parent, lk) in tree_parent.items():
        tree_children.setdefault(parent, []).append((lk, child))

    def child_has_choices(slug: str) -> bool:
        real = [(lk, c) for lk, c in children.get(slug, []) if not is_nav_link(lk)]
        return len(real) > 1

    def visit(slug: str, folder: str):
        paths[slug] = folder
        for lk, child in tree_children.get(slug, []):
            cf = child_folder(folder, lk, child, child_has_choices(child))
            visit(child, cf)

    if "belem" in by_slug:
        visit("belem", os.path.join("00_entrada", "belem"))

    for slug in by_slug:
        if slug in SYSTEM_SLUGS and slug not in paths:
            visit(slug, os.path.join("_sistema", slug))
        elif slug not in paths:
            visit(slug, os.path.join("_orfas", slug))

    for slug, ps in parents.items():
        if len(ps) > 1:
            cross_parents[slug] = [
                child_folder(
                    paths[p],
                    lk,
                    slug,
                    child_has_choices(slug),
                )
                for p in ps
                if p in paths
                for lk, c in children.get(p, [])
                if c == slug
            ]

    return paths, cross_parents, children, by_slug


def rel_file_path(folder: str, slug: str, pid: int | str | None = None) -> str:
    from jussara_filename import passagem_filename

    fn = passagem_filename(slug, pid) if pid is not None else f"{slug}.rpy"
    return os.path.join(folder, fn).replace("\\", "/")


def write_paths_json(paths, cross_parents):
    payload = {
        "version": 2,
        "root": passagens_root_rel(),
        "filename_pattern": "p{pid:03d}_{slug}.rpy",
        "paths": {slug: rel_file_path(folder, slug) for slug, folder in sorted(paths.items())},
        "folders": paths,
        "cruzamentos": {
            slug: {"canonico": rel_file_path(paths[slug], slug), "outros_ramos": cross_parents[slug]}
            for slug in sorted(cross_parents)
        },
    }
    with open(PATHS_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return payload


def write_readme(paths, cross_parents, by_slug):
    lines = [
        "# Passagens Jussara — árvore Twine",
        "",
        "Cada passagem: `<pasta>/<slug>.rpy` (label Ren'Py = `slug`).",
        "",
        "| Subpasta | Significado |",
        "|----------|-------------|",
        "| `continua/` | Próximo passo único (ou seta ▶) |",
        "| `escolhas/<nome>/` | Ramo escolhido no menu |",
        "| `_cruzamentos/` | Passagem alcançada por vários caminhos |",
        "| `_sistema/` | Game over / fluxos globais |",
        "",
        "## Entrada do jogo",
        "",
        f"- `{rel_file_path(paths['belem'], 'belem')}`",
        "",
        "## Primeiros ramos (abordagem)",
        "",
    ]
    ab = paths.get("abordagem_da_jussara", "")
    if ab:
        lines.append(f"- Abordagem: `{rel_file_path(ab, 'abordagem_da_jussara')}`")
        esc = os.path.join(ab, "escolhas")
        if os.path.isdir(os.path.join(ROOT, esc.replace("/", os.sep))):
            pass
        for name in ("nem_pensar", "posso_sim", "eu_ja_estava_te_procurando_mesmo"):
            if name in paths:
                lines.append(f"  - `{rel_file_path(paths[name], name)}`")
    lines.extend(["", "## Cruzamentos", ""])
    if cross_parents:
        for slug, alts in sorted(cross_parents.items()):
            lines.append(f"- **{slug}** — ficheiro: `{rel_file_path(paths[slug], slug)}`")
            for alt in alts[:3]:
                lines.append(f"  - outro ramo: `{alt}/`")
            if len(alts) > 3:
                lines.append(f"  - … +{len(alts) - 3} ramos")
    else:
        lines.append("(nenhum)")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    passages, name_to_slug = load_passages()
    paths, cross, _children, by_slug = assign_tree(passages, name_to_slug)
    write_paths_json(paths, cross)
    readme = write_readme(paths, cross, by_slug)
    readme_path = os.path.join(ROOT, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"Passagens: {len(paths)} | Cruzamentos: {len(cross)}")
    print(f"Wrote {PATHS_JSON}")
    print(f"Wrote {readme_path}")
