# -*- coding: utf-8 -*-
"""Gera game/story/.../jussara/jussara_twine.rpy a partir do Twine."""
import re, html, json, os, unicodedata

TWINE = r"C:\Users\fabio\Downloads\Jussara _ultima atualiza__o em 17 de Maio_.html"
JSON_IN = r"c:\GameDev\Renpy Projects\Raizes\tools\jussara_passagens.json"
from jussara_roots import find_jussara_dir

JUSSARA_DIR = find_jussara_dir()
OUT_FILE = os.path.join(JUSSARA_DIR, "jussara_twine.rpy")
PATHS_JSON = os.path.join(os.path.dirname(__file__), "jussara_passagem_paths.json")

# Destinos que não são passagem Ren'Py (módulos existentes)
EXTERNAL = {
    "(história}": ("call", "contar_historia_artefato"),
    "historia": ("call", "contar_historia_artefato"),
    "1 semana depois": ("call", "jussara_1_semana_depois"),
    "Belém": ("jump", "belem"),  # loop guard
}

NAV_LINK_NAMES = frozenset({"▶", "►", "→", "➞", "⇨", "➜", "➤", "»", "➡"})


def is_nav_link(name):
    s = name.strip()
    if s in NAV_LINK_NAMES:
        return True
    return bool(s) and all(c in NAV_LINK_NAMES or c.isspace() for c in s)


def emit_link_action(lines, lk, name_to_slug, indent="    "):
    kind, dest = target_action(lk, name_to_slug)
    if kind == "jump":
        lines.append(f"{indent}jump {dest}")
    else:
        lines.append(f"{indent}call {dest}")


MANUAL_SLUG = {
    "▶": "continuar_aeroporto",
    "➞": "game_over_continuar",
    "⇨": "game_over_continuar_alt",
    "Belém": "belem",
    "Universidade Federal do Pará": "universidade_federal_do_para",
    "Mirante do Rio": "mirante_do_rio",
    "abordagem da Jussara": "abordagem_da_jussara",
    "Posso sim": "posso_sim",
    "Decreto 12.600?": "decreto_12_600",
    "Sei, não me importo": "sei_nao_me_importo",
    "Conte-me mais": "conte_me_mais",
    "Claro que não, só zuando": "claro_que_nao_so_zuando",
    "O artefato primeiro": "o_artefato_primeiro",
    "Não acho tão sério assim": "nao_acho_tao_serio_assim",
    "Pix solidário para ajudar nas ocupações": "pix_solidario_para_ajudar_nas_ocupacoes",
    "Ajudar a disseminar em SP, o maior hub do Brasil": "ajudar_a_disseminar_em_sp",
    "Os índios deveriam ser incorporados à sociedade como todo mundo": "os_indios_deveriam_ser_incorporados",
    "Há um significado místico desse rio para esses povos?": "ha_um_significado_mistico_desse_rio",
    "Você está pessoalmente envolvida na causa?": "voce_esta_pessoalmente_envolvida_na_causa",
    "Me conta a história": "me_conta_a_historia",
    "Hmm...": "hmm",
    "E qual o problema?": "e_qual_o_problema",
    "Meu Deus, que triste!": "meu_deus_que_triste",
    "E daí?": "e_dai",
    "Não me importo mesmo": "nao_me_importo_mesmo",
    "Há um significado místico desse rio para esses povos?": "ha_um_significado_mistico",
    "(história}": "historia",
    "1 semana depois": "uma_semana_depois",
    "1 semana depois (se optou por não perguntar se ela está pessoalmente envolvida na causa": "uma_semana_depois_optou_nao_perguntar",
    "Preciso que me empreste um artefato seu para a minha pesquisa": "preciso_que_me_empreste_um_artefato",
    "Gostaria que me emprestasse um artefato seu": "gostaria_que_me_emprestasse_um_artefato_seu",
    "Na verdade, agora queria pedir sua ajuda com outra coisa": "na_verdade_agora_queria_pedir_sua_ajuda",
    "Agora preciso da sua ajuda": "agora_preciso_da_sua_ajuda",
    "Não foi por nada!": "nao_foi_por_nada",
    "Qual a chave pix?": "qual_a_chave_pix",
    "Que nada, vamo sim": "que_nada_vamo_sim",
    "Gracinha é você": "gracinha_e_voce",
    "Que gracinha você": "que_gracinha_voce",
    "Quer sair pra tomar um tacacá?": "quer_sair_pra_tomar_um_tacaca",
    "Vamos para a próxima pergunta": "vamos_para_a_proxima_pergunta",
    "Vamos para a próxima pergunta então": "vamos_para_a_proxima_pergunta",
    "É, uma mão lava a outra": "e_uma_mao_lava_a_outra",
    "Vou dar uma chance": "vou_dar_uma_chance",
    "Primeiro você": "primeiro_voce",
    "Pode ser aqui mesmo na UFPA, no Veropesinho": "pode_ser_ufpa_veropesinho",
    "Pode ser outro dia lá no Ver-o-peso": "pode_ser_ver_o_peso",
    "Veropesinho": "veropesinho",
    "Sim.": "sim_ponto",
    "Não.": "nao_ponto",
    "Sim": "sim",
    "Não": "nao",
    "Sério": "serio",
    "Posso Sim": "posso_sim",
    "Nem Pensar": "nem_pensar",
    "Nem pensar": "nem_pensar",
    "Tava Brincando": "tava_brincando",
    "Tava brincando": "tava_brincando",
    "Perdão": "perdao",
    "Desculpe!": "desculpe",
    "Grande coisa...": "grande_coisa",
    "Era mesmo. Desculpe. Prossiga": "era_mesmo_desculpe_prossiga",
    "Esse povo não tem o que fazer?": "esse_povo_nao_tem_o_que_fazer",
    "Nem é": "nem_e",
    "Nem é ": "nem_e",
    "Interessante!": "interessante",
    "Pior que não": "pior_que_nao",
    "Te juro": "te_juro",
    "Feito": "feito",
    "Pacas?": "pacas",
    "Relevantes": "relevantes",
    "Irrelevantes": "irrelevantes",
    "Prossiga": "prossiga",
    "Prossiga ": "prossiga",
    "Continuar?": "game_over_continuar",
}


