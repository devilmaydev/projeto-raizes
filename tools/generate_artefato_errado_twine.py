# -*- coding: utf-8 -*-
"""Gera viagem_retorno/artefato_errado_twine.rpy a partir do Twine."""
import json
import os
import re

JSON_IN = os.path.join(os.path.dirname(__file__), "artefato_errado_passagens.json")
OUT_FILE = os.path.normpath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "game",
        "story",
        "03_Belem",
        "Belém",
        "viagem_retorno",
        "artefato_errado_twine.rpy",
    )
)

NAV_LINKS = frozenset({"▶", "►", "→", "➞", "⇨"})

MANUAL_SLUG = {
    "Voltando com a Cuia de Tacacá": "voltando_com_a_cuia_de_tacaca",
    "Voltando com a Cerâmica Tapajônica": "voltando_com_a_ceramica_tapajonica",
    "Voltando com o Muiraquitã": "voltando_com_o_muiraquita",
    "Voltando com o Porta Retratos": "voltando_com_o_porta_retratos",
    "Voltando com o Prêmio de Melhor Pesquisa": "voltando_com_o_premio_de_melhor_pesquisa",
    "Este é o artefato": "este_e_o_artefato",
    "(Você posiciona e nada acontece)": "voce_posiciona_e_nada_acontece",
    "Tá bem...": "ta_bem",
    "Nem a pau": "nem_a_pau",
    "De volta ao Lab (com o artefato errado)": "de_volta_ao_lab_com_o_artefato_errado",
}


def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def is_nav(name):
    t = name.strip()
    return t in NAV_LINKS or (t and all(c in NAV_LINKS or c.isspace() for c in t))


def link_slug(name, name_to_slug):
    if name in MANUAL_SLUG:
        return MANUAL_SLUG[name]
    return name_to_slug.get(name)


def is_stage(line):
    line = line.strip()
    return line.startswith("(") and ")" in line


def is_narrator(line):
    line = line.strip()
    if is_stage(line):
        return True
    if line.startswith("(embarque") or line.startswith("(voltando"):
        return True
    if line.startswith("(Você posiciona"):
        return True
    return False


def lines_to_say(text):
    out = []
    for raw in text.split("\n"):
        line = raw.strip()
        if not line:
            continue
        if is_stage(line):
            out.append(f"    # Twine: {line}")
            continue
        if is_narrator(line):
            out.append(f'    n "{escape(line)}"')
        else:
            out.append(f'    p "{escape(line)}"')
    return out


def build_block(p, name_to_slug):
    slug = p["slug"]
    lines = [f'## Twine: "{p["name"]}" (pid {p["pid"]})', f"label {slug}:"]
    say = lines_to_say(p["text"])
    lines.extend(say)

    nav = [lk for lk in p["links"] if is_nav(lk)]
    choices = [lk for lk in p["links"] if not is_nav(lk)]

    if choices:
        if say or p["text"].strip():
            lines.append("")
        lines.append("    menu:")
        for lk in choices:
            dest = link_slug(lk, name_to_slug)
            lines.append(f'        "{escape(lk)}":')
            lines.append(f"            call {dest}")
        lines.append("")

    for lk in nav:
        dest = link_slug(lk, name_to_slug)
        if dest:
            lines.append(f"    call {dest}")

    lines.append("    return")
    return "\n".join(lines)


def main():
    with open(JSON_IN, encoding="utf-8") as f:
        passages = json.load(f)

    name_to_slug = {p["name"]: p["slug"] for p in passages}
    passages.sort(key=lambda p: p["pid"])

    parts = [
        "## Twine: «Voltando com o artefato errado» (ficheiro único)",
        "## Entrada do jogo: label lab_posicionar_artefato_retorno (lab_posicionar_artefato_retorno.rpy)",
        "## Regenerar: python tools/twine_to_artefato_errado.py && python tools/generate_artefato_errado_twine.py",
        "",
        "## Mapa Twine → label",
    ]
    for p in passages:
        parts.append(f"## {p['name']!r} → {p['slug']} (pid {p['pid']})")
    parts.append("")

    for p in passages:
        parts.extend(
            [
                "# " + "=" * 72,
                f"# pid {p['pid']:03d} — {p['slug']}",
                "# " + "=" * 72,
                "",
                build_block(p, name_to_slug),
                "",
            ]
        )

    with open(OUT_FILE, "w", encoding="utf-8") as o:
        o.write("\n".join(parts).rstrip() + "\n")
    print("Wrote", OUT_FILE)


if __name__ == "__main__":
    main()
