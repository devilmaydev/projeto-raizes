# -*- coding: utf-8 -*-
"""Move todos os .rpy de passagens/ para o layout em jussara_passagem_paths.json (atos)."""
from __future__ import annotations

import json
import os
import shutil

from jussara_filename import slug_from_basename
from jussara_paths import ROOT

PATHS_JSON = os.path.join(os.path.dirname(__file__), "jussara_passagem_paths.json")


def find_all_rpy(root: str) -> dict[str, str]:
    """slug -> caminho absoluto do ficheiro."""
    found = {}
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if fn.endswith(".rpy") and fn != "README.md":
                slug = slug_from_basename(fn)
                path = os.path.join(dirpath, fn)
                if slug in found:
                    print(f"Aviso: slug duplicado {slug}:")
                    print(f"  {found[slug]}")
                    print(f"  {path}")
                found[slug] = path
    return found


def main(dry_run: bool = False):
    with open(PATHS_JSON, encoding="utf-8") as f:
        data = json.load(f)
    targets: dict[str, str] = data["paths"]

    sources = find_all_rpy(ROOT)
    moved = 0

    for slug, rel in targets.items():
        dst = os.path.join(ROOT, rel.replace("/", os.sep))
        src = sources.get(slug)
        if not src:
            if os.path.isfile(dst):
                continue
            print(f"Falta origem: {slug}")
            continue
        if os.path.normpath(src) == os.path.normpath(dst):
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if dry_run:
            print(f"{slug}: {os.path.relpath(src, ROOT)} -> {rel}")
        else:
            shutil.move(src, dst)
        moved += 1

    if not dry_run:
        for dirpath, dirnames, filenames in os.walk(ROOT, topdown=False):
            if dirpath == ROOT:
                continue
            if not dirnames and not filenames:
                os.rmdir(dirpath)
            elif not dirnames and filenames == []:
                try:
                    os.rmdir(dirpath)
                except OSError:
                    pass
        # remove pastas vazias de novo
        for _ in range(20):
            removed = False
            for dirpath, dirnames, filenames in os.walk(ROOT, topdown=False):
                if dirpath == ROOT:
                    continue
                if not dirnames and not filenames:
                    os.rmdir(dirpath)
                    removed = True
            if not removed:
                break

    print(f"{'[dry-run] ' if dry_run else ''}Reposicionados: {moved}")


if __name__ == "__main__":
    import sys

    main(dry_run="--dry-run" in sys.argv)