def ascii_slug(name, pid=None):
    if name in MANUAL_SLUG:
        return MANUAL_SLUG[name]
    s = unicodedata.normalize("NFKD", name)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        s = f"passagem_{pid}"
    if s[0].isdigit():
        s = "p_" + s
    return s[:90]


def target_action(link_name, name_to_slug):
    if link_name in EXTERNAL:
        kind, dest = EXTERNAL[link_name]
        return kind, dest
    slug = name_to_slug.get(link_name)
    if not slug:
        slug = ascii_slug(link_name)
    return "call", slug


def is_narrator(line):
    line = line.strip()
    if not line:
        return False
    if line.startswith("(") and line.endswith(")"):
        return False
    starters = ("Você ", "você ", "Game Over", "Continuar", "Tudo pronto", "Obrigado por jogar")
    if any(line.startswith(s) for s in starters):
        return True
    if "[[Missão" in line:
        return True
    return False


def is_jussara(line):
    line = line.strip()
    if not line or (line.startswith("(") and ")" in line):
        return False
  # heurística: falas curtas de reação ou texto sem "Você"
    if line.startswith("Você "):
        return False
    return True


def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def lines_to_say(text):
    out = []
    for raw in text.split("\n"):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("(") and line.endswith(")"):
            out.append(f"    # Twine: {line}")
            continue
        if is_narrator(line):
            out.append(f'    n "{escape(line)}"')
        else:
            out.append(f'    j "{escape(line)}"')
    return out


