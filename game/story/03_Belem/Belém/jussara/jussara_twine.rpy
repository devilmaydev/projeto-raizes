## Arco Jussara — passagens Twine (ficheiro único)
## Labels = slug Twine. Ordem abaixo = pid no Harlowe.
## Módulos interativos: modulos/ (canto, história, 1 semana).
## Regenerar a partir das passagens: python tools/merge_jussara_twine.py

# ============================================================================
# Game over
# ============================================================================

## Game over do arco Jussara: fundo preto, sem background nem sprites.

label jussara_game_over_setup:
    window hide
    scene black with dissolve
    hide jussara
    window show
    return

# ============================================================================
# pid 001 — belem
# ============================================================================

## Twine: "Belém" (pid 1)
label belem:
    $ jussara_checkpoint("belem_aeroporto")
    n "Você acaba de desembarcar no Aeroporto Internacional de Belém. A brisa das árvores e de um céu longe de prédios do bairro do Marex quase disfarça o calor e o mormaço que envolvem a cidade como uma redoma."
    n "Você quase consegue aproveitar a brisa, fechando os olhos e inspirando o ar profundamente, mas, ao tempo de expirar o ar de volta, a brisa já se dissipou em meio a gotículas de águas em temperatura escaldante, deixando sua pele e roupa enxarcada antes mesmo da segunda inspirada."

    call continuar_aeroporto from _call_continuar_aeroporto

    return

# ============================================================================
# pid 002 — universidade_federal_do_para
# ============================================================================

## Twine: "Universidade Federal do Pará" (pid 2)
label universidade_federal_do_para:
    scene bg portao_iii_ufpa
    with dissolve

    n "Você desembarca no Portão III, o mais próximo do Rio Guamá. Dá graças a Deus pelo campus ser longe do centro urbano. Ao contrário: é às margens de um rio belíssimo, cheio de vida e natureza. Você logo se mistura à fila inevitável que se forma na entrada, para então se dissipar após o portão e, e,m seguida, se reorganizar novamente nas calçadas e pontes de acesso que sobrepairam os riachos que cortam a universidade. Você nota um movimento de gente se formando ao chegar perto do enorme prédio que concentra os cursos de humanas e licenciaturas, o"

    call mirante_do_rio from _call_mirante_do_rio

    return

# ============================================================================
# pid 003 — mirante_do_rio
# ============================================================================

## Twine: "Mirante do Rio" (pid 3)
label mirante_do_rio:
    scene bg mirante_rio
    with dissolve

    n "Estudantes por todos os lados espalhados, com placas, bandeiras, pôsteres. Nota-se uma mobilização por alguma pauta do momento. Você passeia com os olhos buscando encontrar pistas da nossa ''Portadora do Artefato''. Não demora para você mesmo ser surpreendido por quem está ali entrevistando pessoas para a sua pesquisa."

    call abordagem_da_jussara from _call_abordagem_da_jussara
    return

# ============================================================================
# pid 004 — continuar_aeroporto
# ============================================================================

## Twine: "▶" (pid 4)
label continuar_aeroporto:
    n "Ficar o máximo possível no ar-condicionado é a solução paliativa ideal no momento. Pedir um Uber Black com um ar trincando enquanto espera do lado de dentro do aeroporto e experimenta os exóticos sorvetes de frutas regionais, como o Cupuaçú, o Acaí, o Taperebá e o Bacurí. A experiência não está tão ruim assim, afinal. Antes você estava doido para partir, agora você até pensa que o motorista podia demorar um pouco mais para você degustar os sorvetes com mais calma. Eis que o carro chega, você empurra g'uela abaixo o resto da casquinha e embarca rumo à"

    return

# ============================================================================
# pid 005 — abordagem_da_jussara
# ============================================================================

## Twine: "abordagem da Jussara" (pid 5)
label abordagem_da_jussara:
    $ jussara_checkpoint("abordagem_jussara")
    show jussara idle at jussara_show
    with dissolve

    # Twine: (a imagem da personagem aparece em primeiro plano)
    j "Olá! Tudo bem? Prazer, eu me chamo Jussara, sou estudante de pós-graduação do curso de jornalismo aqui na UFPA. Meu grupo e eu estamos realizando um projeto de pesquisa e gostaria de te fazer algumas perguntas, pode ser?"

    menu:
        "Posso sim":
            call posso_sim from _call_posso_sim
        "Eu já estava te procurando mesmo":
            call eu_ja_estava_te_procurando_mesmo from _call_eu_ja_estava_te_procurando_mesmo
        "Nem pensar":
            call nem_pensar from _call_nem_pensar

    return

# ============================================================================
# pid 006 — posso_sim
# ============================================================================

## Twine: "Posso sim" (pid 6)
label posso_sim:
    # Twine: (Jussara assume uma expressão feliz)
    j "Ah, obrigada! Então vamos lá. Primeira pergunta: qual sua opinião sobre o Decreto Nº 12.600?"

    menu:
        "Sou contra":
            call sou_contra from _call_sou_contra
        "Sou a favor":
            call sou_a_favor from _call_sou_a_favor
        "Decreto 12.600?":
            call decreto_12_600 from _call_decreto_12_600

    return

# ============================================================================
# pid 007 — eu_ja_estava_te_procurando_mesmo
# ============================================================================

## Twine: "Eu já estava te procurando mesmo" (pid 7)
label eu_ja_estava_te_procurando_mesmo:
    # Twine: (Jussara assume uma expressão desconfiada)
    j "Como assim \"estava me procurando\"? Quem é você?"

    menu:
        "Tava brincando":
            call tava_brincando from _call_tava_brincando
        "Sou pesquisador de SP":
            call sou_pesquisador_de_sp from _call_sou_pesquisador_de_sp
        "Busco algo em sua posse":
            call busco_algo_em_sua_posse from _call_busco_algo_em_sua_posse

    return

# ============================================================================
# pid 008 — nem_pensar
# ============================================================================

## Twine: "Nem pensar" (pid 8)
label nem_pensar:
    # Twine: (Jussara assume uma expressão de espanto)
    j "Com assim? Sério mesmo?"

    menu:
        "Sério":
            call serio from _call_serio
        "Posso sim":
            call posso_sim from _call_posso_sim_nem_pensar

    return

# ============================================================================
# pid 009 — game_over_continuar
# ============================================================================

## Twine: "➞" (pid 9)
label game_over_continuar:
    call jussara_game_over_setup from _call_jussara_game_over_setup
    n "Game Over"
    n "Continuar?"

    menu:
        "Sim":
            call sim from _call_sim_game_over
        "Não":
            call nao from _call_nao_game_over

    return

# ============================================================================
# pid 010 — sim
# ============================================================================

## Twine: "Sim" (pid 10)
label sim:
    python:
        _slot_go = jussara_checkpoint_slot_to_load()

    if _slot_go is not None:
        $ renpy.load(_slot_go)
    else:
        jump sim_sem_checkpoint

    return

label sim_sem_checkpoint:
    n "Não foi encontrado nenhum checkpoint. A recomeçar em Belém..."

    jump belem

# ============================================================================
# pid 011 — nao
# ============================================================================

## Twine: "Não" (pid 11)
label nao:
    n "Obrigado por jogar!"
    return

# ============================================================================
# pid 012 — tava_brincando
# ============================================================================

## Twine: "Tava brincando" (pid 12)
label tava_brincando:
    # Twine: (Jussara assume uma expressão boba)
    j "Hmm... engraçadinho. Enfim, pode me conceder algumas respostas então?"

    menu:
        "Posso sim":
            call posso_sim from _call_posso_sim_1
        "Nem pensar":
            call nem_pensar from _call_nem_pensar_1
        "O artefato primeiro":
            call o_artefato_primeiro from _call_o_artefato_primeiro

    return

# ============================================================================
# pid 013 — sou_pesquisador_de_sp
# ============================================================================

## Twine: "Sou pesquisador de SP" (pid 13)
label sou_pesquisador_de_sp:
    j "Um pesquisador que estava me procurando? Para que exatamente?"

    menu:
        "Busco algo em sua posse":
            call busco_algo_em_sua_posse from _call_busco_algo_em_sua_posse_1
        "Ajudar na sua pesquisa":
            call ajudar_na_sua_pesquisa from _call_ajudar_na_sua_pesquisa

    return

# ============================================================================
# pid 014 — busco_algo_em_sua_posse
# ============================================================================

## Twine: "Busco algo em sua posse" (pid 14)
label busco_algo_em_sua_posse:
    j "Não sei se eu tô entendendo direito. Bom, acho que tu não podes me ajudar com a pesquisa então, né?"

    menu:
        "Posso sim":
            call posso_sim from _call_posso_sim_2
        "Nem pensar":
            call nem_pensar from _call_nem_pensar_2
        "O artefato primeiro":
            call o_artefato_primeiro from _call_o_artefato_primeiro_1

    return

