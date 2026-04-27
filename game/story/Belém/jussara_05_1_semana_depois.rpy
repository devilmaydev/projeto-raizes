## == Jussara 05 — 1 semana depois ==

label jussara_1_semana_depois:
    scene black with dissolve

    centered "{size=72}1 semana depois{/size}"

    with dissolve
    pause 1.0

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

    call canto_jussara_point_n_click from _call_canto_jussara_point_n_click_timeskip
    return