def build_passage_block(p, name_to_slug):
    slug = p["slug"]
    lines = [f'## Twine: "{p["name"]}" (pid {p["pid"]})', f"label {slug}:"]

    say_lines = lines_to_say(p["text"])
    lines.extend(say_lines)

    if p["links"]:
        nav_links = [lk for lk in p["links"] if is_nav_link(lk)]
        choice_links = [lk for lk in p["links"] if not is_nav_link(lk)]

        if choice_links:
            if say_lines or p["text"].strip():
                lines.append("")
            lines.append("    menu:")
            for lk in choice_links:
                lines.append(f'        "{escape(lk)}":')
                kind, dest = target_action(lk, name_to_slug)
                if kind == "jump":
                    lines.append(f"            jump {dest}")
                else:
                    lines.append(f"            call {dest}")
            lines.append("")

        for lk in nav_links:
            emit_link_action(lines, lk, name_to_slug)

        lines.append("    return")
    else:
        if "Obrigado por jogar" in p["text"]:
            lines.append("    return")
        elif not p["links"]:
            lines.append("    return")

    if p["links"] and not say_lines and not p["text"].strip():
        lines = [f'## Twine: "{p["name"]}" (pid {p["pid"]})', f"label {slug}:"]
        nav_links = [lk for lk in p["links"] if is_nav_link(lk)]
        choice_links = [lk for lk in p["links"] if not is_nav_link(lk)]
        if choice_links:
            lines.append("    menu:")
            for lk in choice_links:
                lines.append(f'        "{escape(lk)}":')
                kind, dest = target_action(lk, name_to_slug)
                if kind == "jump":
                    lines.append(f"            jump {dest}")
                else:
                    lines.append(f"            call {dest}")
            lines.append("")
        for lk in nav_links:
            emit_link_action(lines, lk, name_to_slug)
        lines.append("    return")

    return "\n".join(lines)


def main():
    with open(JSON_IN, encoding="utf-8") as f:
        passages = json.load(f)

    # re-parse with pid for slug disambiguation
    with open(TWINE, encoding="utf-8") as f:
        html_text = f.read()
    parsed = []
    for m in re.finditer(
        r'<tw-passagedata pid="(\d+)" name="([^"]*)"[^>]*>(.*?)</tw-passagedata>',
        html_text,
        re.DOTALL,
    ):
        pid, name, body = m.group(1), m.group(2), m.group(3)
        links = re.findall(r"\[\[([^\]]+)\]\]", body)
        clean_links = []
        for lk in links:
            if "|" in lk:
                clean_links.append(lk.split("|")[-1].strip())
            else:
                clean_links.append(lk.strip())
        text = html.unescape(body)
        text = re.sub(r"\[\[[^\]]+\]\]", "", text)
        text = re.sub(r"<[^>]+>", "", text).strip()
        parsed.append({"pid": pid, "name": name, "links": clean_links, "text": text})

    name_to_slug = {}
    slug_count = {}
    for p in parsed:
        base = ascii_slug(p["name"], p["pid"])
        if base in slug_count:
            slug_count[base] += 1
            slug = f"{base}_{slug_count[base]}"
        else:
            slug_count[base] = 0
            slug = base
        name_to_slug[p["name"]] = slug
        p["slug"] = slug

    parsed.sort(key=lambda p: int(p["pid"]))

    parts = [
        "## Arco Jussara — passagens Twine (ficheiro único, gerado)",
        "## Regenerar: python tools/twine_to_jussara_passagens.py && python tools/generate_jussara_passagens.py",
        "## Módulos: modulos/ (canto, história, 1 semana)",
        "",
        "## Mapa Twine → label",
    ]
    for p in parsed:
        parts.append(f"## {p['name']!r} → {p['slug']} (pid {p['pid']})")
    parts.extend(
        [
            "",
            "# " + "=" * 76,
            "# Game over",
            "# " + "=" * 76,
            "",
            "## Game over: fundo preto, sem BG nem sprites.",
            "label jussara_game_over_setup:",
            "    window hide",
            "    scene black with dissolve",
            "    hide jussara",
            "    window show",
            "    return",
            "",
        ]
    )

    for p in parsed:
        parts.extend(
            [
                "# " + "=" * 76,
                f"# pid {int(p['pid']):03d} — {p['slug']}",
                "# " + "=" * 76,
                "",
                build_passage_block(p, name_to_slug),
                "",
            ]
        )

    with open(OUT_FILE, "w", encoding="utf-8") as o:
        o.write("\n".join(parts).rstrip() + "\n")

    print("Wrote", OUT_FILE, f"({len(parsed)} passagens)")


if __name__ == "__main__":
    main()
