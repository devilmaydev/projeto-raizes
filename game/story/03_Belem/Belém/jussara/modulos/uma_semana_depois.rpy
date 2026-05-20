## Módulo — 1 semana depois (pós-história / decreto)

label jussara_1_semana_depois:
    $ jussara_checkpoint("uma_semana_depois")
    scene black with dissolve
    window hide

    show text Text("1 semana depois", size=72, text_align=0.5) as titulo_tempo:
        xalign 0.5
        yalign 0.5

    with dissolve
    pause 1.0

    hide titulo_tempo with dissolve
    window show

    scene bg mirante_rio with dissolve
    show jussara idle at jussara_show
    with dissolve

    j "Olá, novamente! Você já deve estar sabendo da boa notícia né?"

    menu:
        "Sim!":
            j "Sim - E muito graças a você por ter levado essa causa tão longe! Muito obrigada mesmo!"
        "Qual?":
            j "O decreto foi derrubado e agora podemos respirar aliviados, pelo menos por enquanto! E muito graças a você por ter levado essa causa tão longe! Muito obrigada mesmo!"

    j "Bom, acho que uma mão lava a outra, né? Então tá na hora de eu te ajudar na sua pesquisa também."
    j "Vem, vamos pro meu cantinho que eu te deixo dar uma olhada e procurar esse seu tal artefato."

    $ lab_proposital_maos_vazias = False
    $ canto_exit_urna_recusada = False
    call canto_jussara_point_n_click from _call_canto_jussara_point_n_click_timeskip
    if canto_exit_urna_recusada:
        $ canto_exit_urna_recusada = False
        return
    if artefato_id is None:
        call escolha_artefato_na_mochila_para_viagem from _call_escolha_artefato_na_mochila_para_viagem
        $ mochila_com_artefato = True
    call alfandega_belem_inicio from _call_alfandega_belem_inicio
    return
