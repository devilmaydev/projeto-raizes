# The script of the game goes in this file.
#
# Character definitions are in game/characters.rpy.
#
# Game starts here. Intro is in game/story/introducao.rpy.
# Belem entry labels are in:
#   game/story/Belem/belem_00_entrada_aeroporto_universidade.rpy
# Scene content stays in belem_02, belem_03, and jussara_*.rpy.
# Ren'Py resolves calls by label name, not file name.

label start:
    call introducao from _call_introducao
    return
