# -*- coding: utf-8 -*-
"""Remove menus whose only option is a Twine navigation arrow (▶, ➞, ⇨, etc.)."""
import glob
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..", "game", "story", "Belém", "jussara", "passagens")

# Símbolos de navegação do Twine (não são escolhas reais do jogador).
NAV_LINK_NAMES = frozenset({"▶", "►", "→", "➞", "⇨", "➜", "➤", "»", "➡"})
NL = r"\r?\n"
BLOCK = re.compile(
    NL + r"    menu:" + NL + r"        \"([^\"]+)\":" + NL + r"            ((?:call|jump) .+?)" + NL,
    re.MULTILINE,
)


def is_arrow_label(label: str) -> bool:
    s = label.strip()
    if s in NAV_LINK_NAMES:
        return True
    return bool(s) and all(c in NAV_LINK_NAMES or c.isspace() for c in s)


def fix_file(path: str) -> bool:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    orig = text

    def repl(m):
        if is_arrow_label(m.group(1)):
            return f"\n    {m.group(2)}\n"
        return m.group(0)

    text = BLOCK.sub(repl, text)
    if text == orig:
        return False
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return True


def main():
    fixed = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.rpy"))):
        if fix_file(path):
            fixed.append(os.path.basename(path))
    print(f"Fixed {len(fixed)} file(s):")
    for name in fixed:
        print(f"  {name}")


if __name__ == "__main__":
    main()
