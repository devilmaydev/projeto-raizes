# -*- coding: utf-8 -*-
"""
Grafo de ramificações Jussara (Twine → Ren'Py).

Modelo híbrido recomendado:
  - Ficheiros nos ATOS (pastas rasas) — editar sem 18 níveis de pasta.
  - Um ficheiro = um label (sem duplicar passagens em vários pais).
  - Cabeçalho ## Grafo em cada .rpy — pai canónico + filhos + cruzamentos.
  - tools/jussara_grafo.json + passagens/ARVORE.md — visão global.

Pai canónico = primeiro caminho mais curto desde `belem` (BFS).
Cruzamentos = passagens alcançáveis por mais de um pai (normal no Twine).

Uso:
  python tools/jussara_grafo.py
  python tools/jussara_grafo.py --no-patch   # só JSON + ARVORE.md
"""
from __future__ import annotations

import argparse
import json
import os
import re

from generate_jussara_passagens import is_nav_link
from jussara_filename import passagem_basename, pid_from_file
from jussara_paths import (
    PATHS_JSON,
    ROOT,
    SYSTEM_SLUGS,
    build_graph,
    link_to_slug,
    load_passages,
    tree_parent_from_belem,
)
from jussara_roots import find_passagens_root, passagens_root_rel

GRAFO_JSON = os.path.join(os.path.dirname(__file__), "jussara_grafo.json")
ARVORE_MD = os.path.join(find_passagens_root(), "ARVORE.md")

GRAFO_START = "## --- Grafo"
GRAFO_END = "## ---"
LABEL_RE = re.compile(r"^label\s+\w+\s*:", re.MULTILINE)


def slug_pids_from_paths_json() -> dict[str, int]:
    if not os.path.isfile(PATHS_JSON):
        return {}
    with open(PATHS_JSON, encoding="utf-8") as f:
        data = json.load(f)
    out: dict[str, int] = {}
    for slug, rel in data.get("paths", {}).items():
        m = re.search(r"/p(\d+)_", rel.replace("\\", "/"))
        if m:
            out[slug] = int(m.group(1))
    return out


def ref(slug: str, pids: dict[str, int]) -> str:
    pid = pids.get(slug)
    if pid is not None:
        return passagem_basename(slug, pid)
    return slug


def build_grafo_data(passages, name_to_slug, paths_rel: dict[str, str]) -> dict:
    by_slug, children, parents = build_graph(passages, name_to_slug)
    tree_parent = tree_parent_from_belem(by_slug, children)
    pids = slug_pids_from_paths_json()

    for p in passages:
        if "pid" in p:
            pids[p["slug"]] = int(p["pid"])

    nodes = {}
    for slug, p in by_slug.items():
        canon = tree_parent.get(slug)
        canon_parent, canon_link = (canon[0], canon[1]) if canon else (None, None)
        child_edges = []
        for lk, ch in children.get(slug, []):
            if ch not in by_slug:
                continue
            child_edges.append(
                {
                    "slug": ch,
                    "link": lk,
                    "nav": is_nav_link(lk),
                    "ref": ref(ch, pids),
                }
            )
        other_parents = sorted(set(parents.get(slug, [])) - ({canon_parent} if canon_parent else set()))
        nodes[slug] = {
            "pid": pids.get(slug),
            "twine_name": p["name"],
            "file": paths_rel.get(slug),
            "canon_parent": canon_parent,
            "canon_link": canon_link,
            "children": child_edges,
            "other_parents": [
                {"slug": op, "ref": ref(op, pids)} for op in other_parents
            ],
            "is_crossing": len(other_parents) > 0,
        }

    return {
        "version": 1,
        "root": passagens_root_rel(),
        "entry": "belem",
        "nodes": nodes,
        "stats": {
            "passages": len(nodes),
            "crossings": sum(1 for n in nodes.values() if n["is_crossing"]),
        },
    }


def grafo_header_block(node: dict) -> str:
    lines = [
        GRAFO_START,
        "## Gerado por: python tools/jussara_grafo.py",
    ]
    pid = node.get("pid")
    if pid is not None:
        lines.append(f"## pid Twine: {pid}")

    cp = node.get("canon_parent")
    if cp:
        cl = node.get("canon_link") or ""
        lines.append(f"## Pai canonico: {cp}" + (f' (escolha/link: «{cl}»)' if cl else ""))
    else:
        lines.append("## Pai canonico: (entrada / sem pai no grafo)")

    kids = node.get("children") or []
    if kids:
        parts = []
        for e in kids:
            tag = "nav" if e.get("nav") else "menu"
            parts.append(f'{e["ref"]} «{e["link"]}» [{tag}]')
        lines.append("## Filhos: " + "; ".join(parts))
    else:
        lines.append("## Filhos: (nenhum no Twine exportado)")

    others = node.get("other_parents") or []
    if others:
        refs = ", ".join(o["ref"] for o in others)
        lines.append(f"## Outros pais (cruzamentos): {refs}")
    else:
        lines.append("## Outros pais (cruzamentos): —")

    lines.append(GRAFO_END)
    return "\n".join(lines)