# ============================================================================
# pid 015 — sou_contra
# ============================================================================

## Twine: "Sou contra" (pid 15)
label sou_contra:
    # Twine: (Jussara assume uma expressão contente)
    j "Ah, como é bom ouvir isso de um forasteiro! Sabe, esse decreto está pondo em risco todo o sistema hídrico do Pará..."

    call prossiga from _call_prossiga

    return

# ============================================================================
# pid 016 — sou_a_favor
# ============================================================================

## Twine: "Sou a favor" (pid 16)
label sou_a_favor:
    # Twine: (Jussara assume uma expressão de espanto)
    n "Você tá brincando?? Você sabe o impacto que esse decreto causará para mais de 14 povos originários e para toda a população da região norte?"

    menu:
        "Sei, não me importo":
            call sei_nao_me_importo from _call_sei_nao_me_importo
        "Conte-me mais":
            call conte_me_mais from _call_conte_me_mais

    return

# ============================================================================
# pid 017 — decreto_12_600
# ============================================================================

## Twine: "Decreto 12.600?" (pid 17)
label decreto_12_600:
    j "Sim, todo esse movimento que tu estás vendo aqui é em torno disso. E não somente aqui, há ocupações de povos indígenas em vários locais do estado, além de bloqueio de vias e manifestações nas ruas."

    menu:
        "Conte-me mais":
            call conte_me_mais from _call_conte_me_mais_1

    return

# ============================================================================
# pid 018 — sei_nao_me_importo
# ============================================================================

## Twine: "Sei, não me importo" (pid 18)
label sei_nao_me_importo:
    # Twine: (Jussara assume uma expressão irritada)
    n "Você não pode estar falando sério!!"

    menu:
        "Estou sim":
            call estou_sim from _call_estou_sim
        "Claro que não, só zuando":
            call claro_que_nao_so_zuando from _call_claro_que_nao_so_zuando

    return

# ============================================================================
# pid 019 — conte_me_mais
# ============================================================================

## Twine: "Conte-me mais" (pid 19)
label conte_me_mais:
    j "Esse decreto visa a concessão do Rio Tapajós e mais outros dois rios daqui do Pará, o que, na prática, acaba sendo a privatização desses rios."

    menu:
        "E qual o problema?":
            call e_qual_o_problema from _call_e_qual_o_problema
        "Meu Deus, que triste!":
            call meu_deus_que_triste from _call_meu_deus_que_triste
        "Prossiga":
            call prossiga from _call_prossiga_1

    return

# ============================================================================
# pid 020 — ajudar_na_sua_pesquisa
# ============================================================================

## Twine: "Ajudar na sua pesquisa" (pid 20)
label ajudar_na_sua_pesquisa:
    j "Ah sim! Égua, que bom que tu já estavas disposto a ajudar no projeto, fico feliz com isso. Então, vamos lá, podes responder as perguntas agora?"

    menu:
        "Posso sim":
            call posso_sim from _call_posso_sim_3
        "O artefato primeiro":
            call o_artefato_primeiro from _call_o_artefato_primeiro_2
        "Nem pensar":
            call nem_pensar from _call_nem_pensar_3

    return

# ============================================================================
# pid 021 — serio
# ============================================================================

## Twine: "Sério" (pid 21)
label serio:
    # Twine: (Jussara assume uma expressão triste)
    j "Ah, tudo bem, entendo... Enfim, obrigado pela atenção! Tenha um bom dia!"

    call game_over_continuar from _call_game_over_continuar_serio

    return

# ============================================================================
# pid 022 — e_qual_o_problema
# ============================================================================

## Twine: "E qual o problema?" (pid 22)
label e_qual_o_problema:
    j "O problema? Os problemas, né?"

    menu:
        "Prossiga":
            call prossiga from _call_prossiga_2

    return

# ============================================================================
# pid 023 — meu_deus_que_triste
# ============================================================================

## Twine: "Meu Deus, que triste!" (pid 23)
label meu_deus_que_triste:
    j "Pois é, né?"

    call prossiga from _call_prossiga_3

    return

# ============================================================================
# pid 024 — prossiga
# ============================================================================

## Twine: "Prossiga" (pid 24)
label prossiga:
    j "Esse rios passam por dentro de reservas indígenas. A dragagem mata os animais e a poluição afeta toda a população da região Norte. Sem falar na intoxicação com agrotóxicos do excesso de monocultura. Florestas inteiras viraram plantações de soja, que além de tudo exalam um odor insuportável, que a população sequer consegue dormir direito com o cheiro..."

    menu:
        "Há um significado místico desse rio para esses povos?":
            call ha_um_significado_mistico from _call_ha_um_significado_mistico
        "Os índios deveriam ser incorporados à sociedade como todo mundo":
            call os_indios_deveriam_ser_incorporados from _call_os_indios_deveriam_ser_incorporados

    return

# ============================================================================
# pid 025 — estou_sim
# ============================================================================

## Twine: "Estou sim" (pid 25)
label estou_sim:
    # Twine: (Jussara assume uma postura séria)
    j "Bom, não vejo porque darmos continuidade à essa pesquisa então. Tenha um bom dia."

    call game_over_continuar from _call_game_over_continuar

    return

# ============================================================================
# pid 026 — claro_que_nao_so_zuando
# ============================================================================

## Twine: "Claro que não, só zuando" (pid 26)
label claro_que_nao_so_zuando:
    # Twine: (Jussara assume uma expressão de desconfiança)
    j "Rum... Um pouco delicado brincar com uma questão dessa gravidade."

    menu:
        "Relaxa, gata":
            call relaxa_gata from _call_relaxa_gata
        "Eu sei, desculpe":
            call eu_sei_desculpe from _call_eu_sei_desculpe

    return

# ============================================================================
# pid 027 — relaxa_gata
# ============================================================================

## Twine: "Relaxa, gata" (pid 27)
label relaxa_gata:
    # Twine: (Jussara assume uma postura séria e brava)
    j "Olha, definitivamente não deveríramos estar aqui conversando. Obrigado pela participação."

    call game_over_continuar from _call_game_over_continuar_1

    return

# ============================================================================
# pid 028 — eu_sei_desculpe
# ============================================================================

## Twine: "Eu sei, desculpe" (pid 28)
label eu_sei_desculpe:
    # Twine: (Juassara assume uma postura mais leve)
    j "Tudo bem, Mas e então, tu sabes mesmo o significado desse decreto?"

    menu:
        "Conte-me mais":
            call conte_me_mais from _call_conte_me_mais_2
        "Não me importo mesmo":
            call nao_me_importo_mesmo from _call_nao_me_importo_mesmo

    return

# ============================================================================
# pid 029 — o_artefato_primeiro
# ============================================================================

## Twine: "O artefato primeiro" (pid 29)
label o_artefato_primeiro:
    j "Artefato? Que artefato?"

    menu:
        "Preciso que me ajude a descobrir":
            call preciso_que_me_ajude_a_descobrir from _call_preciso_que_me_ajude_a_descobrir
        "Um artefato mágico que transforma a realidade":
            call um_artefato_magico_que_transforma_a_realidade from _call_um_artefato_magico_que_transforma_a_realidade

    return

# ============================================================================
# pid 030 — preciso_que_me_ajude_a_descobrir
# ============================================================================

## Twine: "Preciso que me ajude a descobrir" (pid 30)
label preciso_que_me_ajude_a_descobrir:
    # Twine: (Jusara assume uma expressão confusa)
    j "Desculpe, mas não faço ideia do que se trata. Tem certeza que sou eu?"

    menu:
        "Absoluta":
            call absoluta from _call_absoluta
        "Tava brincando":
            call tava_brincando from _call_tava_brincando_1

    return

# ============================================================================
# pid 031 — um_artefato_magico_que_transforma_a_realidade
# ============================================================================

## Twine: "Um artefato mágico que transforma a realidade" (pid 31)
label um_artefato_magico_que_transforma_a_realidade:
    # Twine: (Jussara assume uma postura séria)
    j "Olha, eu não sei que espécie de jogo é essa, onde tu falas de coisas fantasiosas enquanto eu tô aqui te perguntando coisas sérias..."

    menu:
        "Perdão":
            call perdao from _call_perdao
        "Não acho tão sério assim":
            call nao_acho_tao_serio_assim from _call_nao_acho_tao_serio_assim

    return

# ============================================================================
# pid 032 — perdao
# ============================================================================

