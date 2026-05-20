## Belém — recuperação após mochila vazia em GRU (Twine «Alfândega»).

label alfandega_belem_recuperacao_inicio:
    scene bg aeroporto
    with dissolve

    n "De volta ao Aeroporto de Belém."

    menu:
        "Procurar a segurança":
            n "Olá! Sim, eu lembro de ti. Deixaste o teu \"objeto de pesquisa\" em cima da mesa. Todo afobado! Levei ele pro achados e perdidos"
        "Procurar achados e perdidos":
            pass

    n "Olá! Boas vindas"
    call alfandega_belem_recuperacao_menu_loop from _call_alfandega_belem_recuperacao_menu_loop
    return


label alfandega_belem_recuperacao_menu_loop:
    n "Poderia descrever esse seu objeto?"

    menu:
        "Uma cuia de Tacacá, preta com grafismos amarelos":
            if artefato_id == "cuia":
                n "(Se foi esse o objeto que você trouxe)"
                n "Ah, aqui está! Não esquça de guardar na mochila, hein?"
                $ mochila_com_artefato = True
                call alfandega_guarulhos_primeira_chegada from _call_alfandega_guarulhos_primeira_chegada_1
                return
            else:
                n "(Se não foi esse o objeto que você trouxe)"
                n "Desculpe, não encontramos nada assim aqui.  Quer tentar de novo?"
                jump alfandega_belem_recuperacao_menu_loop

        "Um Muiraquitã, tamoanho grande":
            if artefato_id == "muiraquita":
                n "(Se foi esse o objeto que você trouxe)"
                n "Ah, aqui está! Não esquça de guardar na mochila, hein?"
                $ mochila_com_artefato = True
                call alfandega_guarulhos_primeira_chegada from _call_alfandega_guarulhos_primeira_chegada_2
                return
            else:
                n "(Se não foi esse o objeto que você trouxe)"
                n "Desculpe, não encontramos nada assim aqui.  Quer tentar de novo?"
                jump alfandega_belem_recuperacao_menu_loop

        "Um prêmio de Melhor Pesquisa em nome de Jussara":
            if artefato_id == "premio":
                n "(Se foi esse o objeto que você trouxe)"
                n "Ah, aqui está! Não esquça de guardar na mochila, hein?"
                $ mochila_com_artefato = True
                call alfandega_guarulhos_primeira_chegada from _call_alfandega_guarulhos_primeira_chegada_3
                return
            else:
                n "(Se não foi esse o objeto que você trouxe)"
                n "Desculpe, não encontramos nada assim aqui.  Quer tentar de novo?"
                jump alfandega_belem_recuperacao_menu_loop

        "Uma cerâmica Tapajônica em forma de homem sentado":
            if artefato_id == "tapajonica":
                n "(Se foi esse o objeto que você trouxe)"
                n "Ah, aqui está! Não esquça de guardar na mochila, hein?"
                $ mochila_com_artefato = True
                call alfandega_guarulhos_primeira_chegada from _call_alfandega_guarulhos_primeira_chegada_4
                return
            else:
                n "(Se não foi esse o objeto que você trouxe)"
                n "Desculpe, não encontramos nada assim aqui.  Quer tentar de novo?"
                jump alfandega_belem_recuperacao_menu_loop

        "Um porta-retratos com a fotografia de uma linda moça":
            if artefato_id == "retrato":
                n "(Se foi esse o objeto que você trouxe)"
                n "Ah, aqui está! Não esquça de guardar na mochila, hein?"
                $ mochila_com_artefato = True
                call alfandega_guarulhos_primeira_chegada from _call_alfandega_guarulhos_primeira_chegada_5
                return
            else:
                n "(Se não foi esse o objeto que você trouxe)"
                n "Desculpe, não encontramos nada assim aqui.  Quer tentar de novo?"
                jump alfandega_belem_recuperacao_menu_loop

        "Uma urna de cerâmica Marajoara":
            if artefato_id == "urna":
                n "(Se foi esse o objeto que você trouxe)"
                n "Ah, aqui está! Não esquça de guardar na mochila, hein?"
                $ mochila_com_artefato = True
                call alfandega_guarulhos_primeira_chegada from _call_alfandega_guarulhos_primeira_chegada_6
                return
            else:
                n "(Se não foi esse o objeto que você trouxe)"
                n "Desculpe, não encontramos nada assim aqui.  Quer tentar de novo?"
                jump alfandega_belem_recuperacao_menu_loop
