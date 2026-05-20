## Alfândega — retorno com o artefato na mochila (qual for o escolhido em Belém).
## Primeira viagem: após canto / 1 semana → escolha mochila → Belém → Guarulhos → laboratório.
## Twine de referência: «Alfândega». Recuperação (objeto perdido/errado): alfandega_belem_recuperacao.rpy

label alfandega_belem_inicio:
    scene bg aeroporto
    with dissolve

    n "Você está de volta ao aeroporto internacional de Belém. A missão está quase cumprida. Por hora tudo o que precisamos é embarcar de volta para São Paulo, mas, é claro, sem antes passar na alfândega"

    call alfandega_belem_posto from _call_alfandega_belem_posto
    return


label alfandega_belem_posto:
    n "(talvez haja inclusão de uma personagem da segurança do aeroporto)"
    n "Olá! Vamos precisar que abra sua mochila e nos mostre o que tem dentro, por gentileza"

    menu:
        "POint N' Click + Point N' Drag (o jogador clica na mochila para abrí-la e arrasta o objeto para cima da mesa)":
            pass

    n "O que é isso?"

    menu:
        "objeto da minha pesquisa":
            pass

    n "Hmmm... tudo bem. Está linerado. Pode seguir"
    n "(O botão de seguir estatá como elemento de Point N' Click. O jogador poderar clicar no botão de seguir desde já, mas o artefato ainda estará em cima da mesa e estatá também visível o sprite da mochila aberta. Ou seja"

    menu:
        "(click no botão \"Seguir\")":
            jump alfandega_belem_ramificacao_seguir_sem_guardar
        "Guardar artefato e seguir":
            jump alfandega_belem_ramificacao_guardar


label alfandega_belem_ramificacao_seguir_sem_guardar:
    $ mochila_com_artefato = False
    call alfandega_guarulhos_desembarque_mochila_vazia from _call_alfandega_guarulhos_desembarque_mochila_vazia
    return


label alfandega_belem_ramificacao_guardar:
    $ mochila_com_artefato = True
    call alfandega_guarulhos_primeira_chegada from _call_alfandega_guarulhos_primeira_chegada
    return
