# -*- coding: utf-8 -*-
"""
Junta passagens/**/*.rpy num único game/story/.../jussara/jussara_twine.rpy.

Uso:
  python tools/merge_jussara_twine.py
  python tools/merge_jussara_twine.py --delete-passagens
"""
from __future__ import annotations

import argparse
import os
import re
import shutil

from jussara_filename import HEADER_PID, slug_from_basename
from jussara_roots import find_jussara_dir, find_passagens_root

GRAFO_BLOCK = re.compile(
    r"\n?## --- Grafo.*?## ---\n?",
    re.DOTALL,
)
PID_IN_NAME = re.compile(r"^p(\d+)_", re.I)

JUSSARA_DIR = find_jussara_dir()
PASSAGENS = os.path.join(JUSSARA_DIR, "passagens")
OUT_FILE = os.path.join(JUSSARA_DIR, "jussara_twine.rpy")
GAME_OVER = os.path.join(JUSSARA_DIR, "jussara_game_over.rpy")


def pid_from_path(path: str, text: str) -> int:
    fn = os.path.basename(path)
    m = PID_IN_NAME.match(fn.replace(".rpy", ""))
    if m:
        return int(m.group(1))
    m = HEADER_PID.search(text)
    if m:
        return int(m.group(1))
    return 99999


def clean_passage(text: str) -> str:
    text = GRAFO_BLOCK.sub("\n", text)
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def collect_passages() -> list[tuple[int, str, str]]:
    if not os.path.isdir(PASSAGENS):
        raise SystemExit(
            f"Sem pasta {PASSAGENS}. O Twine já está em jussara_twine.rpy ou regenere com generate_jussara_passagens.py."
        )
    rows = []
    for dirpath, _dirs, files in os.walk(PASSAGENS):
        for fn in files:
            if not fn.endswith(".rpy"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as f:
                raw = f.read()
            pid = pid_from_path(path, raw)
            slug = slug_from_basename(fn)
            rows.append((pid, slug, clean_passage(raw)))
    rows.sort(key=lambda x: (x[0], x[1]))
    return rows


def game_over_block() -> str:
    if not os.path.isfile(GAME_OVER):
        return ""
    with open(GAME_OVER, encoding="utf-8") as f:
        return clean_passage(f.read())


def build_file(passages: list[tuple[int, str, str]]) -> str:
    parts = [
        "## Arco Jussara — passagens Twine (ficheiro único)",
        "## Labels = slug Twine. Ordem abaixo = pid no Harlowe.",
        "## Módulos interativos: modulos/ (canto, história, 1 semana).",
        "## Regenerar a partir das passagens: python tools/merge_jussara_twine.py",
        "",
    ]
    go = game_over_block()
    if go:
        parts.extend(
            [
                "# " + "=" * 76,
                "# Game over",
                "# " + "=" * 76,
                "",
                go,
                "",
            ]
        )
    for pid, slug, body in passages:
        parts.extend(
            [
                "# " + "=" * 76,
                f"# pid {pid:03d} — {slug}",
                "# " + "=" * 76,
                "",
                body,
                "",
            ]
        )
    return "\n".join(parts).rstrip() + "\n"


def delete_passagens_tree() -> None:
    for name in os.listdir(PASSAGENS):
        path = os.path.join(PASSAGENS, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif name != ".gitkeep":
            os.remove(path)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--delete-passagens",
        action="store_true",
        help="Remove passagens/ após gerar jussara_twine.rpy",
    )
    ap.add_argument(
        "--delete-game-over",
        action="store_true",
        help="Remove jussara_game_over.rpy (já fundido)",
    )
    args = ap.parse_args()

    passages = collect_passages()
    content = build_file(passages)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Wrote {OUT_FILE} ({len(passages)} passagens)")

    if args.delete_passagens:
        delete_passagens_tree()
        readme = os.path.join(PASSAGENS, "README.md")
        arvore = os.path.join(PASSAGENS, "ARVORE.md")
        for p in (readme, arvore):
            if os.path.isfile(p):
                os.remove(p)
        print(f"Limpou {PASSAGENS} (pastas de atos)")

    if args.delete_game_over and os.path.isfile(GAME_OVER):
        os.remove(GAME_OVER)
        print(f"Removed {GAME_OVER}")


if __name__ == "__main__":
    main()