## Twine: "Perdão" (pid 32)
label perdao:
    # Twine: (Juassara assume uma postura mais leve)
    j "Tudo bem. Mas e aí, podes responder o questionário?"

    menu:
        "Posso sim":
            call posso_sim from _call_posso_sim_4
        "Nem pensar":
            call nem_pensar from _call_nem_pensar_4

    return

# ============================================================================
# pid 033 — nao_acho_tao_serio_assim
# ============================================================================

## Twine: "Não acho tão sério assim" (pid 33)
label nao_acho_tao_serio_assim:
    # Twine: (Jussara assume uma postura séria)
    j "Bom, então acho que deveríamos encerrar por aqui. Tenha um bom dia"

    call game_over_continuar_alt from _call_game_over_continuar_alt

    return

# ============================================================================
# pid 034 — quero_ajudar
# ============================================================================

## Twine: "Quero ajudar" (pid 34)
label quero_ajudar:
    # Twine: (Jussara assume uma expressão alegre)
    j "Égua! Que bom ouvir isso de também! Temos inúmeras formas de ajudar. Você pode acompanhar os perfis das causas nas redes, já que a mídia hegemônica praticmente ignora ou diminui a causa. Por isso é importante ajudar na comunicação e combater a desinformação por aí. Você também pode fazer um pix solidário, ajudar na compra de alimetento, água e materiais para as ocupações, que contam com secretarias, com escolas, cozinha, segurança..."
    j "E então, como pretede ajudar?"

    menu:
        "Agitar nas redes":
            call agitar_nas_redes from _call_agitar_nas_redes
        "Pix solidário para ajudar nas ocupações":
            call pix_solidario_para_ajudar_nas_ocupacoes from _call_pix_solidario_para_ajudar_nas_ocupacoes
        "Ajudar a disseminar em SP, o maior hub do Brasil":
            call ajudar_a_disseminar_em_sp from _call_ajudar_a_disseminar_em_sp

    return

# ============================================================================
# pid 035 — os_indios_deveriam_ser_incorporados
# ============================================================================

## Twine: "Os índios deveriam ser incorporados à sociedade como todo mundo" (pid 35)
label os_indios_deveriam_ser_incorporados:
    # Twine: (Jussara assume uma expressão irritada)
    j "Tedoidé?? Tu não ouviste nada do que eu acabei de falar? Se não fossem os povos originários não havia talvez nem ar pra respirar direito."

    menu:
        "Você está exagerando":
            call voce_esta_exagerando from _call_voce_esta_exagerando
        "Não tinha parado pra pensar nisso":
            call nao_tinha_parado_pra_pensar_nisso from _call_nao_tinha_parado_pra_pensar_nisso

    return

# ============================================================================
# pid 036 — absoluta
# ============================================================================

## Twine: "Absoluta" (pid 36)
label absoluta:
    # Twine: (Jussara assume uma expressão de choque)
    j "Ué, nunca ouvi falar de nenhum artefato que altere a realidade, a não ser que esteja falando de substâncias. Bom, nesse caso acho que que vai conseguir te ajudar com isso são os moleques que ficam ali perto do Vadião."
    j "Bom, espero que encontre o que procura então. Até um outro dia"

    call game_over_continuar_alt from _call_game_over_continuar_alt_1

    return

# ============================================================================
# pid 037 — nao_me_importo_mesmo
# ============================================================================

## Twine: "Não me importo mesmo" (pid 37)
label nao_me_importo_mesmo:
    # Twine: (Jussara assume uma expressão irritada)
    j "Ah, é? Então faça o favor de se retirar da minha frente. Até mais..."

    call game_over_continuar from _call_game_over_continuar_2

    return

# ============================================================================
# pid 038 — voce_esta_exagerando
# ============================================================================

## Twine: "Você está exagerando" (pid 38)
label voce_esta_exagerando:
    # Twine: (Jussara assume uma postura de decepção)
    j "Bom, sinto muito que pense dessa forma, mas acho melhor então pararmos por aqui. Até"

    call game_over_continuar from _call_game_over_continuar_3

    return

# ============================================================================
# pid 039 — nao_tinha_parado_pra_pensar_nisso
# ============================================================================

## Twine: "Não tinha parado pra pensar nisso" (pid 39)
label nao_tinha_parado_pra_pensar_nisso:
    j "Os indígenas ocuparm o acesso ao aeroporto de Santarém, bloquearam vias em todo o estado, manifestaram nas ruas em vários municípios, isso não é pouca coisa."

    menu:
        "Você está pessoalmente envolvida na causa?":
            call voce_esta_pessoalmente_envolvida_na_causa from _call_voce_esta_pessoalmente_envolvida_na_causa
        "Esse povo não tem o que fazer?":
            call esse_povo_nao_tem_o_que_fazer from _call_esse_povo_nao_tem_o_que_fazer

    return

# ============================================================================
# pid 040 — agitar_nas_redes
# ============================================================================

## Twine: "Agitar nas redes" (pid 40)
label agitar_nas_redes:
    j "Ah,que legal! Isso aí, obrigado pela sua participação e engajamento! Espero encontrar mais pessoas como tu por aqui."

    menu:
        "Não foi por nada!":
            call nao_foi_por_nada from _call_nao_foi_por_nada
        "Na verdade, agora queria pedir sua ajuda com outra coisa":
            call na_verdade_agora_queria_pedir_sua_ajuda from _call_na_verdade_agora_queria_pedir_sua_ajuda

    return

# ============================================================================
# pid 041 — ajudar_a_disseminar_em_sp
# ============================================================================

## Twine: "Ajudar a disseminar em SP, o maior hub do Brasil" (pid 41)
label ajudar_a_disseminar_em_sp:
    j "Sério? Isso seria incrível!"

    menu:
        "Não foi por nada!":
            call nao_foi_por_nada from _call_nao_foi_por_nada_1
        "Na verdade, agora queria pedir sua ajuda com outra coisa":
            call na_verdade_agora_queria_pedir_sua_ajuda from _call_na_verdade_agora_queria_pedir_sua_ajuda_1
        "Você está pessoalmente envolvida na causa?":
            call voce_esta_pessoalmente_envolvida_na_causa from _call_voce_esta_pessoalmente_envolvida_na_causa_1

    return

# ============================================================================
# pid 042 — pix_solidario_para_ajudar_nas_ocupacoes
# ============================================================================

## Twine: "Pix solidário para ajudar nas ocupações" (pid 42)
label pix_solidario_para_ajudar_nas_ocupacoes:
    j "Isso é muito bom! Tu vais estar ajudando uma grande quantidade de gente, em consequência ajudando a todos nós. Agradecemos de coração pela determinação!"

    menu:
        "Qual a chave pix?":
            call qual_a_chave_pix from _call_qual_a_chave_pix
        "Acho que mudei de ideia":
            call acho_que_mudei_de_ideia from _call_acho_que_mudei_de_ideia

    return

# ============================================================================
# pid 043 — game_over_continuar_alt
# ============================================================================

## Twine: "⇨" (pid 43)
label game_over_continuar_alt:
    call jussara_game_over_setup from _call_jussara_game_over_setup_1
    n "Game Over"
    n "Continuar?"

    menu:
        "Sim.":
            call sim_ponto from _call_sim_ponto
        "Não.":
            call nao_ponto from _call_nao_ponto

    return

# ============================================================================
# pid 044 — sim_ponto
# ============================================================================

## Twine: "Sim." (pid 44)
label sim_ponto:
    python:
        _slot_go = jussara_checkpoint_slot_to_load()

    if _slot_go is not None:
        $ renpy.load(_slot_go)
    else:
        jump sim_ponto_sem_checkpoint

    return

label sim_ponto_sem_checkpoint:
    n "Não foi encontrado nenhum checkpoint. A recomeçar em Belém..."

    jump belem

# ============================================================================
# pid 045 — nao_ponto
# ============================================================================

## Twine: "Não." (pid 45)
label nao_ponto:
    n "Obrigado por jogar!"
    return

# ============================================================================
# pid 046 — voce_esta_pessoalmente_envolvida_na_causa
# ============================================================================

## Twine: "Você está pessoalmente envolvida na causa?" (pid 46)
label voce_esta_pessoalmente_envolvida_na_causa:
    j "Particularmente tenho um pé de envolvimento pessoal nessa causa sim."
    j "Sou descendente direta de povos orignários. Minha avó, que já descansa em paz, costumava me contar a história de nossos ancestrais."

    menu:
        "Hmm...":
            call hmm from _call_hmm
        "Me conta a história":
            call me_conta_a_historia from _call_me_conta_a_historia_1

    return

# ============================================================================
# pid 047 — me_conta_a_historia
# ============================================================================

## Twine: "Me conta a história" (pid 47) → modulos/contar_historia_artefato.rpy
label me_conta_a_historia:
    call contar_historia_artefato from _call_contar_historia_artefato
    return

