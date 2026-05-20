# -*- coding: utf-8 -*-
"""
Renomeia passagens/*.rpy para p{pid:03d}_{slug}.rpy (pid no cabeçalho ## Twine).

Depois: python tools/jussara_acts.py
"""
from __future__ import annotations

import argparse
import os
import re

from jussara_filename import (
    HEADER_PID,
    passagem_filename,
    pid_from_file,
    slug_from_basename,
)
from jussara_paths import ROOT
from jussara_roots import find_passagens_root

LABEL_RE = re.compile(r"^label\s+(\w+)\s*:", re.MULTILINE)


def label_from_file(path: str) -> str | None:
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read(8192)
    except OSError:
        return None
    m = LABEL_RE.search(text)
    return m.group(1) if m else None


def scan_rpy(root: str) -> list[dict]:
    rows = []
    for dirpath, _dirs, files in os.walk(root):
        for fn in sorted(files):
            if not fn.endswith(".rpy"):
                continue
            path = os.path.join(dirpath, fn)
            slug_guess = slug_from_basename(fn)
            label = label_from_file(path) or slug_guess
            pid = pid_from_file(path)
            rows.append(
                {
                    "path": path,
                    "dir": dirpath,
                    "fn": fn,
                    "slug": label,
                    "pid": pid,
                }
            )
    return rows


def main(dry_run: bool = False) -> None:
    root = find_passagens_root()
    rows = scan_rpy(root)
    renamed = 0
    skipped = 0
    errors = []

    for row in rows:
        slug = row["slug"]
        pid = row["pid"]
        if pid is None:
            errors.append(f"sem pid: {row['path']}")
            continue
        new_fn = passagem_filename(slug, pid)
        if row["fn"] == new_fn:
            skipped += 1
            continue
        dst = os.path.join(row["dir"], new_fn)
        if os.path.exists(dst) and os.path.normpath(dst) != os.path.normpath(row["path"]):
            errors.append(f"destino existe: {dst} (de {row['path']})")
            continue
        rel_old = os.path.relpath(row["path"], root)
        rel_new = os.path.relpath(dst, root)
        if dry_run:
            print(f"{rel_old} -> {rel_new}")
        else:
            os.rename(row["path"], dst)
        renamed += 1

    print(f"Root: {root}")
    print(f"Renomeados: {renamed} | já ok: {skipped} | erros: {len(errors)}")
    for e in errors[:20]:
        print(" ", e)
    if len(errors) > 20:
        print(f"  … +{len(errors) - 20} erros")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    main(dry_run=args.dry_run)
