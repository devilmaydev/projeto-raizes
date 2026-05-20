# -*- coding: utf-8 -*-
"""
Organização por ATOS (pastas rasas) — melhor para editar que árvore escolhas/.../escolhas.

Gera: tools/jussara_passagem_paths.json  (slug → 02_campus_mirante/foo.rpy)
"""
from __future__ import annotations

import json
import os

from jussara_filename import passagem_filename
from jussara_paths import (
    JSON_IN,
    ROOT,
    SYSTEM_SLUGS,
    build_graph,
    link_to_slug,
    load_passages,
)
from jussara_roots import passagens_root_rel

PATHS_JSON = os.path.join(os.path.dirname(__file__), "jussara_passagem_paths.json")

ACT_01 = frozenset({"belem", "continuar_aeroporto"})

# Entradas do fio «artefato» (vários caminhos do Twine convergem aqui).
ARTEFATO_SEEDS = frozenset(
    {
        "isso_me_lembra_de_um_certo_arfefato",
        "o_artefato_primeiro",
        "preciso_que_me_ajude_a_descobrir",
        "um_artefato_magico_que_transforma_a_realidade",
        "busco_algo_em_sua_posse",
        "sou_pesquisador_de_sp",
        "ajudar_na_sua_pesquisa",
        "preciso_que_me_empreste_um_artefato",
        "gostaria_que_me_emprestasse_um_artefato_seu",
        "e_uma_mao_lava_a_outra",
        "primeiro_voce",
        "agora_preciso_da_sua_ajuda",
        "na_verdade_agora_queria_pedir_sua_ajuda",
        "perdao",
        "nao_acho_tao_serio_assim",
        "absoluta",
    }
)

# Pós-mirante / módulos / combinados finais.
ACT_04_SEEDS = frozenset(
    {
        "uma_semana_depois",
        "uma_semana_depois_optou_nao_perguntar",
        "historia",
        "me_conta_a_historia",
        "beleza",
        "vamo_e_agora",
        "pode_ser_ufpa_veropesinho",
        "pode_ser_ver_o_peso",
        "veropesinho",
        "feito",
        "pacas",
        "de_nada",
        "interessante",
        "qual_a_chave_pix",
    }
)

# Passagens só com call a módulo ou pouco ligadas no grafo exportado.
MANUAL_ACT = {
    "uma_semana_depois": "04_encerramento",
    "uma_semana_depois_optou_nao_perguntar": "04_encerramento",
    "historia": "04_encerramento",
    "e_dai": "02_campus_mirante",
    "nao_obrigado": "03_artefato_conversa",
    "nao_mesmo_sinto_muito": "03_artefato_conversa",
}

ACT_LABELS = {
    "01_aeroporto": "Aeroporto de Belém",
    "02_campus_mirante": "UFPA / Mirante / decreto e conversa",
    "03_artefato_conversa": "Fio do artefato (perguntas e desvios)",
    "04_encerramento": "Fechamento mirante → história / 1 semana",
    "_sistema": "Game over e ramos globais",
    "_orfas": "Passagens soltas ou só no Twine",
}


def assign_acts(passages, name_to_slug):
    """Primeira visita desde belem; marcos forçam o ato (evita loops Twine)."""
    from collections import deque

    by_slug, children, _parents = build_graph(passages, name_to_slug)
    acts: dict[str, str] = {}
    q = deque([("belem", "01_aeroporto")])

    while q:
        slug, parent_act = q.popleft()
        if slug in acts:
            continue
        if slug not in by_slug:
            continue

        if slug in SYSTEM_SLUGS:
            act = "_sistema"
        elif slug in ACT_01:
            act = "01_aeroporto"
        elif slug in ARTEFATO_SEEDS:
            act = "03_artefato_conversa"
        elif slug in ACT_04_SEEDS:
            act = "04_encerramento"
        elif parent_act == "01_aeroporto":
            act = "02_campus_mirante"
        else:
            act = parent_act

        acts[slug] = act
        for _, child in children.get(slug, []):
            if child in by_slug:
                q.append((child, act))

    for slug in by_slug:
        if slug not in acts:
            acts[slug] = "_orfas"

    for slug, act in MANUAL_ACT.items():
        if slug in by_slug:
            acts[slug] = act

    return acts, by_slug, children


def rel_path(act: str, slug: str, pid: int | str) -> str:
    return f"{act}/{passagem_filename(slug, pid)}".replace("\\", "/")


def slug_pids(passages) -> dict[str, int]:
    return {p["slug"]: int(p["pid"]) for p in passages if "pid" in p}


