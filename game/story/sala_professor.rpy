## Continuação da introdução: sala do professor.
## Edite este label com os diálogos/cenas da sala.

image bg sala_professor = im.Scale("images/Sala do Professor.jpg", 1920, 1080)
image professor idle = "images/Professor Idle.png"

transform professor_sala_pose:
    subpixel True
    xalign 0.74
    yalign 1.0
    yanchor 1.0
    zoom 0.8
    yoffset 370

label sala_professor:
    scene bg sala_professor
    with dissolve

    show professor idle at professor_sala_pose
    with dissolve

    p "E é por isso que eu tenho dedicado meus últimos anos estudos dos símbolos, artefatos e grafismos."
    p "Ah, desculpe o tom meio sério no começo da minha fala, é que eu me empolgo falando desse assunto."
    p "Acabo me sentindo narrando um documentário, sabe..."

    menu:
        "Tá tudo bem":
            call tudo_bem from _call_tudo_bem
        "Achei incrível!":
            call achei_incrivel from _call_achei_incrivel
        "Achei meio dramático....":
            call achei_meio_dramatico from _call_achei_meio_dramatico

    return

label achei_meio_dramatico:
    p "Ah, tudo bem, era só meu jeito de fazer as pessoas entrarem no clima.... Msa enfim, vamos ao que interessa: antes de mais nada, seja bem vindo ao Projeto de Extensão Raízes"
    call professor_bloco_missao_grafismos from _call_professor_bloco_missao_grafismos

    menu:
        "Por causa dos grafismos?":
            call por_causa_dos_grafismos from _call_por_causa_dos_grafismos
        "Existe algo ainda mais profundo?":
            call existe_algo_ainda_mais_profundo from _call_existe_algo_ainda_mais_profundo
    
    return

label tudo_bem:
    p "Ah, que bom! Vamos direto ao que interessa então: antes de mais nada, seja bem vindo ao Projeto de Extensão Raízes"
    call professor_bloco_missao_grafismos from _call_professor_bloco_missao_grafismos_1

    menu:
        "Por causa dos grafismos?":
            call por_causa_dos_grafismos from _call_por_causa_dos_grafismos_1
        "Existe algo ainda mais profundo?":
            call existe_algo_ainda_mais_profundo from _call_existe_algo_ainda_mais_profundo_1
    return

label por_causa_dos_grafismos:
    p "Exatamente! Esses grafismos parecem refletir a geometria sagrada das quais os místicos, hierofantes e magos têm falado há milênios."

    menu:
        "Prossiga":
            call prossiga_professor from _call_prossiga_professor
        "Sinto que havia algo além":
            call sinto_que_havia_algo_alem from _call_sinto_que_havia_algo_alem

    return

label prossiga_professor:
    p "Segundo lendas, esse artefato possui o poder de romper o véu que separa o mundo físico do mundo astral. Como o Caduceu de Mercúrio, uma ponte entre céu e terra."

    menu:
        "Que legal! Não vejo a hora de ir atrás disso":
            call que_legal_nao_vejo_a_hora_de_ir_atras_disso from _call_que_legal_nao_vejo_a_hora_de_ir_atras_disso
        "Gosto da alegoria":
            call gosto_da_alegoria from _call_gosto_da_alegoria
        "Balela":
            call balela from _call_balela
    return

label existe_algo_ainda_mais_profundo:
    p "Gostei de ver, você é dos meus, já vai direto ao ponto! De fato, existe sim algo bastante profundo e místico envolvendo esse artefato."

    menu:
        "Interessante, conte mais!":
            call interessante_conte_mais from _call_interessante_conte_mais
        "Não sou religioso":
            call nao_sou_religioso from _call_nao_sou_religioso
    return

label interessante_conte_mais:
    p "Segundo lendas, esse artefato possui o poder de romper o véu que separa o mundo físico do mundo astral. Como o Caduceu de Mercúrio, uma ponte entre céu e terra."

    menu:
        "Que legal! Não vejo a hora de ir atrás disso":
            call que_legal_nao_vejo_a_hora_de_ir_atras_disso from _call_que_legal_nao_vejo_a_hora_de_ir_atras_disso_1
        "Gosto da alegoria":
            call gosto_da_alegoria from _call_gosto_da_alegoria_1
        "Balela":
            call balela from _call_balela_1
    return

label balela:
    p "É, não é todo mundo que acredita no sobrenatural. E tá tudo bem, Bom, mas independente disso, não será um empencilho para sua missão"
    call professor_bloco_missao_belem from _call_professor_bloco_missao_belem
    return

label gosto_da_alegoria:
    p "Claro, nada do que é simbólico deve ser considerado ao pé da letra. O simbolismo é uma faceta da própria realidade, mas vista de uma diferente lente"
    p "Mas apesar disso, acredito que crença ou descrença alguma deverá atrapalhar de fato sua missão"
    call professor_bloco_missao_belem from _call_professor_bloco_missao_belem_1
    return


