## Twine: «Voltando com o artefato errado» (ficheiro único)
## Quando: já passou por Alfândega e está no lab do professor com objeto errado (não é a urna).
## Entrada: lab_posicionar_artefato_retorno.rpy (após alfandega_guarulhos → lab)
## Regenerar: python tools/twine_to_artefato_errado.py && python tools/generate_artefato_errado_twine.py

## Mapa Twine → label
## 'De volta ao Lab (com o artefato errado)' → de_volta_ao_lab_com_o_artefato_errado (pid 1)
## 'Voltando com a Cuia de Tacacá' → voltando_com_a_cuia_de_tacaca (pid 2)
## 'Voltando com a Cerâmica Tapajônica' → voltando_com_a_ceramica_tapajonica (pid 3)
## 'Voltando com o Muiraquitã' → voltando_com_o_muiraquita (pid 4)
## 'Voltando com o Porta Retratos' → voltando_com_o_porta_retratos (pid 5)
## 'Voltando com o Prêmio de Melhor Pesquisa' → voltando_com_o_premio_de_melhor_pesquisa (pid 6)
## 'Este é o artefato' → este_e_o_artefato (pid 7)
## '(Você posiciona e nada acontece)' → voce_posiciona_e_nada_acontece (pid 8)
## 'Tá bem...' → ta_bem (pid 9)
## 'Nem a pau' → nem_a_pau (pid 10)

# ========================================================================
# pid 001 — de_volta_ao_lab_com_o_artefato_errado
# ========================================================================

## Twine: "De volta ao Lab (com o artefato errado)" (pid 1)
label de_volta_ao_lab_com_o_artefato_errado:
    # Twine: (essas variações acontecerão a partir do momento em que o Professor pedir para você abrir a mochila e posicionar o artefato)

    menu:
        "Voltando com a Cuia de Tacacá":
            call voltando_com_a_cuia_de_tacaca from _call_voltando_com_a_cuia_de_tacaca
        "Voltando com a Cerâmica Tapajônica":
            call voltando_com_a_ceramica_tapajonica from _call_voltando_com_a_ceramica_tapajonica
        "Voltando com o Muiraquitã":
            call voltando_com_o_muiraquita from _call_voltando_com_o_muiraquita
        "Voltando com o Porta Retratos":
            call voltando_com_o_porta_retratos from _call_voltando_com_o_porta_retratos
        "Voltando com o Prêmio de Melhor Pesquisa":
            call voltando_com_o_premio_de_melhor_pesquisa from _call_voltando_com_o_premio_de_melhor_pesquisa

    return

# ========================================================================
# pid 002 — voltando_com_a_cuia_de_tacaca
# ========================================================================

## Twine: "Voltando com a Cuia de Tacacá" (pid 2)
label voltando_com_a_cuia_de_tacaca:
    p "Uma cuia de Tacacá? Sério? Quer dizer, sem dúvida é um obejto bem ancesral, mas duvido que tenham atribuido propriedades místicas em um objeto tão comum..."
    p "De qualquer forma vamos testá-lo."
    p "Esta aqui é uma tabuleta antiga com poderes misteriosos. Essa luz fosforescente dela fica mais forte diante do artefato. Posicione sobre ela então eu estiver com as mãos posicionadas. Proto?"

    menu:
        "(Você posiciona e nada acontece)":
            call voce_posiciona_e_nada_acontece from _call_voce_posiciona_e_nada_acontece

    return

# ========================================================================
# pid 003 — voltando_com_a_ceramica_tapajonica
# ========================================================================

## Twine: "Voltando com a Cerâmica Tapajônica" (pid 3)
label voltando_com_a_ceramica_tapajonica:
    p "Cerâmica interessante! Bem Tapajônica e bem ancesrtral. É um forte candidato a ser nosso artefato!"
    p "Vmos testá-lo."
    p "Esta aqui é uma tabuleta antiga com poderes misteriosos. Essa luz fosforescente dela fica mais forte diante do artefato. Posicione sobre ela então eu estiver com as mãos posicionadas. Proto?"

    menu:
        "(Você posiciona e nada acontece)":
            call voce_posiciona_e_nada_acontece from _call_voce_posiciona_e_nada_acontece_1

    return