# ============================================================================
# pid 048 — hmm
# ============================================================================

## Twine: "Hmm..." (pid 48)
label hmm:
    j "Enfim, desculpa o devaneio... Vamos então para a próxima pergunta?"

    menu:
        "Me conta a história":
            call me_conta_a_historia from _call_me_conta_a_historia
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta

    return

# ============================================================================
# pid 049 — esse_povo_nao_tem_o_que_fazer
# ============================================================================

## Twine: "Esse povo não tem o que fazer?" (pid 49)
label esse_povo_nao_tem_o_que_fazer:
    j "Isso só pode ser piada...."

    menu:
        "Era mesmo. Desculpe. Prossiga":
            call era_mesmo_desculpe_prossiga from _call_era_mesmo_desculpe_prossiga
        "Nem é":
            call nem_e from _call_nem_e

    return

# ============================================================================
# pid 050 — era_mesmo_desculpe_prossiga
# ============================================================================

## Twine: "Era mesmo. Desculpe. Prossiga" (pid 50)
label era_mesmo_desculpe_prossiga:
    return

# ============================================================================
# pid 051 — nem_e
# ============================================================================

## Twine: "Nem é" (pid 51)
label nem_e:
    # Twine: (Jussara assume uma expressão séria)
    j "Certo... Obrigado pela sua participação. Tenha um bom dia."

    call game_over_continuar from _call_game_over_continuar_4

    return

# ============================================================================
# pid 052 — qual_a_chave_pix
# ============================================================================

## Twine: "Qual a chave pix?" (pid 52)
label qual_a_chave_pix:
    j "Ah, anota aí, é celular, (91) 98XX-XXXX"

    menu:
        "Feito":
            call feito from _call_feito
        "Agora preciso da sua ajuda":
            call agora_preciso_da_sua_ajuda from _call_agora_preciso_da_sua_ajuda

    return

# ============================================================================
# pid 053 — acho_que_mudei_de_ideia
# ============================================================================

## Twine: "Acho que mudei de ideia" (pid 53)
label acho_que_mudei_de_ideia:
    j "Ah, jura?"

    menu:
        "Te juro":
            call te_juro from _call_te_juro
        "Que nada, vamo sim":
            call que_nada_vamo_sim from _call_que_nada_vamo_sim

    return

# ============================================================================
# pid 054 — feito
# ============================================================================

## Twine: "Feito" (pid 54)
label feito:
    n "Muito obrigada! tu contribuíste pacas na nossa causa!"

    menu:
        "Não foi por nada!":
            call nao_foi_por_nada from _call_nao_foi_por_nada_2
        "Na verdade, agora queria pedir sua ajuda com outra coisa":
            call na_verdade_agora_queria_pedir_sua_ajuda from _call_na_verdade_agora_queria_pedir_sua_ajuda_2
        "Pacas?":
            call pacas from _call_pacas

    return

# ============================================================================
# pid 055 — agora_preciso_da_sua_ajuda
# ============================================================================

## Twine: "Agora preciso da sua ajuda" (pid 55)
label agora_preciso_da_sua_ajuda:
    call gostaria_que_me_emprestasse_um_artefato_seu from _call_gostaria_que_me_emprestasse_um_artefato_seu
    return

# ============================================================================
# pid 056 — nao_foi_por_nada
# ============================================================================

## Twine: "Não foi por nada!" (pid 56)
label nao_foi_por_nada:
    j "Muito gentil mesmo da sua parte!"
    j "Bom, a próxima pergunta seria se você teria interesse em contribuir de alguma forma na causa, mas você já se adiantou em oferecer ajuda"
    j "então"

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_1
        "Na verdade, agora queria pedir sua ajuda com outra coisa":
            call na_verdade_agora_queria_pedir_sua_ajuda from _call_na_verdade_agora_queria_pedir_sua_ajuda_3

    return

# ============================================================================
# pid 057 — na_verdade_agora_queria_pedir_sua_ajuda
# ============================================================================

## Twine: "Na verdade, agora queria pedir sua ajuda com outra coisa" (pid 57)
label na_verdade_agora_queria_pedir_sua_ajuda:
    call gostaria_que_me_emprestasse_um_artefato_seu from _call_gostaria_que_me_emprestasse_um_artefato_seu_1
    return

# ============================================================================
# pid 058 — pacas
# ============================================================================

## Twine: "Pacas?" (pid 58)
label pacas:
    j "É rsrs Desculpa, estou tão à vontade que acabo deixando escapar umas gírias do paraensês! \"Pacas\" é uma forma de falar \"pra caramba\"."

    menu:
        "Interessante!":
            call interessante from _call_interessante
        "Que gracinha você":
            call que_gracinha_voce from _call_que_gracinha_voce

    return

# ============================================================================
# pid 059 — gostaria_que_me_emprestasse_um_artefato_seu
# ============================================================================

## Twine: "Gostaria que me emprestasse um artefato seu" (pid 59)
label gostaria_que_me_emprestasse_um_artefato_seu:
    j "Artefato? Que artefato? Você sabe exatamente como ele se parece?"

    menu:
        "Sei":
            call jussara_sei from _call_jussara_sei
        "Pior que não":
            call pior_que_nao from _call_pior_que_nao

    return

# ============================================================================
# pid 060 — te_juro
# ============================================================================

## Twine: "Te juro" (pid 60)
label te_juro:
    j "Égua... tudo bem... Isso quer dizer então que pretende ajudar de outra forma? Ou simplesmente não vai mais ajudar?"

    menu:
        "Simplesmente não vou mais ajudar":
            call simplesmente_nao_vou_mais_ajudar from _call_simplesmente_nao_vou_mais_ajudar
        "Que ajudar de outra forma":
            call que_ajudar_de_outra_forma from _call_que_ajudar_de_outra_forma

    return

# ============================================================================
# pid 061 — que_nada_vamo_sim
# ============================================================================

## Twine: "Que nada, vamo sim" (pid 61)
label que_nada_vamo_sim:
    j "Ufa! Égua, pára com essas tuas gracinhas, já me deixou nervosa umas três vezes aqui rsrs"

    menu:
        "Qual a chave pix?":
            call qual_a_chave_pix from _call_qual_a_chave_pix_1
        "Gracinha é você":
            call gracinha_e_voce from _call_gracinha_e_voce

    return

# ============================================================================
# pid 062 — simplesmente_nao_vou_mais_ajudar
# ============================================================================

## Twine: "Simplesmente não vou mais ajudar" (pid 62)
label simplesmente_nao_vou_mais_ajudar:
    j "Poxa... sinto muito mesmo que não queria mais... Mas obrigado pela sua participação de qualquer maneira! Até mais!"

    call game_over_continuar_alt from _call_game_over_continuar_alt_2

    return

# ============================================================================
# pid 063 — que_ajudar_de_outra_forma
# ============================================================================

## Twine: "Que ajudar de outra forma" (pid 63)
label que_ajudar_de_outra_forma:
    j "Ah, que bom! E de que outra maneira tu pretendes ajudar?"

    menu:
        "Agitar nas redes":
            call agitar_nas_redes from _call_agitar_nas_redes_1
        "Ajudar a disseminar em SP, o maior hub do Brasil":
            call ajudar_a_disseminar_em_sp from _call_ajudar_a_disseminar_em_sp_1

    return

# ============================================================================
# pid 064 — ha_um_significado_mistico
# ============================================================================

## Twine: "Há um significado místico desse rio para esses povos?" (pid 64)
label ha_um_significado_mistico:
    j "Há um significado espiritual muito grande desse Rio para esses povos. Para os Mundurucus, por exemplo, é o berço do seu povo. A destruição desse rio seria a destruição dos seus ancestrais."
    j "Que interessante!"

    menu:
        "Isso me lembra de um certo arfefato":
            call isso_me_lembra_de_um_certo_arfefato from _call_isso_me_lembra_de_um_certo_arfefato
        "Quero ajudar":
            call quero_ajudar from _call_quero_ajudar
        "Grande coisa...":
            call grande_coisa from _call_grande_coisa

    return

# ============================================================================
# pid 065 — grande_coisa
# ============================================================================

## Twine: "Grande coisa..." (pid 65)
label grande_coisa:
    j "Sério? Tu vais desdenhar disso mesmo?"

    menu:
        "Vou":
            call vou from _call_vou
        "Desculpe!":
            call desculpe from _call_desculpe

    return

# ============================================================================
# pid 066 — vou
# ============================================================================

## Twine: "Vou" (pid 66)
label vou:
    j "Isso só pode ser piada!"

    menu:
        "Era mesmo. Desculpe. Prossiga":
            call era_mesmo_desculpe_prossiga from _call_era_mesmo_desculpe_prossiga_1
        "Nem é":
            call nem_e from _call_nem_e_1

    return

