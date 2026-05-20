## =============================================================================
## Ponto de entrada Belém (labels chamados por script.rpy e sala_professor)
## =============================================================================
## O Ren'Py carrega todos os .rpy; estes `call` encaminham a execução.

label belem_aeroporto:
    call cena_belem_aeroporto from _call_cena_belem_aeroporto
    return

label belem_universidade:
    call cena_belem_universidade_mirante from _call_cena_belem_universidade_mirante
    return