# ========================================================================
# pid 004 — voltando_com_o_muiraquita
# ========================================================================

## Twine: "Voltando com o Muiraquitã" (pid 4)
label voltando_com_o_muiraquita:
    p "Um Muiraquitã? Interessante, suspeitava que fosse algo relacionado à cultura Tapajônica, mas não imaginava que fossse um Muiraquitã. Sei que é muito usado como amuleto de sorte no Pará, e que só é dado de presente."
    p "Ainda assim acho que talvez não seja por aí. De qualquer forma vamos testá-lo."
    p "Esta aqui é uma tabuleta antiga com poderes misteriosos. Essa luz fosforescente dela fica mais forte diante do artefato. Posicione sobre ela então eu estiver com as mãos posicionadas. Proto?"

    menu:
        "(Você posiciona e nada acontece)":
            call voce_posiciona_e_nada_acontece from _call_voce_posiciona_e_nada_acontece_2

    return

# ========================================================================
# pid 005 — voltando_com_o_porta_retratos
# ========================================================================

## Twine: "Voltando com o Porta Retratos" (pid 5)
label voltando_com_o_porta_retratos:
    p "Um porta-retratos de família da Jussara? Okay, então a associação que você fez aqui de ancestralidade do artefato com a figura histórica que sua avó representa para ela;"
    p "Ainda assim acho que talvez não seja por aí. De qualquer forma vamos testá-lo."
    p "Esta aqui é uma tabuleta antiga com poderes misteriosos. Essa luz fosforescente dela fica mais forte diante do artefato. Posicione sobre ela então eu estiver com as mãos posicionadas. Proto?"

    menu:
        "(Você posiciona e nada acontece)":
            call voce_posiciona_e_nada_acontece from _call_voce_posiciona_e_nada_acontece_3

    return

# ========================================================================
# pid 006 — voltando_com_o_premio_de_melhor_pesquisa
# ========================================================================

## Twine: "Voltando com o Prêmio de Melhor Pesquisa" (pid 6)
label voltando_com_o_premio_de_melhor_pesquisa:
    p "O que é isso? Um prêmio de melhor pesquisa da Jussara? Mas e o artefato?"

    menu:
        "Este é o artefato":
            call este_e_o_artefato from _call_este_e_o_artefato

    return

# ========================================================================
# pid 007 — este_e_o_artefato
# ========================================================================

## Twine: "Este é o artefato" (pid 7)
label este_e_o_artefato:
    p "Acho difícil.... Apesar desses grafismos na moldura, acho difícil que esse objeto seja assim tão ancestral."
    p "Ainda assim acho que talvez não seja por aí. De qualquer forma vamos testá-lo."
    p "Esta aqui é uma tabuleta antiga com poderes misteriosos. Essa luz fosforescente dela fica mais forte diante do artefato. Posicione sobre ela então eu estiver com as mãos posicionadas. Proto?"

    menu:
        "(Você posiciona e nada acontece)":
            call voce_posiciona_e_nada_acontece from _call_voce_posiciona_e_nada_acontece_4

    return

# ========================================================================
# pid 008 — voce_posiciona_e_nada_acontece
# ========================================================================

## Twine: "(Você posiciona e nada acontece)" (pid 8)
label voce_posiciona_e_nada_acontece:
    p "Hmm... apesar de a tabuleta ter acendido na presença do objeto, acredito que foi porque ele está ligado com a portadora do artefato real."
    p "Eu sinto muito, mas você terá que voltar lá e procurar novamente pelo objeto."

    menu:
        "Tá bem...":
            call ta_bem from _call_ta_bem
        "Nem a pau":
            call nem_a_pau from _call_nem_a_pau

    return

# ========================================================================
# pid 009 — ta_bem
# ========================================================================

## Twine: "Tá bem..." (pid 9)
label ta_bem:
    # Twine: (embarque de volta)
    call alfandega_belem_recuperacao_inicio from _call_ta_bem_recuperacao
    return

# ========================================================================
# pid 010 — nem_a_pau
# ========================================================================

## Twine: "Nem a pau" (pid 10)
label nem_a_pau:
    p "Tudo bem, iremos mandar outro bolsista."
    p "A propósito, pode arrumar suas coisas..."
    return