# ============================================================================
# pid 067 — e_dai
# ============================================================================

## Twine: "E daí?" (pid 67)
label e_dai:
    j "E daí? Esse decreto visa a concessão do Rio Tapajós e mais outros dois rios daqui do Pará, o que, na prática, acaba sendo a privatização desses rios."

    menu:
        "E qual o problema?":
            call e_qual_o_problema from _call_e_qual_o_problema_1
        "Meu Deus, que triste!":
            call meu_deus_que_triste from _call_meu_deus_que_triste_1
        "Prossiga":
            call prossiga from _call_prossiga_4

    return

# ============================================================================
# pid 068 — jussara_sei
# ============================================================================

## Twine: "Sei" (pid 68)
label jussara_sei:
    j "Então como ele é?"

    menu:
        "Tava mentindo":
            call tava_mentindo from _call_tava_mentindo
        "Não sei":
            call nao_sei from _call_nao_sei

    return

# ============================================================================
# pid 069 — pior_que_nao
# ============================================================================

## Twine: "Pior que não" (pid 69)
label pior_que_nao:
    j "Bom, então acho que não tenho como te ajudar, desculpa... Eu até te levaria ao meu escritório, mas estou tão oculpada com a causa que não tem sobrado tempo pra nada..."

    menu:
        "Sei como é...":
            call sei_como_e from _call_sei_como_e
        "Se vira, dá um jeito!":
            call se_vira_da_um_jeito from _call_se_vira_da_um_jeito

    return

# ============================================================================
# pid 070 — tava_mentindo
# ============================================================================

## Twine: "Tava mentindo" (pid 70)
label tava_mentindo:
    j "..."
    j "Sem graça..."
    j "Então você não sabe como ele é, né? Bom, sinto muito então não poder te ajudar com isso."

    menu:
        "1 semana depois (se optou por não perguntar se ela está pessoalmente envolvida na causa":
            call uma_semana_depois_optou_nao_perguntar from _call_uma_semana_depois_optou_nao_perguntar

    return

# ============================================================================
# pid 071 — nao_sei
# ============================================================================

## Twine: "Não sei" (pid 71)
label nao_sei:
    j "Afinal, você sabe como é ou não?"

    menu:
        "Pior que não":
            call pior_que_nao from _call_pior_que_nao_1
        "Sei sim":
            call sei_sim from _call_sei_sim

    return

# ============================================================================
# pid 072 — sei_como_e
# ============================================================================

## Twine: "Sei como é..." (pid 72)
label sei_como_e:
    j "Então tu me entendes!"

    menu:
        "Quer sair pra tomar um tacacá?":
            call quer_sair_pra_tomar_um_tacaca from _call_quer_sair_pra_tomar_um_tacaca
        "Que tal irmos para a próxima pergunta?":
            call que_tal_irmos_para_a_proxima_pergunta from _call_que_tal_irmos_para_a_proxima_pergunta

    return

# ============================================================================
# pid 073 — se_vira_da_um_jeito
# ============================================================================

## Twine: "Se vira, dá um jeito!" (pid 73)
label se_vira_da_um_jeito:
    j "Olha, não gostei nem um poco dessa maneira de falar! Passou de todos os limites!"

    menu:
        "Era zoas":
            call era_zoas from _call_era_zoas
        "Azar o seu":
            call azar_o_seu from _call_azar_o_seu

    return

# ============================================================================
# pid 074 — desculpe
# ============================================================================

## Twine: "Desculpe!" (pid 74)
label desculpe:
    j "Rum... tudo bem, vou deixar passar essa. Então vamos para a próxima pergunta: tu estarias interessado em ajudar na causa?"
    j "Sim,."

    menu:
        "Quero ajudar":
            call quero_ajudar from _call_quero_ajudar_1
        "Eu adoraria, mas estou mesmo aqui por outro motivo":
            call eu_adoraria_mas_estou_mesmo_aqui_por_outro_motivo from _call_eu_adoraria_mas_estou_mesmo_aqui_por_outro_motivo

    return

# ============================================================================
# pid 075 — interessante
# ============================================================================

## Twine: "Interessante!" (pid 75)
label interessante:
    j "Enfim, mas muito obrigada mesmo mais uma vez!"

    menu:
        "Na verdade, agora queria pedir sua ajuda com outra coisa":
            call na_verdade_agora_queria_pedir_sua_ajuda from _call_na_verdade_agora_queria_pedir_sua_ajuda_4
        "Quer sair pra tomar um tacacá?":
            call quer_sair_pra_tomar_um_tacaca from _call_quer_sair_pra_tomar_um_tacaca_1

    return

# ============================================================================
# pid 076 — que_gracinha_voce
# ============================================================================

## Twine: "Que gracinha você" (pid 76)
label que_gracinha_voce:
    j "Obrigada rsrs"

    menu:
        "De nada!":
            call de_nada from _call_de_nada
        "Quer sair pra tomar um tacacá?":
            call quer_sair_pra_tomar_um_tacaca from _call_quer_sair_pra_tomar_um_tacaca_2

    return

# ============================================================================
# pid 077 — quer_sair_pra_tomar_um_tacaca
# ============================================================================

## Twine: "Quer sair pra tomar um tacacá?" (pid 77)
label quer_sair_pra_tomar_um_tacaca:
    j "Égua! Não tava esperando por essa! Eu adoraria, mas tenho estado tão atarefada com a causa que..."
    j "Ah, quer saber, vamos sim! Onde tu queres ir?"

    menu:
        "Pode ser aqui mesmo na UFPA, no Veropesinho":
            call pode_ser_ufpa_veropesinho from _call_pode_ser_ufpa_veropesinho
        "Pode ser outro dia lá no Ver-o-peso":
            call pode_ser_ver_o_peso from _call_pode_ser_ver_o_peso

    return

# ============================================================================
# pid 078 — vamos_para_a_proxima_pergunta
# ============================================================================

## Twine: "Vamos para a próxima pergunta" (pid 78)
label vamos_para_a_proxima_pergunta:
    j "Claro, vamos lá: qual é o papel dos povos indígenas na sociedade de hoje na sua opinião?"

    menu:
        "Relevantes":
            call relevantes from _call_relevantes
        "Irrelevantes":
            call irrelevantes from _call_irrelevantes

    return

# ============================================================================
# pid 079 — eu_adoraria_mas_estou_mesmo_aqui_por_outro_motivo
# ============================================================================

## Twine: "Eu adoraria, mas estou mesmo aqui por outro motivo" (pid 79)
label eu_adoraria_mas_estou_mesmo_aqui_por_outro_motivo:
    j "E qual seria esse motivo?"

    menu:
        "Só tô passeando":
            call so_to_passeando from _call_so_to_passeando
        "Preciso que me empreste um artefato seu para a minha pesquisa":
            call preciso_que_me_empreste_um_artefato from _call_preciso_que_me_empreste_um_artefato

    return

# ============================================================================
# pid 080 — gracinha_e_voce
# ============================================================================

## Twine: "Gracinha é você" (pid 80)
label gracinha_e_voce:
    j "Ai, para com isso, engraçadinho! Anota logo essa chave pix aí:  (91) 98XX-XXXX"

    menu:
        "Feito":
            call feito from _call_feito_1
        "Agora preciso da sua ajuda":
            call agora_preciso_da_sua_ajuda from _call_agora_preciso_da_sua_ajuda_1

    return

# ============================================================================
# pid 081 — de_nada
# ============================================================================

## Twine: "De nada!" (pid 81)
label de_nada:
    j "Bom, então nos vemos por aí! Muito obrigada e tenha um excelente fim de tarde!"

    menu:
        "1 semana depois (se optou por não perguntar se ela está pessoalmente envolvida na causa":
            call uma_semana_depois_optou_nao_perguntar from _call_uma_semana_depois_optou_nao_perguntar_1

    return

# ============================================================================
# pid 082 — preciso_que_me_empreste_um_artefato
# ============================================================================

## Twine: "Preciso que me empreste um artefato seu para a minha pesquisa" (pid 82)
label preciso_que_me_empreste_um_artefato:
    j "Hmm, então você precisa da minha ajuda, né? Que tal colaborar com a causa primeiro?"

    menu:
        "É, uma mão lava a outra":
            call e_uma_mao_lava_a_outra from _call_e_uma_mao_lava_a_outra
        "Primeiro você":
            call primeiro_voce from _call_primeiro_voce

    return

# ============================================================================
# pid 083 — nao_obrigado
# ============================================================================

