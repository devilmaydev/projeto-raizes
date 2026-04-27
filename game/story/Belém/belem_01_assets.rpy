## == Belém — recursos de cena (fundos, sprite Jussara, transform) ==

image bg aeroporto = im.Scale("images/Aeroporto.jpg", 1920, 1080)
image bg universidade_ufpa = im.Scale("images/Universidade Federal do Pará.jpg", 1920, 1080)
image bg mirante_rio = im.Scale("images/Mirante do Rio.jpg", 1920, 1080)

image jussara idle = "images/Jussara Idle.png"

## Sprite: ajuste zoom / yoffset aqui ou com um transform com nome próprio noutro ficheiro.
transform jussara_show:
    subpixel True
    xalign 0.7
    ypos 1.0
    yanchor 1.0
    zoom 1
    yoffset 870