def enrich_pids_from_disk(pids: dict[str, int]) -> dict[str, int]:
    from jussara_filename import pid_from_file, slug_from_basename

    out = dict(pids)
    for dirpath, _dirs, files in os.walk(ROOT):
        for fn in files:
            if not fn.endswith(".rpy"):
                continue
            slug = slug_from_basename(fn)
            if slug in out:
                continue
            pid = pid_from_file(os.path.join(dirpath, fn))
            if pid is not None:
                out[slug] = pid
    return out


def write_paths_json(acts: dict[str, str], pids: dict[str, int]):
    payload = {
        "version": 4,
        "layout": "atos",
        "root": passagens_root_rel(),
        "filename_pattern": "p{pid:03d}_{slug}.rpy",
        "acts": ACT_LABELS,
        "paths": {
            slug: rel_path(act, slug, pids[slug])
            for slug, act in sorted(acts.items())
            if slug in pids
        },
    }
    with open(PATHS_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return payload


def write_readmes(acts: dict[str, str], by_slug: dict, pids: dict[str, int]):
    os.makedirs(ROOT, exist_ok=True)
    main = [
        "# Passagens Jussara",
        "",
        "Organização por **ato** (pastas rasas). Ficheiros: `p{pid:03d}_{slug}.rpy` (pid = Twine). Label Ren'Py = `slug` (sem o prefixo).",
        "",
        "| Pasta | Conteúdo |",
        "|-------|----------|",
    ]
    for act_id, title in ACT_LABELS.items():
        n = sum(1 for a in acts.values() if a == act_id)
        main.append(f"| `{act_id}/` | {title} ({n} ficheiros) |")
    main.extend(
        [
            "",
            "## Atalhos",
            "",
            "- Entrada: `01_aeroporto/p001_belem.rpy`",
            "- Abordagem: `02_campus_mirante/p005_abordagem_da_jussara.rpy` (pid no Twine pode variar — ver cabeçalho do .rpy)",
            "- Artefato: `03_artefato_conversa/p…_isso_me_lembra_de_um_certo_arfefato.rpy`",
            "- Módulos grandes: `../modulos/` (canto, história, 1 semana)",
            "",
            "## Regenerar do Twine",
            "",
            "```bash",
            "python tools/twine_to_jussara_passagens.py",
            "python tools/generate_jussara_passagens.py",
            "python tools/jussara_acts.py",
            "python tools/rename_passagens_with_pid.py",
            "python tools/migrate_passagens_layout.py",
            "```",
            "",
        ]
    )
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(main))

    for act_id, title in ACT_LABELS.items():
        slugs = sorted(s for s, a in acts.items() if a == act_id)
        if not slugs:
            continue
        lines = [
            f"# {act_id} — {title}",
            "",
            f"{len(slugs)} passagens. **Ctrl+P** pelo slug (`nem_pensar`) ou pelo pid (`p037`).",
            "",
        ]
        if act_id == "01_aeroporto":
            lines.extend(
                [
                    "## Fluxo",
                    "",
                    "`belem` → `continuar_aeroporto` → (campus em `02_campus_mirante`)",
                    "",
                ]
            )
        elif act_id == "02_campus_mirante":
            lines.extend(
                [
                    "## Fluxo (resumo)",
                    "",
                    "`universidade_federal_do_para` → `mirante_do_rio` → `abordagem_da_jussara`",
                    "→ ramos `posso_sim` / `nem_pensar` / `eu_ja_estava_te_procurando_mesmo` (decreto, pix, etc.)",
                    "→ `me_conta_a_historia` e fim levam a `04_encerramento` / `modulos/`",
                    "",
                ]
            )
        elif act_id == "03_artefato_conversa":
            lines.extend(
                [
                    "## Fluxo (resumo)",
                    "",
                    "Entradas típicas: `isso_me_lembra_de_um_certo_arfefato`, `o_artefato_primeiro`,",
                    "`preciso_que_me_ajude_a_descobrir`, ramos de `eu_ja_estava_te_procurando_mesmo`.",
                    "Game overs: `call game_over_continuar` → pasta `_sistema/`.",
                    "",
                ]
            )
        lines.extend(["## Ficheiros", ""])
        for s in slugs:
            name = by_slug[s]["name"]
            pid = pids.get(s, "?")
            if isinstance(pid, int):
                lines.append(f"- `p{pid:03d}_{s}.rpy` — Twine pid {pid}: «{name}»")
            else:
                lines.append(f"- `{s}.rpy` — «{name}»")
        act_dir = os.path.join(ROOT, act_id)
        os.makedirs(act_dir, exist_ok=True)
        with open(os.path.join(act_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    passages, name_to_slug = load_passages()
    acts, by_slug, _ = assign_acts(passages, name_to_slug)
    pids = enrich_pids_from_disk(slug_pids(passages))
    write_paths_json(acts, pids)
    write_readmes(acts, by_slug, pids)
    from collections import Counter

    c = Counter(acts.values())
    print("Atos:", dict(c))
    print("Wrote", PATHS_JSON)
