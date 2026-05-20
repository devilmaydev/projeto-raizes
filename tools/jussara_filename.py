# -*- coding: utf-8 -*-
"""
Nomes de ficheiros das passagens Jussara.

Formato: p{pid:03d}_{slug}.rpy  — ex.: p001_belem.rpy, p009_game_over_continuar.rpy

O label Ren'Py continua a ser só `slug` (não muda com o rename).
"""
from __future__ import annotations

import re

PID_PREFIX = re.compile(r"^p(\d+)_(.+)$", re.IGNORECASE)
HEADER_PID = re.compile(r"\(pid\s+(\d+)\)", re.IGNORECASE)


def passagem_basename(slug: str, pid: int | str) -> str:
    return f"p{int(pid):03d}_{slug}"


def passagem_filename(slug: str, pid: int | str) -> str:
    return passagem_basename(slug, pid) + ".rpy"


def slug_from_basename(basename: str) -> str:
    """Remove .rpy e prefixo pNNN_ se existir."""
    name = basename
    if name.lower().endswith(".rpy"):
        name = name[:-4]
    m = PID_PREFIX.match(name)
    if m:
        return m.group(2)
    return name


def pid_from_file_text(text: str) -> int | None:
    m = HEADER_PID.search(text)
    return int(m.group(1)) if m else None


def pid_from_file(path: str) -> int | None:
    try:
        with open(path, encoding="utf-8") as f:
            return pid_from_file_text(f.read(4096))
    except OSError:
        return None
