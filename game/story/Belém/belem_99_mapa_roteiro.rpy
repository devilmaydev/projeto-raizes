## == Mapa do roteiro em Belém (só comentário; não altera o jogo) ==
## belem_00_entrada_aeroporto_universidade  →  labels belem_aeroporto / belem_universidade
## belem_01_assets                 →  fundos, jussara idle, jussara_show
## belem_02_aeroporto              →  cena_belem_aeroporto
## belem_03_universidade_mirante   →  cena_belem_universidade_mirante
## jussara_01_convite_e_primeiros_menus → convite, “Nem pensar”, te procurando, tava brincando, jussara_pergunta_opiniao_decreto
## jussara_02_decreto_conversa     →  sou contra / a favor, decreto, prossiga, incorporar, etc.
## jussara_03_ajudar_mirante       →  quero ajudar, pix, SP, envolvida_na_causa
## jussara_04_contar_historia_artefato  →  label contar_historia_artefato
## jussara_05_1_semana_depois      →  label jussara_1_semana_depois
## jussara_05_canto_point_n_click  →  label canto_jussara_point_n_click (estrutura point n click)
##
## DRY: jussara_pergunta_opiniao_decreto (pode_sim / nao_zuando / posso_sim)
##      jussara_fala_impacto_rios (sou_contra + prossiga)
