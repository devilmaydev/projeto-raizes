# -*- coding: utf-8 -*-
"""Extrai passagens do Twine «Voltando com o artefato errado»."""
import re, html, json, os

TWINE = r"C:\Users\fabio\Downloads\Voltando com o artefato errado (1).html"
OUT_JSON = os.path.join(os.path.dirname(__file__), "artefato_errado_passagens.json")


def slug(name, pid):
    manual = {
        "De volta ao Lab (com o artefato errado)": "de_volta_ao_lab_com_o_artefato_errado",
        "Voltando com a Cuia de Tacacá": "voltando_com_a_cuia_de_tacaca",
        "Voltando com a Cerâmica Tapajônica": "voltando_com_a_ceramica_tapajonica",
        "Voltando com o Muiraquitã": "voltando_com_o_muiraquita",
        "Voltando com o Porta Retratos": "voltando_com_o_porta_retratos",
        "Voltando com o Prêmio de Melhor Pesquisa": "voltando_com_o_premio_de_melhor_pesquisa",
        "Este é o artefato": "este_e_o_artefato",
        "(Você posiciona e nada acontece)": "voce_posiciona_e_nada_acontece",
        "Tá bem...": "ta_bem",
        "Nem a pau": "nem_a_pau",
    }
    if name in manual:
        return manual[name]
    s = re.sub(r"[^a-z0-9]+", "_", name.lower().strip())
    return s.strip("_") or f"passagem_{pid}"


with open(TWINE, encoding="utf-8") as f:
    s = f.read()

passages = []
for m in re.finditer(
    r'<tw-passagedata pid="(\d+)" name="([^"]*)"[^>]*>(.*?)</tw-passagedata>',
    s,
    re.DOTALL,
):
    pid, name, body = m.group(1), m.group(2), m.group(3)
    links = []
    for lk in re.findall(r"\[\[([^\]]+)\]\]", body):
        links.append(lk.split("|")[-1].strip() if "|" in lk else lk.strip())
    text = html.unescape(body)
    text = re.sub(r"\[\[[^\]]+\]\]", "", text)
    text = re.sub(r"<[^>]+>", "", text).strip()
    passages.append(
        {
            "pid": int(pid),
            "name": name,
            "slug": slug(name, pid),
            "links": links,
            "text": text,
        }
    )

with open(OUT_JSON, "w", encoding="utf-8") as o:
    json.dump(passages, o, ensure_ascii=False, indent=2)

print(len(passages), "passages ->", OUT_JSON)
