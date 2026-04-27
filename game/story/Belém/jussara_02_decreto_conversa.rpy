## == Jussara — Decreto 12.600: “sou contra”, “a favor”, explicações, incorporar, prossiga ==

## Texto comum usado em `sou_contra` (2.º bloco) e em `prossiga`.
label jussara_fala_impacto_rios:
    j "Esses rios passam por dentro de reservas indígenas. A dragagem mata os animais e a poluição afeta toda a população da região Norte."
    j "Sem falar na intoxicação com agrotóxicos do excesso de monocultura. Florestas inteiras viraram plantações de soja, que além de tudo exalam um odor insuportável, que a população sequer consegue dormir direito com o cheiro..."

    return

label sou_contra:
    j "Ah, como é bom ouvir isso de um forasteiro! Sabe, esse decreto está pondo em risco todo o sistema hídrico do Pará..."

    call jussara_fala_impacto_rios from _call_jussara_fala_impacto_rios

    menu:
        "Quero ajudar":
            call quero_ajudar from _call_quero_ajudar
        "Os índios deveriam ser incorporados à sociedade como todo mundo":
            call incorporar_indios from _call_incorporar_indios
    return

label sou_a_favor:
    j "Você tá brincando?? Você sabe o impacto que esse decreto causará para mais de 14 povos originários e para toda a população da região norte?"

    menu:
        "Sei, não me importo":
            call sei_nao_me_importo from _call_sei_nao_me_importo
        "Conte-me mais":
            call conte_me_mais from _call_conte_me_mais
    return

label decreto_12_600:
    j "Sim, todo esse movimento que tu estás vendo aqui é em torno disso. E não somente aqui, há ocupações de povos indígenas em vários locais do estado, além de bloqueio de vias e manifestações nas ruas."

    menu:
        "Conte-me mais":
            call conte_me_mais from _call_conte_me_mais_1
    return

label sei_nao_me_importo:
    j "Você não pode estar falando sério!!"

    menu:
        "Estou sim":
            call estou_sim from _call_estou_sim
        "Claro que não, só zuando":
            call claro_que_nao from _call_claro_que_nao
    return

label estou_sim:
    j "Bom, não vejo porque darmos continuidade à essa pesquisa então. Tenha um bom dia."

    return

label claro_que_nao:
    j "Rum... Um pouco delicado brincar com uma questão dessa gravidade."

    menu:
        "Relaxa, gata":
            call relaxa_gata from _call_relaxa_gata
        "Eu sei, desculpe":
            call eu_sei_desculpe from _call_eu_sei_desculpe
    return

label relaxa_gata:
    j "Olha, definitivamente não deveríramos estar aqui conversando. Obrigado pela participação."

    return

label eu_sei_desculpe:
    j "Tudo bem, Mas e então, tu sabes mesmo o significado desse decreto?"

    menu:
        "Conte-me mais":
            call conte_me_mais from _call_conte_me_mais_2
        "Não me importo mesmo":
            call nao_me_importo from _call_nao_me_importo
    return

label conte_me_mais:
    j "Esse decreto visa a concessão do Rio Tapajós e mais outros dois rios daqui do Pará, o que, na prática, acaba sendo a privatização desses rios."

    menu:
        "E qual o problema?":
            call e_qual_o_problema from _call_e_qual_o_problema
        "Meu Deus, que triste!":
            call meu_deus_que_triste from _call_meu_deus_que_triste
        "Prossiga":
            call prossiga from _call_prossiga
    return

label e_qual_o_problema:
    j "O problema? Os problemas, né?"

    menu:
        "Prossiga":
            call prossiga from _call_prossiga_1
    return

label meu_deus_que_triste:
    j "Pois é, né?"
    call prossiga from _call_prossiga_2
    return

label prossiga:
    call jussara_fala_impacto_rios from _call_jussara_fala_impacto_rios_1
    menu:
        "Quero ajudar":
            call quero_ajudar from _call_quero_ajudar_1
        "Os índios deveriam ser incorporados à sociedade como todo mundo":
            call incorporar_indios from _call_incorporar_indios_1
    return

label nao_me_importo:
    j "Ah, é? Então faça o favor de se retirar da minha frente. Até mais..."

    return

label incorporar_indios:
    j "Tedoidé?? Tu não ouviste nada do que eu acabei de falar? Se não fossem os povos originários não havia talvez nem ar pra respirar direito."

    menu:
        "Você está exagerando":
            call exagerando from _call_exagerando
        "Não tinha parado pra pensar nisso":
            call nao_tinha_parado_pra_pensar from _call_nao_tinha_parado_pra_pensar
    return

label exagerando:
    j "Bom, sinto muito que pense dessa forma, mas acho melhor então pararmos por aqui. Até"

    return

label nao_tinha_parado_pra_pensar:
    j "Os indígenas ocuparm o acesso ao aeroporto de Santarém, bloquearam vias em todo o estado, manifestaram nas ruas em vários municípios, isso não é pouca coisa."

    menu:
        "Você está pessoalmente envolvida na causa?":
            call envolvida_na_causa from _call_envolvida_na_causa
        "Esse povo não tem o que fazer?":
            call esse_povo_nao_tem_o_que_fazer from _call_esse_povo_nao_tem_o_que_fazer
    return

label esse_povo_nao_tem_o_que_fazer:
    j "Isso só pode ser piada...."

    menu:
        "Era mesmo. Desculpe. Prossiga":
            call prossiga from _call_prossiga_3
        "Nem é":
            call nem_e from _call_nem_e
    return

label nem_e:
    j "Certo... Obrigado pela sua participação. Tenha um bom dia."
    return
