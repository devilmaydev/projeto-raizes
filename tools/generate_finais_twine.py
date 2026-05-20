# -*- coding: utf-8 -*-
"""Gera game/story/03_Belem/Belém/viagem_retorno/finais_twine.rpy"""
import json
import os
import re
import unicodedata

JSON_IN = os.path.join(os.path.dirname(__file__), "finais_passagens.json")
OUT_FILE = os.path.normpath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "game",
        "story",
        "03_Belem",
        "Belém",
        "viagem_retorno",
        "finais_twine.rpy",
    )
)

NAV_LINKS = frozenset({"▶", "►", "→", "➞", "⇨"})

# Destinos fora deste Twine
EXTERNAL = {
    "De volta à Belém": ("call", "alfandega_belem_recuperacao_inicio"),
    "De volta ao Aeroporto de Guarulhos": ("call", "alfandega_guarulhos_desembarque_mochila_vazia"),
}

# Labels curtos que colidem com jussara_twine.rpy
SLUG_CONFLICT = frozenset({"sim", "nao", "serio", "prossiga", "vou_dar_uma_chance"})

MANUAL_LINK = {
    "De Volda Ao Laboratório": "de_volta_ao_laboratorio",
    "(objeto posicionado)": "objeto_posicionado",
    "Se for o artefato errado": "se_for_o_artefato_errado",
    "Se for o artefato certo": "se_for_o_artefato_certo",
    "➞": "game_over_finais",
    "Sim": "finais_sim",
    "Não": "finais_nao",
}

# Corpo substituído (stubs / chamadas a outros módulos)
BODY_OVERRIDE = {
    "de_volta_a_belem": [
        "    # Twine: (daqui se segue como se você tivesse voltado sozinho no Twine Alfândega)",
        "    call alfandega_belem_recuperacao_inicio",
    ],
    "de_volta_ao_aeroporto_de_guarulhos": [
        "    call alfandega_guarulhos_desembarque_mochila_vazia",
    ],
    "vou_voltar_la_e_pegar_o_certo": [
        '    p "Então partiremos agora imediatamente para o Aeroporto!"',
        "    call alfandega_belem_recuperacao_inicio",
    ],
}

SKIP_PASSAGE_SLUGS = frozenset(
    {
        "game_over_finais",
        "fin_sim",  # pid 43 — menu do game over usa finais_sim
        "fin_nao",
    }
)


def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def is_nav(name):
    t = name.strip()
    return t in NAV_LINKS or (t and all(c in NAV_LINKS or c.isspace() for c in t))


def link_dest(link_name, name_to_slug):
    if link_name in EXTERNAL:
        return EXTERNAL[link_name]
    if link_name in MANUAL_LINK:
        return ("call", MANUAL_LINK[link_name])
    slug = name_to_slug.get(link_name)
    if slug:
        return ("call", slug)
    return None


def collect_story_labels(exclude_path):
    """Labels já usados noutros .rpy (evita colisão com sala_professor, jussara, etc.)."""
    found = set()
    game_story = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "game", "story"))
    for root, _, files in os.walk(game_story):
        for fname in files:
            if not fname.endswith(".rpy"):
                continue
            path = os.path.normpath(os.path.join(root, fname))
            if path == exclude_path:
                continue
            with open(path, encoding="utf-8") as f:
                for m in re.finditer(r"^label (\w+)", f.read(), re.M):
                    found.add(m.group(1))
    return found


def emit_line(lines, line, pid=None):
    line = line.strip()
    if not line:
        return
    if line.startswith("(") and ")" in line and not re.match(r"^\(Jussara\)", line, re.I):
        lines.append(f"    # Twine: {line}")
        return
    if re.match(r"^\(Jussara\)", line, re.I):
        txt = re.sub(r"^\(Jussara\)\s*:?\s*", "", line, flags=re.I).strip()
        if txt:
            lines.append(f'    j "{escape(txt)}"')
        return
    if line.strip() in ("[[", "]]") or line.strip().startswith("[["):
        return
    if line.strip() == "Fim" or line.startswith("Fim\n"):
        # sem «from»: evita _call_* duplicado quando vários finais chamam o mesmo ecrã
        lines.append("    call finais_tela_fim")
        return
    if "Twine da Batalha" in line or "batalha ética" in line.lower():
        return
    if line.startswith("(") and line.endswith(")"):
        lines.append(f"    # Twine: {line}")
        return
    if line.startswith("Você ") or line.startswith("você "):
        lines.append(f'    n "{escape(line)}"')
        return
    lines.append(f'    p "{escape(line)}"')


def lines_to_say(text, link_texts=None, pid=None):
    out = []
    link_texts = link_texts or set()
    for raw in text.split("\n"):
        if raw.strip() in link_texts:
            continue
        emit_line(out, raw, pid=pid)
    return out


def resolve_slug(slug, existing_labels=None):
    existing_labels = existing_labels or set()
    if slug in SLUG_CONFLICT or slug in existing_labels:
        return "fin_" + slug
    return slug