label que_legal_nao_vejo_a_hora_de_ir_atras_disso:
    p "Isso é ótimo, vejo que está empoulgado! Ñão há porque enrolar mais para te instruir em sua missão"
    call professor_bloco_missao_belem from _call_professor_bloco_missao_belem_2
    return

label como_sabe_tanto_assim_sobre_ela:
    p "Bom, é uma longa história... Digamos que eu possuo várias fonte em diferntes universidades pelo Brazil."

    menu:
        "Ah, networking":
            call ah_networking from _call_ah_networking
        "Não confio em você":
            call nao_confio_em_você from _call_nao_confio_em_você
    return

label ah_networking:
    p "Exatamente! E com o tempo você também poderá ter inúmeras conexões, não somente aqui em São Paulo, mas também em Belém, Recife, Goiânia e muitas outros lugares do Brasil e do mundo."

    menu:
        "Deixa comigo":
            call deixa_comigo from _call_deixa_comigo
        "Não confio em você":
            call nao_confio_em_você from _call_nao_confio_em_você_1
    return

label nao_confio_em_você:
    p "Entendo que não confie no seu orientador que acabou de conhecer. Mas não se preocupe, tenho meus motivos para agir assim"

    menu:
        "Vou dar uma chance":
            call vou_dar_uma_chance from _call_vou_dar_uma_chance
        "Não confio mesmo em você":
            call nao_confio_mesmo_em_você from _call_nao_confio_mesmo_em_você
    return

label nao_confio_mesmo_em_você:
    p "Você está falando sério?"

    menu:
        "Tava brincando":
            call tava_brincando_professor from _call_tava_brincando_professor_1
        "Pior que tô":
            call pior_que_tô from _call_pior_que_tô_1
    return

label vou_dar_uma_chance:
    call professor_bloco_convite_missao from _call_professor_bloco_convite_missao
    return

label achei_incrivel:
    p "Sério?! Er... digo, obrigado, sabe, todo mundo diz isso."

    menu:
        "Sem dúvida":
            call sem_duvida from _call_sem_duvida
        "Sei":
            call sei from _call_sei
    return

label sei:
    p "..."
    p "É, de fato, nem todo mundo curte. Mas enfim, vamos ao que interessa: antes de mais nada, seja bem vindo ao Projeto de Extensão Raízes"
    
    call professor_bloco_missao_grafismos from _call_professor_bloco_missao_grafismos_2
    
    menu:
        "Por causa dos grafismos?":
            call por_causa_dos_grafismos from _call_por_causa_dos_grafismos_2
        "Existe algo ainda mais profundo?":
            call existe_algo_ainda_mais_profundo from _call_existe_algo_ainda_mais_profundo_2
    return

label sem_duvida:
    p "Ah, pára! Tá me deixando sem graça! Mas enfim, vamos ao que interessa: antes de mais nada, seja bem vindo ao Projeto de Extensão Raízes."
    call professor_bloco_missao_grafismos from _call_professor_bloco_missao_grafismos_3

    menu:
        "Por causa dos grafismos?":
            call por_causa_dos_grafismos from _call_por_causa_dos_grafismos_3
        "Existe algo ainda mais profundo?":
            call existe_algo_ainda_mais_profundo from _call_existe_algo_ainda_mais_profundo_3
    return


label achei_meio_dramatico_curto:
    p "Obrigado pela compreensão."
    return

label sinto_que_havia_algo_alem:
    p "De fato. Você não deixa mesmo passar batido! Na verdade, há quem diga que esse artefato possui uma forte conexão com o astral!"

    menu:
        "Interessante, conte mais!":
            call interessante_conte_mais from _call_interessante_conte_mais_1
        "Não sou religioso":
            call nao_sou_religioso from _call_nao_sou_religioso_1
    return

label deixa_comigo:
    call professor_bloco_convite_missao from _call_professor_bloco_convite_missao_1
    return

label nao_sou_religioso:
    p "Tudo bem, eu entendo. Nesse caso podemos ir direto para sua missão"
    call professor_bloco_missao_belem from _call_professor_bloco_missao_belem_3
    return

label absolutamente:
    p "Então não que não percamos mais tempo! Descanse hoje o resto do dia. Amanhã cedo iremos para Guarulhos acompanhar você até o Aeroporto Internacional direto para Belém do Pará"
    call belem_aeroporto from _call_belem_aeroporto
    call belem_universidade from _call_belem_universidade
    return

label nem_pensar_professor:
    p "Está falando sério?"

    menu:
        "Tava brincando":
            call tava_brincando_professor from _call_tava_brincando_professor
        "Pior que tô":
            call pior_que_tô from _call_pior_que_tô

    return

