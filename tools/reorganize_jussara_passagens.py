# -*- coding: utf-8 -*-
"""Move passagens/*.rpy para a árvore em tools/jussara_passagem_paths.json."""
from __future__ import annotations

import json
import os
import shutil

ROOT = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "game", "story", "Belém", "jussara", "passagens")
)
PATHS_JSON = os.path.join(os.path.dirname(__file__), "jussara_passagem_paths.json")


def main(dry_run: bool = False):
    with open(PATHS_JSON, encoding="utf-8") as f:
        data = json.load(f)

    paths: dict[str, str] = data["paths"]
    moved = 0
    missing = []

    for slug, rel in paths.items():
        src = os.path.join(ROOT, f"{slug}.rpy")
        dst = os.path.join(ROOT, rel.replace("/", os.sep))
        if not os.path.isfile(src):
            if os.path.isfile(dst):
                continue
            missing.append(slug)
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.normpath(src) == os.path.normpath(dst):
            continue
        if dry_run:
            print(f"  {slug}.rpy -> {rel}")
        else:
            shutil.move(src, dst)
        moved += 1

    if not dry_run:
        for name in os.listdir(ROOT):
            if name.endswith(".rpy") and name != "README.md":
                path = os.path.join(ROOT, name)
                if os.path.isfile(path):
                    os.remove(path)

    print(f"{'[dry-run] ' if dry_run else ''}Movidos: {moved}")
    if missing:
        print(f"Não encontrados na raiz ({len(missing)}):", ", ".join(missing[:10]), "...")


if __name__ == "__main__":
    import sys

    main(dry_run="--dry-run" in sys.argv)
