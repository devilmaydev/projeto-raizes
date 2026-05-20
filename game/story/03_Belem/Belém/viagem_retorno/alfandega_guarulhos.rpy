## Alfândega — continuação em Guarulhos (Twine «Alfândega»). Termina em lab_posicionar_artefato_retorno.

label alfandega_guarulhos_desembarque_mochila_vazia:
    scene black
    with dissolve

    n "Horas depois, no Aeroporto Internacinal de Guarulhos, SP"
    n "Você está desembarcando e o segurança chama sua atenção:"
    n "\"Ei amigo, sua mochila tá aberta.\""
    n "Você checa e vê que a mochila está vazia"

    menu:
        "Voltar pra Belém":
            $ lab_proposital_maos_vazias = False
            call alfandega_belem_recuperacao_inicio from _call_alfandega_belem_recuperacao_inicio
        "Seguir mesmo assim":
            $ lab_proposital_maos_vazias = True
            $ artefato_id = None
            $ mochila_com_artefato = False
            call lab_posicionar_artefato_retorno from _call_lab_posicionar_artefato_retorno

    return


label alfandega_guarulhos_primeira_chegada:
    scene black
    with dissolve

    n "Horas depois, você desembarca no aeroporto internacional de Guarulhos, em São Paulo. Vcoê sabe que precisará passar pelo processo de novo."
    n "\"Olá precisamos que abra a mochila\""

    menu:
        "(abrir mochila e arrastar o arfetado de dentro dela para a mesa)":
            pass

    n "O que seria isso? Ah, objeto da sua pesquisa? Um objeto um tanto inusitado."
    n "Tudo bem, objeto liberado. Pode seguir!"

    menu:
        "Seguir":
            jump alfandega_guarulhos_ramificacao_seguir_sem_guardar
        "Guardar artefato novamente e seguir":
            jump alfandega_guarulhos_ramificacao_guardar


label alfandega_guarulhos_ramificacao_seguir_sem_guardar:
    $ mochila_com_artefato = False
    $ lab_proposital_maos_vazias = False
    call lab_posicionar_artefato_retorno from _call_lab_posicionar_artefato_retorno_1
    return


label alfandega_guarulhos_ramificacao_guardar:
    $ mochila_com_artefato = True
    call lab_posicionar_artefato_retorno from _call_lab_posicionar_artefato_retorno_2
    return