## Twine: "Não, obrigado" (pid 83)
label nao_obrigado:
    j "Tem certeza? É uma causa importante pra muita gente. Na verdade eu diria que é importante pra todos nós!"

    menu:
        "Vou dar uma chance":
            call jussara_vou_dar_uma_chance from _call_jussara_vou_dar_uma_chance
        "Não mesmo, sinto muito":
            call nao_mesmo_sinto_muito from _call_nao_mesmo_sinto_muito

    return

# ============================================================================
# pid 084 — so_to_passeando
# ============================================================================

## Twine: "Só tô passeando" (pid 84)
label so_to_passeando:
    j "Bom, eu entendo... Mas nada impede de ajudar de alguma forma na causa, não é mesmo?"
    j "De fato."

    menu:
        "Vou dar uma chance":
            call jussara_vou_dar_uma_chance from _call_jussara_vou_dar_uma_chance_1
        "Não quero mesmo me envolver":
            call nao_quero_mesmo_me_envolver from _call_nao_quero_mesmo_me_envolver

    return

# ============================================================================
# pid 085 — nao_mesmo_sinto_muito
# ============================================================================

## Twine: "Não mesmo, sinto muito" (pid 85)
label nao_mesmo_sinto_muito:
    j "Tudo bem, eu entendo. Não é todo mundo que consegue contribuir."
    j "Mudei de ideia."

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_2
        "Vou dar uma chance":
            call jussara_vou_dar_uma_chance from _call_jussara_vou_dar_uma_chance_2

    return

# ============================================================================
# pid 086 — historia
# ============================================================================

## Twine: "(história}" (pid 86) — atalho pós-história no Twine
label historia:
    call uma_semana_depois from _call_uma_semana_depois_historia
    return

# ============================================================================
# pid 087 — uma_semana_depois
# ============================================================================

## Twine: "1 semana depois" (pid 87)
label uma_semana_depois:
    # Twine: (aqui é o evento canônico onde o decreto é derrutado graças à sua ajuda divulgando em São Paulo)
    call jussara_1_semana_depois from _call_jussara_1_semana_depois_passagem
    return

# ============================================================================
# pid 088 — pode_ser_ufpa_veropesinho
# ============================================================================

## Twine: "Pode ser aqui mesmo na UFPA, no Veropesinho" (pid 88)
label pode_ser_ufpa_veropesinho:
    j "Ah, ótimo! Bom que é perto e dá pra passar lá antes de ir embora!"
    j "Então assim que eu acabar de arrumar minhas coisas aqui te encontro lá, beleza?"

    menu:
        "Beleza":
            call beleza from _call_beleza
        "Vamo é agora":
            call vamo_e_agora from _call_vamo_e_agora

    return

# ============================================================================
# pid 089 — pode_ser_ver_o_peso
# ============================================================================

## Twine: "Pode ser outro dia lá no Ver-o-peso" (pid 89)
label pode_ser_ver_o_peso:
    j "Combinado!"

    menu:
        "1 semana depois (se optou por não perguntar se ela está pessoalmente envolvida na causa":
            call uma_semana_depois_optou_nao_perguntar from _call_uma_semana_depois_optou_nao_perguntar_2

    return

# ============================================================================
# pid 090 — uma_semana_depois_optou_nao_perguntar
# ============================================================================

## Twine: "1 semana depois (se optou por não perguntar se ela está pessoalmente envolvida na causa" (pid 90)
label uma_semana_depois_optou_nao_perguntar:
    # Twine: (Aqui você ajudou, mas não da maneira correta - que seria divulgar em São Paulo - então você terá que continuar ajudando até tomar a escolha certa e o decreto ser derrubado)
    return

# ============================================================================
# pid 091 — sei_sim
# ============================================================================

## Twine: "Sei sim" (pid 91)
label sei_sim:
    j "Como que ele é então?"

    menu:
        "Tava mentindo":
            call tava_mentindo from _call_tava_mentindo_1

    return

# ============================================================================
# pid 092 — era_zoas
# ============================================================================

## Twine: "Era zoas" (pid 92)
label era_zoas:
    j "Sei, acho que brincadeira tem limite, sabe? Mas enfim, sinto muito mesmo por não poder ajudar com isso. Nos vemos por aí?"

    menu:
        "1 semana depois (se optou por não perguntar se ela está pessoalmente envolvida na causa":
            call uma_semana_depois_optou_nao_perguntar from _call_uma_semana_depois_optou_nao_perguntar_3

    return

# ============================================================================
# pid 093 — jussara_vou_dar_uma_chance
# ============================================================================

## Twine: "Vou dar uma chance" (pid 93)
label jussara_vou_dar_uma_chance:
    # Twine: (Jussara assume uma expressão alegre)
    j "Égua! Que bom que decidiste mudar de ideia!"
    j "Temos inúmeras formas de ajudar. Você pode acompanhar os perfis das causas nas redes, já que a mídia hegemônica praticmente ignora ou diminui a causa. Por isso é importante ajudar na comunicação e combater a desinformação por aí. Você também pode fazer um pix solidário, ajudar na compra de alimetento, água e materiais para as ocupações, que contam com secretarias, com escolas, cozinha, segurança..."
    j "E então, como pretede ajudar?"

    menu:
        "Agitar nas redes":
            call agitar_nas_redes from _call_agitar_nas_redes_2
        "Pix solidário para ajudar nas ocupações":
            call pix_solidario_para_ajudar_nas_ocupacoes from _call_pix_solidario_para_ajudar_nas_ocupacoes_1
        "Ajudar a disseminar em SP, o maior hub do Brasil":
            call ajudar_a_disseminar_em_sp from _call_ajudar_a_disseminar_em_sp_2

    return

# ============================================================================
# pid 094 — azar_o_seu
# ============================================================================

## Twine: "Azar o seu" (pid 94)
label azar_o_seu:
    j "Aff... Adeus!"

    call game_over_continuar_alt from _call_game_over_continuar_alt_3

    return

# ============================================================================
# pid 095 — e_uma_mao_lava_a_outra
# ============================================================================

## Twine: "É, uma mão lava a outra" (pid 95)
label e_uma_mao_lava_a_outra:
    j "Então você vai  ajudar na causa?!"
    j "Tá bom!"

    menu:
        "Vou dar uma chance":
            call jussara_vou_dar_uma_chance from _call_jussara_vou_dar_uma_chance_3
        "Primeiro você":
            call primeiro_voce from _call_primeiro_voce_1

    return

# ============================================================================
# pid 096 — primeiro_voce
# ============================================================================

## Twine: "Primeiro você" (pid 96)
label primeiro_voce:
    j "Okay, vou dar uma chance. Que artefato é esse, afinal?"

    menu:
        "Não sei exatamente como ele é":
            call nao_sei_exatamente_como_ele_e from _call_nao_sei_exatamente_como_ele_e
        "É um artefato mágico":
            call e_um_artefato_magico from _call_e_um_artefato_magico

    return

# ============================================================================
# pid 097 — nao_quero_mesmo_me_envolver
# ============================================================================

## Twine: "Não quero mesmo me envolver" (pid 97)
label nao_quero_mesmo_me_envolver:
    j "..."
    j "Tem certeza? É uma causa muito importante pra muita gente. Diria que pra todo mundo..."
    j "Desculpe."
    j "Okay!"
    j "Na verdade..."

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_3
        "Vou dar uma chance":
            call jussara_vou_dar_uma_chance from _call_jussara_vou_dar_uma_chance_4
        "Preciso que me empreste um artefato seu para a minha pesquisa":
            call preciso_que_me_empreste_um_artefato from _call_preciso_que_me_empreste_um_artefato_1

    return

# ============================================================================
# pid 098 — relevantes
# ============================================================================

## Twine: "Relevantes" (pid 98)
label relevantes:
    j "Que bom ouvir isso! Obrigado por responder o questionário! Tenha uma boa tarde!"

    call game_over_continuar from _call_game_over_continuar_relevantes

    return

# ============================================================================
# pid 099 — irrelevantes
# ============================================================================

## Twine: "Irrelevantes" (pid 99)
label irrelevantes:
    j "..."
    j "Entendo... Certo. Obrigado por ter participado do questionário! Tenha uma boa tarde!"

    call game_over_continuar from _call_game_over_continuar_irrelevantes

    return

# ============================================================================
# pid 100 — isso_me_lembra_de_um_certo_arfefato
# ============================================================================

## Twine: "Isso me lembra de um certo arfefato" (pid 100)
label isso_me_lembra_de_um_certo_arfefato:
    j "Que artefato?"
    j "Nada não."

    menu:
        "Um que está na sua posse":
            call um_que_esta_na_sua_posse from _call_um_que_esta_na_sua_posse
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_4

    return

# ============================================================================
# pid 101 — um_que_esta_na_sua_posse
# ============================================================================

