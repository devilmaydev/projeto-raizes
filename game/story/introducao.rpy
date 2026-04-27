## Introdução visual baseada no storyboard.
## A voz é do professor, mas sem identificação para o jogador.

## Período = largura após crop + pequeno respiro entre blocos.
default faixa1_periodo = 1332
default faixa2_periodo = 1296

image intro_fundo = im.Scale("images/Fundo_Introducao.jpeg", 1920, 1080)

init python:
    import math
    intro_faixa_zoom = 1.8
    ## Crop horizontal: tira a margem transparente dos 800px. Se repetir o bloco inteiro,
    ## a junção somava margem+margem = “espaço gigante” entre um ciclo e outro.
    cro1 = im.Crop( "images/simbolos 1.png", (36, 0, 720, 132) )
    cro2 = im.Crop( "images/simbolos 2.png", (53, 0, 700, 154) )
    s1w = int(720 * intro_faixa_zoom)
    s2w = int(700 * intro_faixa_zoom)
    s1h = int(132 * intro_faixa_zoom)
    s2h = int(154 * intro_faixa_zoom)
    s1 = im.Scale( cro1, s1w, s1h )
    s2 = im.Scale( cro2, s2w, s2h )
    ## Espaço entre o fim de um bloco e o início do próximo.
    gap = int(24 * intro_faixa_zoom)
    store.faixa1_periodo = s1w + gap
    store.faixa2_periodo = s2w + gap

    def _repetir_copias_coladas(im0, w, h, periodo):
        n = int(
            math.ceil(
                (config.screen_width + periodo) / float(periodo)
            )
        )
        total = (n - 1) * periodo + w
        partes = []
        for i in range(n):
            partes.append( (i * periodo, 0) )
            partes.append( im0 )
        return im.Composite( (total, h), *partes )

    renpy.image(
        "intro_simbolos_1_tiled",
        _repetir_copias_coladas( s1, s1w, s1h, store.faixa1_periodo),
    )
    renpy.image(
        "intro_simbolos_2_tiled",
        _repetir_copias_coladas( s2, s2w, s2h, store.faixa2_periodo),
    )
image intro_rupestres = "images/rupestres.png"
image intro_hieroglifos = "images/Hieróglifos wide.png"
image intro_deuses = "images/desus egípcios.png"
image intro_thoth = "images/Thoth 2.png"
image intro_adinkras = im.Scale(
    im.Crop("images/adinrkas.png", (0, 0, 1321, 935)),
    1920,
    1080,
)
image intro_horus = "images/olho de horus.png"
image intro_cuia = "images/CUIA.png"
image intro_horus_full = "images/olho de horus.png"

## Faixa 1: textura desliza; xanchor 0.0 = borda alinhada (reduz corte visível na costura).
transform faixa_direita_esquerda:
    subpixel True
    yalign 0
    xalign 0.0
    xanchor 0.0
    xoffset 0
    linear 10.0 xoffset -faixa1_periodo
    repeat

## Faixa 2: sentido oposto. yalign alto demais = colide com a textbox (gui.textbox embaixo).
transform faixa_esquerda_direita:
    subpixel True
    yalign 0.7
    xalign 0.0
    xanchor 0.0
    xoffset -faixa2_periodo
    linear 10.0 xoffset 0
    repeat

transform horus_centro:
    xalign 0.5
    yalign 0.35
    zoom 0.6

transform rupestres_centro:
    xalign 0.5
    yalign 0.3
    zoom 2

transform hieroglifos_centro:
    xalign 0.5
    yalign 0.3
    zoom 2

transform deuses_centro:
    xalign 0.5
    yalign 0.3
    zoom 1

transform thoth_centro:
    xalign 0.40
    yalign 1.0
    yanchor 1.0
    yoffset 320
    zoom 0.72

label introducao:
    if renpy.loadable("audio/Raízes INTRO.mp3.mpeg"):
        play music "audio/Raízes INTRO.mp3.mpeg" fadein 1.0

    scene intro_fundo with fade

    # Abertura com olho de Hórus e duas fileiras em sentidos opostos.
    show intro_horus_full at horus_centro
    show intro_simbolos_1_tiled at faixa_direita_esquerda
    show intro_simbolos_2_tiled at faixa_esquerda_direita
    "Símbolos, por milénios têm guiado toda a humanidade."

    scene intro_fundo with dissolve
    show intro_rupestres at rupestres_centro
    "Desde os primórdios dos tempos, homens recém-evoluídos marcavam paredes de cavernas, usando matérias-primas facilmente encontradas na natureza."

    scene intro_fundo
    show intro_rupestres at rupestres_centro
    "uvas tintas, barro, folhas verdes e até sangue. Pintavam registros do seu cotidiano primitivo, como a caça, dança ou elementos da natureza."

    scene intro_fundo with dissolve
    show intro_hieroglifos at hieroglifos_centro
    "Ainda em épocas muito remotas, no que é considerado o berço da civilização, na África, mais precisamente no antigo Egito, os símbolos ganharam ainda mais notoriedade e ultilidade na sociedade."

    scene intro_fundo
    show intro_hieroglifos at hieroglifos_centro
    "Muito menos figurativos que as pinturas rupestres, os símbolos egípcios tomaram uma direção mais simbólica e alegórica."

    scene intro_fundo with dissolve
    show intro_deuses at deuses_centro
    "Suas divindades são representadas por amálgamas de homens e animais. Cada animal cuidadosamente selecionado para representar uma virtude humana."

    scene intro_fundo with dissolve
    show intro_thoth at thoth_centro
    "Tot, deus mensageiro entre os céus e a terra, é um homem com cabeça de Ibis - pássaro de bico fino. Representa a inteligência. Sua pinçada simboliza a tomada precisa de uma escolha..."

    scene black with dissolve
    "Os símbolos... Eles nunca desapareceram. Nos acaompanham até hoje, com diferentes variações em todo o planeta, com diferentes roupagens"
    "de diferentes culturas..."

    scene intro_adinkras with dissolve
    "E não precisa ir muito longe para se deparar com a mais diversa variedade de ideogramas, arabescos, padrões e grafismos."
    "Aqui mesmo, em nosso território, é possível achar resquícios mais do que sutis dessa herança ancestral."

    stop music fadeout 1.0
    call sala_professor from _call_sala_professor
    return
