## == Jussara — convite da pesquisa, “Nem pensar”, “Te procurando”, artefato, etc. ==

## Bloco reutilizável: mesma pergunta (usada em pode_sim, nao_zuando, posso_sim).
label jussara_pergunta_opiniao_decreto:
    j "Ah, obrigada! Então vamos lá. Primeira pergunta: qual sua opinião sobre o Decreto Nº 12.600?"

    menu:
        "Sou contra":
            call sou_contra from _call_sou_contra
        "Sou a favor":
            call sou_a_favor from _call_sou_a_favor
        "Decreto 12.600?":
            call decreto_12_600 from _call_decreto_12_600

    return


label pode_sim:
    call jussara_pergunta_opiniao_decreto from _call_jussara_pergunta_opiniao_decreto
    return

label nem_pensar:
    j "Com assim? Sério mesmo?"

    menu:
        "Sim, sério mesmo":
            call sim_serio_mesmo from _call_sim_serio_mesmo
        "Não, só zuando":
            call nao_zuando from _call_nao_zuando

    return

label te_procurando:
    j "Como assim \"estava me procurando\"? Quem é você?"

    menu:
        "Tava Brincando":
            call tava_brincando from _call_tava_brincando
        "Sou pesquisador de SP":
            call sou_pesquisador_de_sp from _call_sou_pesquisador_de_sp
        "Busco algo em sua posse":
            call busco_algo_em_sua_posse from _call_busco_algo_em_sua_posse

    return


label tava_brincando:
    j "Hmm... engraçadinho. Enfim, pode me conceder algumas respostas então?"

    menu:
        "Posso Sim":
            call posso_sim from _call_posso_sim
        "Nem pensar":
            call sim_serio_mesmo from _call_sim_serio_mesmo_1
        "O artefato primeiro":
            call artefato_primeiro from _call_artefato_primeiro
    return

label posso_sim:
    call jussara_pergunta_opiniao_decreto from _call_jussara_pergunta_opiniao_decreto_1
    return

label artefato_primeiro:
    j "Artefato? Que artefato?"

    menu:
        "Preciso que me ajude a descobrir":
            call preciso_que_me_ajude_a_descobrir from _call_preciso_que_me_ajude_a_descobrir
        "Um artefato mágico que transforma a realidade":
            call um_artefato_magico_que_transforma_a_realidade from _call_um_artefato_magico_que_transforma_a_realidade
    return

label preciso_que_me_ajude_a_descobrir:
    j "Desculpe, mas não faço ideia do que se trata. Tem certeza que sou eu?"

    menu:
        "Absoluta":
            call absoluta from _call_absoluta
        "Tava brincando":
            call tava_brincando_volta_ao_decreto from _call_tava_brincando_volta_ao_decreto
    return

## Evita chamar de novo `tava_brincando` (ciclo) — volta à pergunta do Decreto.
label tava_brincando_volta_ao_decreto:
    j "Então a gente volta ao que interessa, pode ser?"
    call posso_sim from _call_posso_sim_1
    return

label um_artefato_magico_que_transforma_a_realidade:
    j "Olha, eu não sei que espécie de jogo é essa, onde tu falas de coisas fantasiosas enquanto eu tô aqui te perguntando coisas sérias..."

    menu:
        "Perdão":
            call perdão from _call_perdão
        "Não acho tão sério assim":
            call nao_acho_tao_serio_assim from _call_nao_acho_tao_serio_assim
    return

label perdão:
    j "Tudo bem. Mas e aí, podes responder o questionário?"

    menu:
        "Posso Sim":
            call posso_sim from _call_posso_sim_2
        "Nem pensar":
            call sim_serio_mesmo from _call_sim_serio_mesmo_2
    return

label nao_acho_tao_serio_assim:
    j "Ah, é? Então faça o favor de se retirar da minha frente. Até mais..."

    return

label absoluta:
    j "Ué, nunca ouvi falar de nenhum artefato que altere a realidade, a não ser que esteja falando de substâncias. Bom, nesse caso acho que que vai conseguir te ajudar com isso são os moleques que ficam ali perto do Vadião."
    j "Bom, espero que encontre o que procura então. Até um outro dia"
    return

label sou_pesquisador_de_sp:
    j "Um pesquisador que estava me procurando? Para que exatamente?"

    menu:
        "Busco algo em sua posse":
            call busco_algo_em_sua_posse from _call_busco_algo_em_sua_posse_1
        "Ajudar na sua pesquisa":
            call ajudar_na_sua_pesquisa from _call_ajudar_na_sua_pesquisa
    return

label busco_algo_em_sua_posse:
    j "Não sei se eu tô entendendo direito. Bom, acho que tu não podes me ajudar com a pesquisa então, né?"

    menu:
        "Posso Sim":
            call posso_sim from _call_posso_sim_3
        "Nem pensar":
            call sim_serio_mesmo from _call_sim_serio_mesmo_3
        "O artefato primeiro":
            call artefato_primeiro from _call_artefato_primeiro_1
    return

label nao_zuando:
    call jussara_pergunta_opiniao_decreto from _call_jussara_pergunta_opiniao_decreto_2
    return

label sim_serio_mesmo:
    j "Ah, tudo bem, entendo... Enfim, obrigado pela atenção! Tenha um bom dia!"

    return

label ajudar_na_sua_pesquisa:
    j "Ah sim! Égua, que bom que tu já estavas disposto a ajudar no projeto, fico feliz com isso. Então, vamos lá, podes responder as perguntas agora?"

    menu:
        "Posso Sim":
            call posso_sim from _call_posso_sim_4
        "Nem pensar":
            call sim_serio_mesmo from _call_sim_serio_mesmo_4
        "O artefato primeiro":
            call artefato_primeiro from _call_artefato_primeiro_2

    return
