## Laboratório — após o processo em Alfândega (Belém + Guarulhos).
## Ramifica para o Twine conforme o artefato que chegou na mochila:
##   urna  → finais_twine.rpy («Finais», objeto certo)
##   outro → artefato_errado_twine.rpy («Voltando com o artefato errado»)

label lab_posicionar_artefato_retorno:
    scene bg sala_professor
    show professor idle at professor_sala_pose
    with dissolve

    if lab_proposital_maos_vazias:
        n "(voltando ao laboratória de mãis vazias propositalmente)"
        hide professor
        return

    if not mochila_com_artefato:
        n "(Voltando ao laboratório de mãos vazias, sem ter se dado conta)"
        hide professor
        return

    if artefato_id == "urna":
        call de_volta_ao_laboratorio from _call_finais_urna_lab
        return

    if artefato_id == "cuia":
        call voltando_com_a_cuia_de_tacaca from _call_voltando_cuia_lab
    elif artefato_id == "tapajonica":
        call voltando_com_a_ceramica_tapajonica from _call_voltando_tapajonica_lab
    elif artefato_id == "muiraquita":
        call voltando_com_o_muiraquita from _call_voltando_muiraquita_lab
    elif artefato_id == "retrato":
        call voltando_com_o_porta_retratos from _call_voltando_retrato_lab
    elif artefato_id == "premio":
        call voltando_com_o_premio_de_melhor_pesquisa from _call_voltando_premio_lab
    else:
        n "(voltando ao laboratório — objeto na mochila não mapeado para o Twine)"
        hide professor
        return

    hide professor
    return
