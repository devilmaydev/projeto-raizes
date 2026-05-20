## == Belém — aeroporto (narrador) ==
## Chamado a partir de belem/entrada.rpy (label cena_belem_aeroporto)

label cena_belem_aeroporto:
    scene bg aeroporto
    with dissolve
    call belem from _call_belem_passagem
    return
