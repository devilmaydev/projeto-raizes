# The script of the game goes in this file.
#
# Character definitions are in game/characters.rpy.
#
# Game starts here. Intro: game/story/01_introducao/introducao.rpy
# Professor: game/story/02_sala_professor/sala_professor.rpy
# Belém: game/story/03_Belem/Belém/ (belem/, jussara/, viagem_retorno/)
# Ren'Py resolves calls by label name, not file name.

label start:
    call introducao from _call_introducao
    return
