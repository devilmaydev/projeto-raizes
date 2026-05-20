# -*- coding: utf-8 -*-
"""Adiciona jussara_fim_mirante antes de return em passagens de despedida sem menu."""
import os, re
DIR = r"c:\GameDev\Renpy Projects\Raizes\game\story\Belém\jussara\passagens"
SKIP = {
    "game_over_continuar.rpy", "game_over_continuar_alt.rpy", "sim.rpy", "sim_ponto.rpy",
    "nao.rpy", "nao_ponto.rpy", "belem.rpy", "continuar_aeroporto.rpy",
    "universidade_federal_do_para.rpy", "mirante_do_rio.rpy", "abordagem_da_jussara.rpy",
    "me_conta_a_historia.rpy", "historia.rpy", "uma_semana_depois.rpy",
}
PHRASES = ("Até mais", "bom dia", "Adeus", "encerrar por aqui", "se retirar", "Obrigado por jogar")

for fn in os.listdir(DIR):
    if fn not in SKIP and fn.endswith(".rpy"):
        path = os.path.join(DIR, fn)
        text = open(path, encoding="utf-8").read()
        if "jussara_fim_mirante" in text or "game_over_continuar" in text:
            continue
        if "    menu:" in text:
            continue
        if not any(p in text for p in PHRASES):
            continue
        if not re.search(r"\n    return\s*$", text):
            continue
        text = text.replace("\n    return\n", "\n    call jussara_fim_mirante\n    return\n", 1)
        open(path, "w", encoding="utf-8").write(text)
print("fim appended")