## Twine: "Um que está na sua posse" (pid 101)
label um_que_esta_na_sua_posse:
    j "Peraí, como sabe disso?"

    menu:
        "Meu professor me disse":
            call meu_professor_me_disse from _call_meu_professor_me_disse
        "Não posso te falar":
            call nao_posso_te_falar from _call_nao_posso_te_falar

    return

# ============================================================================
# pid 102 — meu_professor_me_disse
# ============================================================================

## Twine: "Meu professor me disse" (pid 102)
label meu_professor_me_disse:
    j "E como ele sabe disso? Ele me conhece de onde? Qual é o nome dele?"

    menu:
        "Não sei responder nenhuma dessas perguntas":
            call nao_sei_responder_nenhuma_dessas_perguntas from _call_nao_sei_responder_nenhuma_dessas_perguntas
        "Você pode simplesmente dar o artefato??":
            call voce_pode_simplesmente_dar_o_artefato from _call_voce_pode_simplesmente_dar_o_artefato

    return

# ============================================================================
# pid 103 — nao_posso_te_falar
# ============================================================================

## Twine: "Não posso te falar" (pid 103)
label nao_posso_te_falar:
    j "Por que não?"

    menu:
        "Segredo de pesquisa":
            call segredo_de_pesquisa from _call_segredo_de_pesquisa
        "Na verdade, nem eu sei":
            call na_verdade_nem_eu_sei from _call_na_verdade_nem_eu_sei

    return

# ============================================================================
# pid 104 — na_verdade_nem_eu_sei
# ============================================================================

## Twine: "Na verdade, nem eu sei" (pid 104)
label na_verdade_nem_eu_sei:
    j "Bom, parece que tu sabes pouquíssimo sobre a própria pesquisa, né?"
    j "Nesse caso não tem mesmo o que eu possa fazer pra te ajudar."
    j "Tudo bem."

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_5
        "Você pode simplesmente dar o artefato??":
            call voce_pode_simplesmente_dar_o_artefato from _call_voce_pode_simplesmente_dar_o_artefato_1

    return

# ============================================================================
# pid 105 — nao_sei_responder_nenhuma_dessas_perguntas
# ============================================================================

## Twine: "Não sei responder nenhuma dessas perguntas" (pid 105)
label nao_sei_responder_nenhuma_dessas_perguntas:
    j "Esquisito, hein? Tu pelo menos sabes como é esse artefato?"

    menu:
        "Ele não me falou":
            call ele_nao_me_falou from _call_ele_nao_me_falou
        "Acho que nem ele mesmo sabe":
            call acho_que_nem_ele_mesmo_sabe from _call_acho_que_nem_ele_mesmo_sabe

    return

# ============================================================================
# pid 106 — voce_pode_simplesmente_dar_o_artefato
# ============================================================================

## Twine: "Você pode simplesmente dar o artefato??" (pid 106)
label voce_pode_simplesmente_dar_o_artefato:
    j "Não, né?! Não posso simplesmente te dar aula que nem eu nem tu sabes como é"
    j "Tudo bem"

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_6
        "Se vira, dá um jeito!":
            call se_vira_da_um_jeito from _call_se_vira_da_um_jeito_1

    return

# ============================================================================
# pid 107 — segredo_de_pesquisa
# ============================================================================

## Twine: "Segredo de pesquisa" (pid 107)
label segredo_de_pesquisa:
    j "Certo... E como seria exatamente esse artefato?"

    menu:
        "Ele não me falou":
            call ele_nao_me_falou from _call_ele_nao_me_falou_1
        "Acho que nem ele mesmo sabe":
            call acho_que_nem_ele_mesmo_sabe from _call_acho_que_nem_ele_mesmo_sabe_1

    return

# ============================================================================
# pid 108 — ele_nao_me_falou
# ============================================================================

## Twine: "Ele não me falou" (pid 108)
label ele_nao_me_falou:
    j "Que estranho! Ele te mandar assim de tão longe buscar um artefato e nem mesmo te contar como ele se parece..."

    menu:
        "Também desconfiei...":
            call tambem_desconfiei from _call_tambem_desconfiei
        "Não questiono meu trabalho":
            call nao_questiono_meu_trabalho from _call_nao_questiono_meu_trabalho

    return

# ============================================================================
# pid 109 — acho_que_nem_ele_mesmo_sabe
# ============================================================================

## Twine: "Acho que nem ele mesmo sabe" (pid 109)
label acho_que_nem_ele_mesmo_sabe:
    j "Que esquisito... Ele não sabe como ele se parece e ainda assim sabe que está comigo? Aqui em Belém do Pará?"

    menu:
        "Pois é, vai saber":
            call pois_e_vai_saber from _call_pois_e_vai_saber
        "Parece que o artefato tem propriedades mágicas":
            call parece_que_o_artefato_tem_propriedades_magicas from _call_parece_que_o_artefato_tem_propriedades_magicas

    return

# ============================================================================
# pid 110 — pois_e_vai_saber
# ============================================================================

## Twine: "Pois é, vai saber" (pid 110)
label pois_e_vai_saber:
    j "Enfim, etá ficando tarde, preciso recolher minhas coisas e ir. Mas muito obrigada mesmo por participar da minha pesquisa!"

    menu:
        "Espera":
            call espera from _call_espera
        "Tchau, tchau":
            call tchau_tchau from _call_tchau_tchau

    return

# ============================================================================
# pid 111 — parece_que_o_artefato_tem_propriedades_magicas
# ============================================================================

## Twine: "Parece que o artefato tem propriedades mágicas" (pid 111)
label parece_que_o_artefato_tem_propriedades_magicas:
    j "É mesmo? E quais seriam essas propriedades?"

    menu:
        "Ele pode alterar a realidade":
            call ele_pode_alterar_a_realidade from _call_ele_pode_alterar_a_realidade
        "Não faço ideia":
            call nao_faco_ideia from _call_nao_faco_ideia

    return

# ============================================================================
# pid 112 — tambem_desconfiei
# ============================================================================

## Twine: "Também desconfiei..." (pid 112)
label tambem_desconfiei:
    j "Hmm... Talvez seja uma boa então ficar de olho nesse seu professor. Muitas pontas soltas nessa pesquisa dele..."
    j "Enfim, etá ficando tarde, preciso recolher minhas coisas e ir. Mas muito obrigada mesmo por participar da minha pesquisa!"

    menu:
        "Espera":
            call espera from _call_espera_1
        "Tchau, tchau":
            call tchau_tchau from _call_tchau_tchau_1

    return

# ============================================================================
# pid 113 — nao_questiono_meu_trabalho
# ============================================================================

## Twine: "Não questiono meu trabalho" (pid 113)
label nao_questiono_meu_trabalho:
    j "Bom, eu sinto muito então. Eu estou extremamente ocupada com a causa."
    j "Quem sabe em um outro momento, quano talvez tu tiveres mais informação sobre esse tal artefato, eu consiga me ajudar."
    j "Já está ficando tarde, preciso recolher minhas coisas e ir. Mas muito obrigada mesmo por participar da minha pesquisa."

    menu:
        "Espera":
            call espera from _call_espera_2
        "Tchau, tchau":
            call tchau_tchau from _call_tchau_tchau_2

    return

# ============================================================================
# pid 114 — espera
# ============================================================================

## Twine: "Espera" (pid 114)
label espera:
    j "Desulpe, não consigo mesmo. Quem sabe um outro dia."
    j "Beijo!"

    call game_over_continuar_alt from _call_game_over_continuar_alt_4

    return

# ============================================================================
# pid 115 — tchau_tchau
# ============================================================================

## Twine: "Tchau, tchau" (pid 115)
label tchau_tchau:
    j "Beijo! Até mais!"

    call game_over_continuar_alt from _call_game_over_continuar_alt_5

    return

# ============================================================================
# pid 116 — nao_sei_exatamente_como_ele_e
# ============================================================================

## Twine: "Não sei exatamente como ele é" (pid 116)
label nao_sei_exatamente_como_ele_e:
    j "Então como pretende que eu te ajude??"
    n "Você tem razão."
    n "Você não entende."

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_7
        "É um artefato mágico":
            call e_um_artefato_magico from _call_e_um_artefato_magico_1

    return

# ============================================================================
# pid 117 — e_um_artefato_magico
# ============================================================================

## Twine: "É um artefato mágico" (pid 117)
label e_um_artefato_magico:
    j "Todos os artefatos carregam uma magia ancestral."

    menu:
        "De fato":
            call de_fato from _call_de_fato
        "Esse pode alterar a realidade":
            call esse_pode_alterar_a_realidade from _call_esse_pode_alterar_a_realidade

    return

# ============================================================================
# pid 118 — de_fato
# ============================================================================