label tava_brincando_professor: 
    p "Hahahaha, quase me pegou! Mas enfim, tudo o que você precisa fazer é encontrá-la, conversar com ela e convencê-la a conceder o 'artefato' empretado, para que você possa trazer de volta aqui para São Paulo para a conclusão da nossa pesquisa de extensão do Projeto Raízes"
    call professor_bloco_convite_missao from _call_professor_bloco_convite_missao_4
    
    return

label pior_que_tô:
    p "Por que não?"

    menu:
        "Não posso viajar":
            call nao_posso_viajar from _call_nao_posso_viajar
        "Não posso embarcar numa missão que não conheço completamente":
            call nao_posso_embarcar_numa_missao_que_nao_conheco_completamente from _call_nao_posso_embarcar_numa_missao_que_nao_conheco_completamente
        "Quer saber? Bora!":
            call quer_saber_bora from _call_quer_saber_bora
    return

label nao_posso_viajar:
    p "Entendi. Bom, sinto muito então. Tenho certeza que conseguiremos realocar você em outro setor da pesquisa. Então acho que por hoje é isso. Nos vemos em breve!"
    return

label nao_posso_embarcar_numa_missao_que_nao_conheco_completamente:
    p "Isso é perfeitamente compreensível, mas você acavou de chegar no projeto, ao longo da pesquisa eu irei aos poucos te contando como tudo isso se conecta. E então?"

    menu:
        "Tá bom, Deixa comigo":
            call tá_bom_deixa_comigo from _call_tá_bom_deixa_comigo
        "Desculpa, não mesmo":
            call desculpa_não_mesmo from _call_desculpa_não_mesmo
    return

label desculpa_não_mesmo:
    return

label tá_bom_deixa_comigo:
    call professor_bloco_convite_missao from _call_professor_bloco_convite_missao_2
    return

label quer_saber_bora:
    p "Assim que se fala! Então não que não percamos mais tempo! Descanse hoje o resto do dia. Amanhã cedo iremos para Guarulhos acompanhar você até o Aeroporto Internacional direto para Belém do Pará"
    call belem_aeroporto from _call_belem_aeroporto_1

    return

label qual_sua_verdadeira_intencao:
    p "Olha, não há porque acreditar que há uma intenção oculta por trás da minha pesquisa. Tudo o que posso dizer é que sou um entusiasta dos símbolos, grafismos e ideogramas...."
    
    menu:
        "Então tá":    
            call entao_tá from _call_entao_tá
        "Não confio mesmo em você":
            call nao_confio_mesmo_em_você from _call_nao_confio_mesmo_em_você_1

    return

label entao_tá:
    p "Ufa! Digo, er... Claro que temos todos nossas ambições pessoais. Mas o importante é justamente nos unirmos todos em busca de um objetivo em comum. Tenho certeza que você passou por todo aquele processo pela bolsa para se envolver e dedicar, certo?"

    menu:
        "Certo":
            call certo from _call_certo

    return

label certo:
    call professor_bloco_convite_missao from _call_professor_bloco_convite_missao_3
    return

label professor_bloco_missao_grafismos:
    p "Parábens por ter sido escolhido no processo seletivo para nossa bolsa! Foi uma seletiva muito árdua, mas ficamos felizes em ter você na nossa equipe"
    p "E para esse projeto em espefícico eu tenho uma missão muito especial!"
    p "Como havia dizendo, já pesquisei uma centenas de símbolos, ideogramas, grafismos... de várias eras e de diferentes regiões"
    p "Mas durante todo esse tempo eu havia negligenciado nosso próprio quintal."
    p "Os grafismos indígenas são a peça chave que falta para a conclusão do meu projeto."
    p "Nos últimos meses, tenho reunido o máximo de informação que pude para descobrir o paradeiro de um artefato que contempla vários pontos da minha pesquisa."
    return

label professor_bloco_missao_belem:
    p "Você irá realizar uma viagem, com tudo pago, para Belém, mais precisamente para a Universidade Federal do Pará, onde estuda nossa portadora do artefato"
    p "Ela se chama Jussara, jornalista e pesquisadora, ainda estuda na Univerdidade na sua pós-graduação."

    menu:
        "Deixa comigo":
            call deixa_comigo from _call_deixa_comigo_1
        "Como sabe tanto assim sobre ela":
            call como_sabe_tanto_assim_sobre_ela from _call_como_sabe_tanto_assim_sobre_ela
    return

label professor_bloco_convite_missao:
    p "Maravilha! Tudo o que você precisa fazer é encontrá-la, conversar com ela e convencê-la a conceder o artefato empretado, para que você possa trazer de volta aqui para São Paulo para a conclusão da nossa pesquisa de extensão do Projeto Raízes"
    p "Acha que consegue?"

    menu:
        "Absolutamente":
            call absolutamente from _call_absolutamente
        "Nem pensar":
            call nem_pensar_professor from _call_nem_pensar_professor
        "Qual sua verdadeira intenção?":
            call qual_sua_verdadeira_intencao from _call_qual_sua_verdadeira_intencao
    return
