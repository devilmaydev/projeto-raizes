## == Jussara 05 — Canto da Jussara (Point n Click) ==
## Integrado com game/libs/point_and_click/point_and_click.rpy

image bg canto_jussara = im.Scale("images/Cantinho da Jussara (Sem os Assets).jpg", 1920, 1080)
image bg canto_jussara_com_assets = im.Scale("images/Cantinho da Jussara.jpg", 1920, 1080)
image pnc_quadro_idle = Transform("images/Asset 2.png", zoom=1.)
image pnc_quadro_hover = Transform("images/Asset 2.png", zoom=1.05)
image pnc_escultura_tapajonica_idle = Transform("images/Escultura Tapajônica.png", zoom=0.40)
image pnc_escultura_tapajonica_hover = Transform("images/Escultura Tapajônica.png", zoom=0.45)
image pnc_urna_artefato_idle = Transform("images/Artefato Cortado.png", zoom=1)
image pnc_urna_artefato_hover = Transform("images/Artefato Cortado.png", zoom=1.05)
image pnc_cuia_tacaca_idle = Transform("images/Cuia de Tacacá.png", zoom=0.33, rotate=20)
image pnc_cuia_tacaca_hover = Transform("images/Cuia de Tacacá.png", zoom=0.36, rotate=20)
image pnc_muiraquita_idle = Transform("images/Asset 3.png", zoom=1)
image pnc_muiraquita_hover = Transform("images/Asset 3.png", zoom=1.2)
image pnc_retrato_asset_1_idle = Transform("images/asset 1.png", zoom=0.98)
image pnc_retrato_asset_1_hover = Transform("images/asset 1.png", zoom=1.05)

## Sprites de visualização detalhada (independentes dos botões do cenário).
image pnc_det_quadro = "images/Prêmio Jussara.png"
image pnc_det_escultura = "images/Escultura Tapajônica.png"
image pnc_det_urna = "images/Urna (Artefato).png"
image pnc_det_cuia = "images/Cuia de Tacacá.png"
image pnc_det_sapo = "images/Muiraquitã.png"
image pnc_det_retrato = "images/Jussara Avó Retrato.png"

screen pnc_objeto_detalhe(img_path, zoom=1.0):
    modal True
    add Solid("#000000")
    add Transform(img_path, xalign=0.5, yalign=0.5, zoom=zoom)
    key "dismiss" action Return()

define jussara_canto_buttons = [
    # Quadro (superior esquerdo)
    (("pnc_quadro_idle", "pnc_quadro_hover"), (271, 238), "pnc_jussara_item_01_label", None),
    # Escultura Tapajônica (inferior esquerdo)
    (("pnc_escultura_tapajonica_idle", "pnc_escultura_tapajonica_hover"), (165, 645), "pnc_jussara_item_02_label", None),
    # Urna (Artefato) - prateleira superior
    (("pnc_urna_artefato_idle", "pnc_urna_artefato_hover"), (1202, 124), "pnc_jussara_item_03_label", None),
    # Cuia de Tacacá (prateleira do meio)
    (("pnc_cuia_tacaca_idle", "pnc_cuia_tacaca_hover"), (1550, 440), "pnc_jussara_item_04_label", None),
    # Asset 3 (substitui o sapo na prateleira inferior direita)
    (("pnc_muiraquita_idle", "pnc_muiraquita_hover"), (1696, 690), "pnc_jussara_item_05_label", None),
    # Asset 1 (retrato) - inferior direito
    (("pnc_retrato_asset_1_idle", "pnc_retrato_asset_1_hover"), (1419, 901), "pnc_jussara_item_06_label", None),
]


