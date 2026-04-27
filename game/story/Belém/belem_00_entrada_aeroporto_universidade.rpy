## =============================================================================
## belem_00 — Ponto de entrada (labels chamados por `script.rpy`)
## =============================================================================
## O Ren'Py carrega todos os .rpy; estes `call` encaminham a execução.

label belem_aeroporto:
    call cena_belem_aeroporto from _call_cena_belem_aeroporto
    return

label belem_universidade:
    call cena_belem_universidade_mirante from _call_cena_belem_universidade_mirante
    return
