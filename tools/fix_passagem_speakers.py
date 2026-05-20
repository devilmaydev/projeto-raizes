# -*- coding: utf-8 -*-
import os, re
DIR = r"c:\GameDev\Renpy Projects\Raizes\game\story\Belém\jussara\passagens"
NARRATOR_STARTS = (
    "Você ", "Ficar ", "Pedir ", "A experiência", "Antes você", "Eis que",
    "Estudantes", "Nota-se", "Game Over", "Continuar", "Tudo pronto",
    "Obrigado por jogar", "Não demora", "Muito obrigada! tu contribuíste",
)

for fn in os.listdir(DIR):
    if not fn.endswith(".rpy"):
        continue
    path = os.path.join(DIR, fn)
    text = open(path, encoding="utf-8").read()
    def repl(m):
        line = m.group(1)
        if any(line.startswith(s) for s in NARRATOR_STARTS):
            return f'    n "{line}"'
        return m.group(0)
    new = re.sub(r'    j "([^"]+)"', repl, text)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
print("done")
