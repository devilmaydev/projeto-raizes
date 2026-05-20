# -*- coding: utf-8 -*-
"""Localiza game/.../jussara/ e passagens/ (se existir)."""
from __future__ import annotations

import os

_TOOLS = os.path.dirname(os.path.abspath(__file__))
_GAME_STORY = os.path.normpath(os.path.join(_TOOLS, "..", "game", "story"))


def find_jussara_dir() -> str:
    for dirpath, dirnames, files in os.walk(_GAME_STORY):
        norm = dirpath.replace("\\", "/")
        if not norm.endswith("/jussara"):
            continue
        if "jussara_twine.rpy" in files or "jussara_core.rpy" in files:
            return dirpath
    raise FileNotFoundError("Pasta jussara/ não encontrada em game/story")


def find_passagens_root() -> str:
    """Pasta passagens/ (legado) ou jussara/ se o Twine está só em jussara_twine.rpy."""
    jussara = find_jussara_dir()
    legacy = os.path.join(jussara, "passagens")
    if os.path.isdir(legacy):
        return legacy
    return jussara


def passagens_root_rel(passagens_root: str | None = None) -> str:
    root = passagens_root or find_jussara_dir()
    game = os.path.normpath(os.path.join(_TOOLS, "..", "game"))
    rel = os.path.relpath(root, game).replace("\\", "/")
    return f"game/{rel}"