label canto_jussara_point_n_click:
    scene bg canto_jussara_com_assets with dissolve
    show jussara idle at jussara_show
    with dissolve
    
    j "Boas-vindas ao meu cantinho! Não tá no ápice da sua arrumação, mas também não tá no da bagunça."
    j "Fique à vontade para olhar em volta e procurar pelo seu objeto."

    scene bg canto_jussara

    $ pnc_flags["jussara_item_01"] = False
    $ pnc_flags["jussara_item_02"] = False
    $ pnc_flags["jussara_item_03"] = False
    $ pnc_flags["jussara_item_04"] = False
    $ pnc_flags["jussara_item_05"] = False
    $ pnc_flags["jussara_item_06"] = False
    $ current_room = "jussara_canto"
    jump pnc_loop


label pnc_jussara_item_01_label:
    scene bg canto_jussara_com_assets
    show jussara idle at jussara_show
    show expression Transform("pnc_det_quadro", xalign=0.78, yalign=0.5, zoom=0.85) as detalhe_objeto
    j "Ah, isso? É o prêmio que eu recebi pela minha tese de conclusão de curso. Eu não imaginava que fosse ser premiada logo na primeira defesa, parece que eu estava destinada à minha vocação."
    j "É esse o artefato que você procura?"

    menu:
        "Sim":
            j "Não, esse não é o artefato que você procura."
        "Não":
            pass
    hide detalhe_objeto
    jump pnc_jussara_pos_clique


label pnc_jussara_item_02_label:
    scene bg canto_jussara_com_assets
    show jussara idle at jussara_show
    show expression Transform("pnc_det_escultura", xalign=0.78, yalign=0.5, zoom=1.05) as detalhe_objeto
    j "Ah, isso? É uma escultura de cerâmica tapajônica. Eu sei que eu te contei que a vovó fazia cerâmica e era originária do Rio Tapajós. Mas ela saiu de lá jovem demais e não teve tempo de aprender as cerâmicas Tapajônicas."
    j "No Marajó, onde ela se criou, criou outros tipos de cerâmicas. Ou seja, essa escultura está com a nossa família bem antes dela!"
    j "É esse o artefato que você procura?"

    menu:
        "Sim":
            j "Não, esse não é o artefato que você procura."
        "Não":
            pass
    hide detalhe_objeto
    jump pnc_jussara_pos_clique


label pnc_jussara_item_03_label:
    scene bg canto_jussara_com_assets
    show jussara idle at jussara_show
    show expression Transform("pnc_det_urna", xalign=0.78, yalign=0.5, zoom=0.9) as detalhe_objeto
    j "Ah, isso? Esta é a urna funerária que guarda as cinzas da minha avó Jussara. Como eu tinha falado, este é um dos artefatos mais antigos que temos, se não o mais."
    j "Ter essa urna aqui no meu cantinho, junto de todas minhas outras coisas, é como se a vovó estivesse aqui comigo."
    j "Não é esse o artefato que você procura, é?"
    hide detalhe_objeto

    menu:
        "Olha... infelizmente":
            jump pnc_jussara_urna_infelizmente
        "Sim e você vai me deixar levar":
            jump pnc_jussara_urna_forcar
        "Não":
            j "Tudo bem, continue olhando."
            jump pnc_jussara_pos_clique


label pnc_jussara_item_04_label:
    scene bg canto_jussara_com_assets
    show jussara idle at jussara_show
    show expression Transform("pnc_det_cuia", xalign=0.78, yalign=0.5, zoom=0.9) as detalhe_objeto
    j "Ah, isso? É uma cuia de Tacacá, bebida típica famosíssima aqui da Amazônia. Feita de caldo de Tucupí, goma de mandioca, jambu e camarão, uma iguaria paraense e também uma especiaria muito ancestral."
    j "É esse o artefato que você procura?"

    menu:
        "Sim":
            j "Não, esse não é o artefato que você procura."
        "Não":
            pass
    hide detalhe_objeto
    jump pnc_jussara_pos_clique


