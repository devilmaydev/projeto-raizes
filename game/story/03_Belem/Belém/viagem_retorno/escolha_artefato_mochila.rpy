## Se o canto da Jussara não fixou o artefato (ex.: missão com urna falhou), o jogador escolhe o que vai na mochila.
## Rótulos do menu copiam o Twine «Alfândega» (passagem ➞).

label escolha_artefato_na_mochila_para_viagem:
    menu:
        "Uma cuia de Tacacá, preta com grafismos amarelos":
            $ artefato_id = "cuia"
        "Um Muiraquitã, tamoanho grande":
            $ artefato_id = "muiraquita"
        "Um prêmio de Melhor Pesquisa em nome de Jussara":
            $ artefato_id = "premio"
        "Uma cerâmica Tapajônica em forma de homem sentado":
            $ artefato_id = "tapajonica"
        "Um porta-retratos com a fotografia de uma linda moça":
            $ artefato_id = "retrato"
        "Uma urna de cerâmica Marajoara":
            $ artefato_id = "urna"

    $ mochila_com_artefato = True
    return