def build_block(p, name_to_slug):
    slug = p["slug"]
    if slug in SKIP_PASSAGE_SLUGS:
        return None
    lines = [f'## Twine: "{p["name"]}" (pid {p["pid"]})', f"label {slug}:"]

    if slug in BODY_OVERRIDE:
        lines.extend(BODY_OVERRIDE[slug])
        lines.append("    return")
        return "\n".join(lines)

    if slug == "sinto_que_nao_e_certo_sem_a_opiniao_dos_demais":
        lines.extend(
            [
                "    # Twine Finais → Twine separado «Batalha Jussara × Professor»",
                "    call batalha_jussara_professor_inicio",
            ]
        )
        lines.append("    return")
        return "\n".join(lines)

    if slug == "objeto_posicionado":
        lines.extend(
            [
                "    if artefato_id == \"urna\":",
                "        call se_for_o_artefato_certo",
                "    else:",
                "        call se_for_o_artefato_errado",
                "    return",
            ]
        )
        return "\n".join(lines)

    if slug == "de_volta_ao_laboratorio":
        lines.extend(
            [
                "    scene bg sala_professor",
                "    show professor idle at professor_sala_pose",
                "    with dissolve",
                '    $ jussara_checkpoint("finais_lab")',
            ]
        )

    link_texts = {lk.strip() for lk in p["links"]}
    say = lines_to_say(p["text"], link_texts, pid=p["pid"])
    lines.extend(say)
    teve_fim = "Fim" in (p.get("text") or "") or any(
        "finais_tela_fim" in ln for ln in say
    )

    nav = [lk for lk in p["links"] if is_nav(lk)]
    choices = [lk for lk in p["links"] if not is_nav(lk)]

    if choices:
        if say:
            lines.append("")
        lines.append("    menu:")
        for lk in choices:
            dest = link_dest(lk, name_to_slug)
            lines.append(f'        "{escape(lk)}":')
            if dest:
                kind, target = dest
                if kind == "jump":
                    lines.append(f"            jump {target}")
                else:
                    lines.append(f"            call {target}")
        lines.append("")

    for lk in nav:
        dest = link_dest(lk, name_to_slug)
        if dest:
            kind, target = dest
            if teve_fim and target == "game_over_finais":
                continue
            if kind == "jump":
                lines.append(f"    jump {target}")
            else:
                lines.append(f"    call {target}")

    lines.append("    return")
    return "\n".join(lines)


def main():
    out_abs = os.path.normpath(OUT_FILE)
    existing_labels = collect_story_labels(out_abs)

    with open(JSON_IN, encoding="utf-8") as f:
        data = json.load(f)
    passages = data["passages"]
    for p in passages:
        p["slug"] = resolve_slug(p["slug"], existing_labels)
    name_to_slug = {p["name"]: p["slug"] for p in passages}
    passages.sort(key=lambda p: p["pid"])

    parts = [
        "## Twine: «Finais» — em processo; pós-Alfândega com artefato certo (urna)",
        "## Entrada: lab_posicionar_artefato_retorno → de_volta_ao_laboratorio",
        "## Batalha Jussara×Professor: Twine menor separado → batalha_jussara_professor.rpy",
        "## Regenerar: python tools/twine_to_finais.py && python tools/generate_finais_twine.py",
        "",
        "## Mapa Twine → label",
    ]
    for p in passages:
        parts.append(f"## {p['name']!r} → {p['slug']} (pid {p['pid']})")
    parts.extend(
        [
            "",
            "# " + "=" * 72,
            "# Finais — ecrã de fim e game over",
            "# " + "=" * 72,
            "",
            "label finais_voltar_menu:",
            "    window hide",
            "    scene black with dissolve",
            "    pause 0.5",
            "    $ renpy.full_restart()",
            "",
            "label finais_tela_fim:",
            "    scene black with dissolve",
            "    window hide",
            '    show text "{size=48}Fim{/size}" as finais_fim_txt:',
            "        xalign 0.5",
            "        yalign 0.5",
            "    pause 2.0",
            "    hide finais_fim_txt",
            "    jump finais_voltar_menu",
            "",
            "label game_over_finais:",
            "    call jussara_game_over_setup",
            '    n "Game Over"',
            "    pause 1.5",
            "    jump finais_voltar_menu",
            "",
        ]
    )

    for p in passages:
        block = build_block(p, name_to_slug)
        if block is None:
            continue
        parts.extend(
            [
                "# " + "=" * 72,
                f"# pid {p['pid']:03d} — {p['slug']}",
                "# " + "=" * 72,
                "",
                block,
                "",
            ]
        )

    with open(OUT_FILE, "w", encoding="utf-8") as o:
        o.write("\n".join(parts).rstrip() + "\n")
    print("Wrote", OUT_FILE, f"({len(passages)} passagens)")


if __name__ == "__main__":
    main()