label pnc_jussara_item_05_label:
    scene bg canto_jussara_com_assets
    show jussara idle at jussara_show
    show expression Transform("pnc_det_sapo", xalign=0.78, yalign=0.5, zoom=0.75) as detalhe_objeto
    j "Ah, isso? Isso é um Muiraquitã. É um artefato talhado em amazonita, uma linda pedra verde amazônica. Parece que assim como eu e meus ancestrais, ele também tem origem nos povos do Tapajós, e também dos Konduris."
    j "Aqui em Belém temos a tradição de dar de presente como amuleto da sorte. Nunca se deve comprar um Muiraquitã."
    j "É esse o artefato que você procura?"

    menu:
        "Sim":
            j "Não, esse não é o artefato que você procura."
        "Não":
            pass
    hide detalhe_objeto
    jump pnc_jussara_pos_clique


label pnc_jussara_item_06_label:
    scene bg canto_jussara_com_assets
    show jussara idle at jussara_show
    show expression Transform("pnc_det_retrato", xalign=0.78, yalign=0.5, zoom=0.62) as detalhe_objeto
    j "Ah, isso? É um retrato da vovó Jussara quando jovem. Ela era linda, né? É, eu sei, ela era igualzinha a mim."
    j "É esse o artefato que você procura?"

    menu:
        "Sim":
            j "Não, esse não é o artefato que você procura."
        "Não":
            pass
    hide detalhe_objeto
    jump pnc_jussara_pos_clique


label pnc_jussara_urna_infelizmente:
    show expression Transform("pnc_det_urna", xalign=0.78, yalign=0.5, zoom=0.9) as detalhe_objeto
    j "..."
    j "Como pode? O universo e suas sincronicidades... Como pode ser o mesmo objeto que esteve por gerações conosco há anos, ser usado para guardar as cinzas da minha avozinha e, ainda, ser tão importante numa pesquisa tão misteriosa?"
    j "Você sabe mesmo o que será feito com ela?"

    menu:
        "Não sei, mas fique tranquila que será para estudos e voltará a salvo":
            j "Bom, como uma estudante e pesquisadora, por mais envolvida que eu esteja com o objeto, não posso empacar o avanço de uma causa nobre. Quero que me prometa que voltará são e salvo."
            n "[[Missão cumprida]]"
            hide detalhe_objeto
            return

        "Eu realmente não sei o que será feito":
            j "Eu tenho temor de simplesmente entregar assim um objeto tão importante pra um futuro tão incerto. Eu tenho sempre muita gratidão por quem me ajuda, mas ainda mais pelos meus ancestrais e todo o seu legado..."
            n "[[Missão falhou]]"
            hide detalhe_objeto
            return

        "Tenho certeza que será usada pro bem":
            j "Que bom! Se você acredita tanto no projeto, então quem sou eu pra te impedir? Justo eu, alguém tão engajada, de um povo igualmente engajado."
            j "Então faça, faça por nós. Faça pelo meu povo, que também é seu povo, povo de todo brasileiro."
            n "[[Missão cumprida]]"
            hide detalhe_objeto
            return


label pnc_jussara_urna_forcar:
    show expression Transform("pnc_det_urna", xalign=0.78, yalign=0.5, zoom=0.9) as detalhe_objeto
    j "Calma aí! Como pode ser tão insensível depois de ouvir toda a minha história e se envolver diretamente com a causa? Não posso te deixar levar assim um objeto tão importante pra mim, praticamente à força!"
    j "Sou muito grata mesmo por você ter me ajudado, mas isso não te dá o direito de me impor algo tão delicado assim. Além disso, não foi só você o único que me ajudou."
    j "Dá até pra dizer que sua ajuda foi tão grande quanto o de uma formiga."
    j "Não leve a mal, cada formiga tem um papel importante, mas o coletivo que prevalece no final."
    j "E quando se trata de coletivo, acho que o homem \"civilizado\" (entre muitas aspas) tem muita dificuldade em assimilar o seu papel diante dele."
    j "Mais uma vez obrigada! Mas você não vai falar comigo assim. Adeus!"
    hide detalhe_objeto
    return


label pnc_jussara_pos_clique:
    scene bg canto_jussara
    jump pnc_loop
