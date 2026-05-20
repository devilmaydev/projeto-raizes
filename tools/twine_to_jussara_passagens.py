# -*- coding: utf-8 -*-
"""Extrai passagens do Twine Jussara e gera slug + links."""
import re, html, json, sys

TWINE = r"C:\Users\fabio\Downloads\Jussara _ultima atualiza__o em 17 de Maio_.html"
OUT_JSON = r"c:\GameDev\Renpy Projects\Raizes\tools\jussara_passagens.json"

def slug(name):
    s = name.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s or s[0].isdigit():
        s = "p_" + s
    # reservados / duplicados conhecidos
    aliases = {
        "": "sem_titulo",
        "▶": "continuar_aeroporto",
        "➞": "continuar",
        "⇨": "continuar_alt",
        "abordagem_da_jussara": "abordagem_da_jussara",
        "(história}": "historia",
        "posso_sim": "posso_sim",
    }
    return aliases.get(s, s)[:80]

with open(TWINE, encoding="utf-8") as f:
    s = f.read()

passages = []
for m in re.finditer(
    r'<tw-passagedata pid="(\d+)" name="([^"]*)"[^>]*>(.*?)</tw-passagedata>',
    s,
    re.DOTALL,
):
    pid, name, body = m.group(1), m.group(2), m.group(3)
    links = re.findall(r"\[\[([^\]]+)\]\]", body)
    # limpar links: remover display|target harlowe style
    clean_links = []
    for lk in links:
        if "|" in lk:
            parts = lk.split("|")
            clean_links.append(parts[-1].strip())
        else:
            clean_links.append(lk.strip())
    text = html.unescape(body)
    text = re.sub(r"\[\[[^\]]+\]\]", "", text)
    text = re.sub(r"<[^>]+>", "", text).strip()
    passages.append({
        "pid": pid,
        "name": name,
        "slug": slug(name),
        "links": clean_links,
        "text": text,
    })

with open(OUT_JSON, "w", encoding="utf-8") as o:
    json.dump(passages, o, ensure_ascii=False, indent=2)

print(len(passages), "passages ->", OUT_JSON)