def patch_file_header(path: str, block: str) -> bool:
    with open(path, encoding="utf-8") as f:
        text = f.read()

    if GRAFO_START in text:
        pattern = re.compile(
            re.escape(GRAFO_START) + r".*?" + re.escape(GRAFO_END),
            re.DOTALL,
        )
        new_text = pattern.sub(block, text, count=1)
    else:
        m = LABEL_RE.search(text)
        if m:
            new_text = text[: m.start()] + block + "\n" + text[m.start() :]
        else:
            new_text = block + "\n" + text

    if new_text == text:
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return True


def render_arvore_md(data: dict) -> str:
    nodes = data["nodes"]
    pids = {s: n["pid"] for s, n in nodes.items() if n.get("pid")}

    # Só arestas do pai canónico (BFS desde belem) — evita explosão em cruzamentos.
    canon_children: dict[str, list[tuple[str, str]]] = {}
    for slug, n in nodes.items():
        cp = n.get("canon_parent")
        if not cp:
            continue
        lk = n.get("canon_link") or ""
        canon_children.setdefault(cp, []).append((lk, slug))

    lines = [
        "# Árvore de ramificações (pai canónico desde `belem`)",
        "",
        "Cada passagem existe **uma vez** nos atos (`01_aeroporto/`, …).",
        "Esta árvore mostra **um** caminho por passagem (o mais curto desde `belem`).",
        "Ramos alternativos: cabeçalho `## --- Grafo` no `.rpy` e [Cruzamentos](#cruzamentos).",
        "",
        f"- Passagens: {data['stats']['passages']}",
        f"- Cruzamentos: {data['stats']['crossings']}",
        "",
        "## Árvore",
        "",
    ]

    def walk(slug: str, depth: int, stack: tuple[str, ...]):
        if slug in stack:
            lines.append("  " * depth + f"- `{ref(slug, pids)}` _(ciclo Twine)_")
            return
        n = nodes.get(slug, {})
        name = n.get("twine_name", slug)
        pid = n.get("pid")
        pid_s = f" pid {pid}" if pid else ""
        lines.append("  " * depth + f"- **{ref(slug, pids)}** — «{name}»{pid_s}")
        for lk, ch in canon_children.get(slug, []):
            lines.append("  " * (depth + 1) + f"- «{lk}» →")
            walk(ch, depth + 2, stack + (slug,))

    walk(data["entry"], 0, ())

    lines.extend(
        [
            "",
            "## Cruzamentos",
            "",
            "Passagens com mais de um pai no Twine. O ficheiro fica no ato; os caminhos extra não duplicam o `.rpy`.",
            "",
        ]
    )
    for slug in sorted(nodes, key=lambda s: (nodes[s].get("pid") or 9999, s)):
        n = nodes[slug]
        if not n.get("is_crossing"):
            continue
        cp = n.get("canon_parent")
        others = [o["ref"] for o in n.get("other_parents", [])]
        lines.append(f"- `{ref(slug, pids)}` — pai canónico: `{cp}`; também desde: {', '.join(f'`{o}`' for o in others)}")
    lines.append("")
    return "\n".join(lines)


def collect_files_by_slug() -> dict[str, str]:
    out = {}
    for dirpath, _dirs, files in os.walk(ROOT):
        for fn in files:
            if not fn.endswith(".rpy"):
                continue
            from jussara_filename import slug_from_basename

            slug = slug_from_basename(fn)
            out[slug] = os.path.join(dirpath, fn)
    return out


def main(patch_headers: bool = True) -> None:
    passages, name_to_slug = load_passages()
    with open(PATHS_JSON, encoding="utf-8") as f:
        paths_rel = json.load(f).get("paths", {})

    data = build_grafo_data(passages, name_to_slug, paths_rel)

    with open(GRAFO_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    arvore = render_arvore_md(data)
    with open(ARVORE_MD, "w", encoding="utf-8") as f:
        f.write(arvore)

    patched = 0
    if patch_headers:
        files = collect_files_by_slug()
        for slug, node in data["nodes"].items():
            path = files.get(slug)
            if not path:
                continue
            block = grafo_header_block(node)
            if patch_file_header(path, block):
                patched += 1

    print(f"Grafo: {data['stats']['passages']} passagens, {data['stats']['crossings']} cruzamentos")
    print(f"Wrote {GRAFO_JSON}")
    print(f"Wrote {ARVORE_MD}")
    if patch_headers:
        print(f"Cabeçalhos Grafo atualizados: {patched} ficheiros")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-patch", action="store_true", help="Não alterar .rpy")
    args = ap.parse_args()
    main(patch_headers=not args.no_patch)
