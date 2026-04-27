## == Belém — portão, campus, Mirante; primeiro menu Jussara ==
## Chamado a partir de belem_00_entrada_aeroporto_universidade.rpy (label cena_belem_universidade_mirante)

label cena_belem_universidade_mirante:
    scene bg universidade_ufpa
    with dissolve

    n "Você desembarca no Portão III, o mais próximo do Rio Guamá. Dá graças a Deus pelo campus ser longe do centro urbano. Ao contrário: é às margens de um rio belíssimo, cheio de vida e natureza."

    n "Você logo se mistura à fila inevitável que se forma na entrada, para então se dissipar após o portão e, em seguida, se reorganizar novamente nas calçadas e pontes de acesso que sobrepõem os riachos que cortam a universidade."

    scene bg mirante_rio
    with dissolve

    n "Você nota um movimento de gente se formando ao chegar perto do enorme prédio que concentra os cursos de humanas e licenciaturas, o Mirante do Rio."

    show jussara idle at jussara_show
    with dissolve

    j "Olá! Tudo bem? Prazer, eu me chamo Jussara, sou estudante de pós-graduação do curso de jornalismo aqui na UFPA."

    j "Meu grupo e eu estamos realizando um projeto de pesquisa e gostaria de te fazer algumas perguntas, pode ser?"

    menu:
        "Pode Sim":
            call pode_sim from _call_pode_sim
        "Nem Pensar":
            call nem_pensar from _call_nem_pensar
        "Eu já estava te procurando mesmo":
            call te_procurando from _call_te_procurando

    hide jussara
    with dissolve

    return