## Twine: "De fato" (pid 118)
label de_fato:
    j "E como esse artefato se parece?"

    menu:
        "Não sei como ele se parece":
            call nao_sei_como_ele_se_parece from _call_nao_sei_como_ele_se_parece
        "Meu professor não disse":
            call meu_professor_nao_disse from _call_meu_professor_nao_disse

    return

# ============================================================================
# pid 119 — esse_pode_alterar_a_realidade
# ============================================================================

## Twine: "Esse pode alterar a realidade" (pid 119)
label esse_pode_alterar_a_realidade:
    j "É mesmo? De que maneira esse artefato pode alterar a realidade?"

    menu:
        "Rompendo o véu entre o mundo físico e o astral":
            call rompendo_o_veu_entre_o_mundo_fisico_e_o_astral from _call_rompendo_o_veu_entre_o_mundo_fisico_e_o_astral
        "Não faço a mínima ideia":
            call nao_faco_a_minima_ideia from _call_nao_faco_a_minima_ideia

    return

# ============================================================================
# pid 120 — nao_faco_a_minima_ideia
# ============================================================================

## Twine: "Não faço a mínima ideia" (pid 120)
label nao_faco_a_minima_ideia:
    j "Esse papo tá todo sem pé nem cabeça! Primeiro tu falas que eu tô com um artefato e tu não sabes nem como ele é. Depois fala que ele pode mudar magicamente a realidade, mas não diz como...."
    j "Enfim, tô vendo que é só enrolação, Desculpe, mas não posso mais continuar aqui. Obrigada pela participação de qualquer forma."

    call game_over_continuar from _call_game_over_continuar_5

    return

# ============================================================================
# pid 121 — rompendo_o_veu_entre_o_mundo_fisico_e_o_astral
# ============================================================================

## Twine: "Rompendo o véu entre o mundo físico e o astral" (pid 121)
label rompendo_o_veu_entre_o_mundo_fisico_e_o_astral:
    j "Impressionante! Eu amo esses assuntos místicos. Eu ficaria aqui conversando por mais tempo, mas preciso focar agora nessa pesquisa."
    j "Se tiver mais um tempinho..."
    j "agora"

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_8
        "Sem problemas, até mais!":
            call sem_problemas_ate_mais from _call_sem_problemas_ate_mais
        "Quero ajudar":
            call quero_ajudar from _call_quero_ajudar_2

    return

# ============================================================================
# pid 122 — que_tal_irmos_para_a_proxima_pergunta
# ============================================================================

## Twine: "Que tal irmos para a próxima pergunta?" (pid 122)
label que_tal_irmos_para_a_proxima_pergunta:
    j "Claro, vamos lá: qual é o papel dos povos indígenas na sociedade de hoje na sua opinião?"

    menu:
        "Relevantes":
            call relevantes from _call_relevantes_1
        "Irrelevantes":
            call irrelevantes from _call_irrelevantes_1

    return

# ============================================================================
# pid 123 — beleza
# ============================================================================

## Twine: "Beleza" (pid 123)
label beleza:
    j "Selou então! Daqui a pouco te encontro lá! Até daqui a pouco!"

    call veropesinho from _call_veropesinho

    return

# ============================================================================
# pid 124 — vamo_e_agora
# ============================================================================

## Twine: "Vamo é agora" (pid 124)
label vamo_e_agora:
    j "Calma, calma! Preciso recolher minhas coisas da pesquisa. É rapidinho. Já já te encontro lá."

    menu:
        "Veropesinho":
            call veropesinho from _call_veropesinho_1

    return

# ============================================================================
# pid 125 — veropesinho
# ============================================================================

## Twine: "Veropesinho" (pid 125)
label veropesinho:
    # Twine: (Aqui terá um breve diálogo onde o jogador pensa que estará avançando)
    return

# ============================================================================
# pid 126 — nao_sei_como_ele_se_parece
# ============================================================================

## Twine: "Não sei como ele se parece" (pid 126)
label nao_sei_como_ele_se_parece:
    j "Bom, então aí mesmo que não consigo te ajudar."
    j "Tudo bem."

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_9
        "Podemos procurar por ele?":
            call podemos_procurar_por_ele from _call_podemos_procurar_por_ele

    return

# ============================================================================
# pid 127 — meu_professor_nao_disse
# ============================================================================

## Twine: "Meu professor não disse" (pid 127)
label meu_professor_nao_disse:
    j "Então parece que ele não confia muito em ti, né? Eu não confiaria nele também..."

    menu:
        "Acho que nem ele sabe":
            call acho_que_nem_ele_sabe from _call_acho_que_nem_ele_sabe
        "Só sigo ordens":
            call so_sigo_ordens from _call_so_sigo_ordens
        "É, estranho mesmo":
            call e_estranho_mesmo from _call_e_estranho_mesmo

    return

# ============================================================================
# pid 128 — acho_que_nem_ele_sabe
# ============================================================================

## Twine: "Acho que nem ele sabe" (pid 128)
label acho_que_nem_ele_sabe:
    j "Bom, então acho que não vejo sentido em mais nada nessa conversa"
    j "então"
    j "e vou ajudar"

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_10
        "Então tchau":
            call entao_tchau from _call_entao_tchau
        "Vou dar uma chance":
            call jussara_vou_dar_uma_chance from _call_jussara_vou_dar_uma_chance_5

    return

# ============================================================================
# pid 129 — so_sigo_ordens
# ============================================================================

## Twine: "Só sigo ordens" (pid 129)
label so_sigo_ordens:
    j "Entendo seu posicionamento. Mas eu acho que um pouco de ceticismo nunca é demais..."
    j "agora"

    menu:
        "Então tchau":
            call entao_tchau from _call_entao_tchau_1
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_11
        "Quero ajudar":
            call quero_ajudar from _call_quero_ajudar_3

    return

# ============================================================================
# pid 130 — e_estranho_mesmo
# ============================================================================

## Twine: "É, estranho mesmo" (pid 130)
label e_estranho_mesmo:
    j "Pois é, eu questionaria mais ele na próxima vez que o visse... Enfim..."
    j "e vou ajudar"

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_12
        "Vou dar uma chance":
            call jussara_vou_dar_uma_chance from _call_jussara_vou_dar_uma_chance_6
        "Então tchau":
            call entao_tchau from _call_entao_tchau_2

    return

# ============================================================================
# pid 131 — podemos_procurar_por_ele
# ============================================================================

## Twine: "Podemos procurar por ele?" (pid 131)
label podemos_procurar_por_ele:
    j "Sem chance. Não tem restando o mínimo tempinho."
    j "Mudei de ideia.  e vou ajudar"

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_13
        "Vou dar uma chance":
            call jussara_vou_dar_uma_chance from _call_jussara_vou_dar_uma_chance_7
        "Então tchau":
            call entao_tchau from _call_entao_tchau_3

    return

# ============================================================================
# pid 132 — sem_problemas_ate_mais
# ============================================================================

## Twine: "Sem problemas, até mais!" (pid 132)
label sem_problemas_ate_mais:
    j "Beijo! Até!"

    call game_over_continuar from _call_game_over_continuar_6

    return

# ============================================================================
# pid 133 — ele_pode_alterar_a_realidade
# ============================================================================

## Twine: "Ele pode alterar a realidade" (pid 133)
label ele_pode_alterar_a_realidade:
    j "Impressionante! Eu amo esses assuntos místicos. Eu ficaria aqui conversando por mais tempo, mas preciso focar agora nessa pesquisa."
    j "Se tiver mais um tempinho..."

    menu:
        "Vamos para a próxima pergunta":
            call vamos_para_a_proxima_pergunta from _call_vamos_para_a_proxima_pergunta_14
        "Tudo bem, até mais!":
            call tudo_bem_ate_mais from _call_tudo_bem_ate_mais

    return

# ============================================================================
# pid 134 — nao_faco_ideia
# ============================================================================

## Twine: "Não faço ideia" (pid 134)
label nao_faco_ideia:
    j "Bom, não tá fazendo o mínimo sentido pra mim isso."

    menu:
        "Tava brincando":
            call tava_brincando from _call_tava_brincando_2
        "Tudo bem, até mais!":
            call tudo_bem_ate_mais from _call_tudo_bem_ate_mais_1

    return

# ============================================================================
# pid 135 — tudo_bem_ate_mais
# ============================================================================

## Twine: "Tudo bem, até mais!" (pid 135)
label tudo_bem_ate_mais:
    j "Beijo! Até!"

    call game_over_continuar_alt from _call_game_over_continuar_alt_6

    return

# ============================================================================
# pid 136 — entao_tchau
# ============================================================================

## Twine: "Então tchau" (pid 136)
label entao_tchau:
    j "Tá, né... Tchau, tchau!"

    call game_over_continuar from _call_game_over_continuar_7

    return
