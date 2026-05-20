## == Mapa do roteiro em Belém (só comentário; não altera o jogo) ==
##
## belem/
##   entrada.rpy              →  belem_aeroporto / belem_universidade
##   assets.rpy               →  fundos, jussara idle, jussara_show
##   aeroporto.rpy              →  cena_belem_aeroporto → passagens belem + continuar_aeroporto
##   universidade_mirante.rpy   →  jussara_arco_mirante
##
## jussara/
##   jussara_core.rpy           →  jussara_arco_mirante, jussara_fim_mirante
##   jussara_twine.rpy          →  todo o Twine Jussara (labels por pid no ficheiro)
##   game/checkpoints.rpy       →  $ jussara_checkpoint() nos marcos; game over → autosave
##   modulos/
##     contar_historia_artefato.rpy  →  label contar_historia_artefato
##     uma_semana_depois.rpy         →  label jussara_1_semana_depois
##     canto_point_n_click.rpy       →  label canto_jussara_point_n_click
##
## viagem_retorno/  — retorno Belém → SP (após canto / 1 semana)
##
## Ordem narrativa (importante):
##   1. Alfândega — retorno com o artefato na mochila (qualquer um: urna, cuia, etc.)
##      escolha_artefato_mochila.rpy → alfandega_belem.rpy → alfandega_guarulhos.rpy
##   2. Laboratório — hub após alfândega: lab_posicionar_artefato_retorno.rpy
##      • artefato certo (urna)  → finais_twine.rpy («Finais», em processo)
##      • artefato errado        → artefato_errado_twine.rpy («Voltando com o artefato errado»)
##   3. Recuperação — nova passagem por alfândega se perdeu/errou o objeto
##      alfandega_belem_recuperacao.rpy
##
##   artefato_viagem_state.rpy       →  artefato_id, mochila_com_artefato, flags
##   finais_twine.rpy                →  Twine «Finais» (pós-alfândega, objeto certo)
##   artefato_errado_twine.rpy       →  Twine «Voltando com o artefato errado» (pós-alfândega, objeto errado)
##   batalha_jussara_professor.rpy   →  Twine menor «Batalha Jussara × Professor» (fora de Finais)
##   lab_posicionar_artefato_retorno.rpy
