# -*- coding: utf-8 -*-
"""Extrai passagens do Twine «Finais»."""
import re, html, json, os, unicodedata

TWINE = r"C:\Users\fabio\Downloads\Finais.html"
OUT_JSON = os.path.join(os.path.dirname(__file__), "finais_passagens.json")


def slug(name, pid):
    manual = {
        "De Volda Ao Laboratório": "de_volta_ao_laboratorio",
        "(objeto posicionado)": "objeto_posicionado",
        "ô cidade quente do cacete...": "a_cidade_quente_do_cacete",
        "Tô": "to",
        "➞": "game_over_finais",
        "De volta à Belém": "de_volta_a_belem",
        "De volta ao Aeroporto de Guarulhos": "de_volta_ao_aeroporto_de_guarulhos",
        "....": "quatro_pontos",
        "...": "tres_pontos",
    }
    if name in manual:
        return manual[name]
    s = unicodedata.normalize("NFKD", name)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return s[:90] or f"passagem_{pid}"


with open(TWINE, encoding="utf-8") as f:
    s = f.read()

startnode = int(re.search(r'startnode="(\d+)"', s).group(1))
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
    text = re.sub(r"\[\[[^\]]*\]\]?", "", text)
    text = re.sub(r"<[^>]+>", "", text).strip()
    # Harlowe: [[Ok]]! Vamos buscar → «Ok! Vamos buscar»
    text = re.sub(r"^\s*!\s*", "Ok! ", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    passages.append(
        {
            "pid": int(pid),
            "name": name,
            "slug": slug(name, pid),
            "links": links,
            "text": text,
        }
    )

slug_count = {}
for p in passages:
    base = p["slug"]
    if base in slug_count:
        slug_count[base] += 1
        p["slug"] = f"{base}_{slug_count[base]}"
    else:
        slug_count[base] = 0

with open(OUT_JSON, "w", encoding="utf-8") as o:
    json.dump({"startnode": startnode, "passages": passages}, o, ensure_ascii=False, indent=2)

print("Wrote", len(passages), "passages ->", OUT_JSON)
