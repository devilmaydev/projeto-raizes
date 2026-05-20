## Módulo — História (avó, Cotijuba). Chamada por passagem me_conta_a_historia.
##
## Artes: `imagem_cima` = base (CUIA ou Pinheiros, etc.); `imagem_sobre` = opcional, por cima (ex. Fogo
## na faixa preta da cuia). Ajusta `zoom_sobre` e `yal_sobre` para alinhar a fogueira na cuia.
##
define JCU_ARTE_CUIA = "images/CUIA.png"
define JCU_ARTE_FOGUEIRA = "images/Fogo.png"
define JCU_ARTE_TRES_FORMAS = "images/Pinheiros.png"

init python:
    def jussara_resolved_top_art(path):
        if path and renpy.loadable(path):
            return path
        if renpy.loadable(JCU_ARTE_CUIA):
            return JCU_ARTE_CUIA
        return path

screen jussara_cuia_card(
        texto,
        imagem_cima=JCU_ARTE_CUIA,
        imagem_sobre=None,
        zoom_cima=0.9,
        yal_cima=0.12,
        yoff_cima=0,
        zoom_sobre=0.28,
        yal_sobre=0.198,
        escurece_area_texto=0,
    ):
    modal True
    # Dismiss: após o texto lento terminar, fecha o `call screen` (segundo toque, como o say padrão).
    key "dismiss" action Return()

    $ _jcu_top = jussara_resolved_top_art(imagem_cima)
    add Transform(_jcu_top, xalign=0.5, yalign=yal_cima, yoffset=yoff_cima, zoom=zoom_cima)
    if imagem_sobre is not None and renpy.loadable(imagem_sobre):
        add Transform(imagem_sobre, xalign=0.5, yalign=yal_sobre, zoom=zoom_sobre)
    add Transform("images/Dialogue_Box.png", xalign=0.5, yalign=0.80, zoom=1.0)
    ## Atrás do texto: bloqueia a arte de cima no “buraco” transparente do Dialogue_Box
    if escurece_area_texto > 0:
        add Transform(Solid("#000", xsize=1200, ysize=270), xalign=0.5, yalign=0.77, alpha=escurece_area_texto)

    frame:
        background None
        xalign 0.5
        yalign 0.77
        xsize 1240
        ysize 290
        xpadding 28
        ypadding 26

        text texto:
            id "jussara_cuia_what"
            xalign 0.0
            yalign 0.0
            xmaximum 1180
            text_align 0.0
            font "fonts/Oswald-Regular.ttf"
            color "#f2ad45"
            size 40
            line_spacing 4
            ## 1.º clique/Enter: conclui o letra a letra; 2.º: fecha o card (via key dismiss).
            slow True
            slow_cps True
            slow_abortable True


label contar_historia_artefato:
    scene black
    with dissolve

    call screen jussara_cuia_card(
        "Me lembro quando era pequena e ia para Cotijuba. Ficava eu e meus primos na praia do \"Vai Quem Quer\". Eu sei, nome engraçado. Enfim, ficávamos numa roda em volta de uma fogueira e, no centro dela, sempre de frente pro pôr-do-sol, ficava minha avó, Jussara, assim como eu."
    )

    call screen jussara_cuia_card(
        "Sempre com um sorriso leve no rosto, suas bochechas brilhavam refletindo a luz pastel do céu rosê do fim da tarde. A gente amava ouvir as suas histórias!"
    )

    call screen jussara_cuia_card(
        "E lembro até hoje da sensação: normalmente viajávamos pra lá final de semestre, tudo o que eu e meus primos queríamos era esquecer toda a matéria da escola, mergulhar numa água gelada de igarapé (pra refrescar o carolão de Belém) e, principalmente, passar esse tempo gostoso na casa da nossa avó Jussara.",
        imagem_cima=JCU_ARTE_CUIA,
        imagem_sobre=JCU_ARTE_FOGUEIRA,
    )

    call screen jussara_cuia_card(
        "Ela que sempre nos mimava, mas também disciplinava. Nos enchia daquelas comidas gostosas de casa de vó, brincava com a gente (desde que não exigisse muito do seu físico), ensinava a gente a pintar os padrões Mundurucus, Marajoaras e de outros povos. Era mágico, a gente reproduzia eles em tudo quanto é lugar.",
        imagem_cima=JCU_ARTE_FOGUEIRA,
        zoom_cima=0.40,
        yal_cima=0.11,
        yoff_cima=-8,
        escurece_area_texto=0.88,
    )

    call screen jussara_cuia_card(
        "Mas os momentos que ficaram mesmo mais marcados no meu coração eram nas rodas de histórias que a vovó costumava contar no pôr-do-sol na praia do \"Vai Quem Quer\". Me lembro de várias, mas a que realmente me marcou, foi sua própria. Da forma que eu me lembro, era mais ou menos assim:",
        imagem_cima=JCU_ARTE_FOGUEIRA,
        zoom_cima=0.40,
        yal_cima=0.11,
        yoff_cima=-8,
        escurece_area_texto=0.88,
    )

    call screen jussara_cuia_card(
        "Por centenas de anos, em uma terra sem fronteiras, mas com rios, florestas densas, a maior variedade de animais e plantas do planeta e um clima bom para colheitas férteis o ano inteiro, reinavam povos guerreiros e pacíficos.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Guerreiros porque sempre lutaram pela sua sobrevivência, em suas diversas formas - caçando, zelando, resistindo, produzindo artefatos, realizando ritos e, claro, contando histórias - e pacíficos, pois nunca por vontade própria colocavam em risco seus pares e a própria natureza.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Tinham uma vida simples e organizada. Cada um nascia sabendo do seu dever com sua comunidade e levava isso consigo durante toda a vida.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Os Caciques chefiavam as tribos, geralmente levavam consigo essa alcunha até mesmo depois de se tornarem anciãos, sendo praticamente bibliotecas vivas ambulantes e, quando partiam, partia também boa parte do conhecimento de todo seu povo.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Os Pagés, responsáveis pela \"pagelança\", ou aquilo que vinha do astral, ou metafísico, além de dominarem forças físicas da natureza e conhecerem profundamente ervas e especiarias e como usá-las na comunidade. Se um Pagé se fosse, um povo inteiro perdia parte do seu conhecimento místico...",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Mas, por sorte, os males da vida nunca foram tão rápidos a ponto de levar mais dos povos do que eles poderiam construir de volta, preservando assim seus anciãos vivos em suas memórias e mantendo sempre presente sua ancestralidade.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Durante centenas de anos tiveram tempo de confraternizar, caçar, nadar, praticar esportes, casar, ter filhos, construir família e, no coração dessa terra, a Amazônia, cultivar o maior jardim do mundo.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "As crianças levavam uma vida muito livre e muito à vontade. Subiam nas árvores, nadavam nos rios, caçavam pequenos animais... Corriam ao ar livre...",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Os adultos desenvolveram seus símbolos, seus padrões, seus grafismos. Estampavam suas peles, suas casas, seus utensílios, seus artefatos. Viveram assim por eras, convivendo em harmonia com a natureza no plano físico e no astral.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Até mesmo os povos rivais, eram rivais porque se separavam por um rio.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Me lembro das aulas de Latim na minha graduação aqui na UFPA. Lembro do saudoso professor Alírio dizer que o radical riv de rival, é o mesmo da palavra latina rivium que significa \"rio\", e que até aparece em river, do inglês. Mas de volta à história:",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Um desses povos era chamado de os Mundurukus, ou 'formigas vermelhas', por um povo rival, os Parintitins. Eles os chamavam assim pois eram numerosos, raivosos e prontos pra atacar.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Um deles, há tempos atrás - ainda em épocas pacíficas - viu às margens do rio um pedaço de ouro refletindo forte a luz numa manhã de céu limpo e sol forte.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Nada de novo, pensou consigo, afinal, ouro era algo que brotava ali aos montes na bacia do Rio Tapajós, local de origem do seu povo. As pedras estavam por toda parte, a ponto de as crianças brincarem de bolinhas de gude com elas.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Nada de novo, a não ser por esse pedaço de ouro parar de brilhar engolida pelo bolso de um garimpeiro, que surgiu ali do nada, servindo de prenúncio para tempos não mais tão pacíficos.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Um homem branco, meio pançudo com um chapelão e uma peneira era o cavaleiro do apocalipse que anunciava a aceleração dos males da vida, outrora nunca rápidos demais para destruir suas bibliotecas vivas antes que elas pudessem ser repostas.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Ao longo do tempo, não vinha só mais um, mas vários, e não só com peneiras, mas com armas de fogo. Cada vez mais os povos às margens do rio precisaram provar sua alcunha de guerreiros...",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "...lutando pela sua sobrevivência agora literalmente, ao ter que combater frente a frente os homens brancos que apareciam cada vez mais numerosos e raivosos, o suficiente para ultrapassar em número e raiva as formigas vermelhas e todos os seus rivais!",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Quando os povos não pereciam por ataque direto dos homens brancos, pereciam pelas doenças que eles traziam. Doenças que acometiam principalmente os anciões. Com o tempo, morria mais ancião do que um povo conseguia repor, fazendo sua cultura e memória serem aos poucos apagadas. Ferindo sua ancestralidade.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Quando eu era pequena, lembro vagamente de ver por cima dos ombros da minha mãe, que me carregava firme em seu colo, os homens de quem ela e meu pai fugiam. Eram jagunços, assassinos a mando dos autoproclamados novos donos daquelas terras.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Lembro de ver eles ficando pra trás enquanto nós embarcávamos com pressa num popopô. A bordo estavam uns companheiros da aldeia, um casal com blusas com as letras S, P e I (eu não sabia ler na época, mas eu ainda iria ver aquelas blusas por anos, até ter idade o suficiente para reconhecer as letras)",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "...e estava também minha avó, Jussara, assim como eu - ela olhava pra mim - e como tu também és Jussara, minha neta.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Zarpávamos Rio Tapajós acima rumo à sua foz, no município de Santarém, onde as águas do Tapajós desaguam no Rio Amazonas, que nos levaria mais ainda ao Norte até a Ilha de Marajó, onde me estabeleci na infância.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Durante a viagem, vovó Jussara me contava essas histórias, e as contaria de novo por milhares de vezes.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Também nos mostrava suas lindas tapeçarias, com aqueles lindos padrões. Eu jamais conseguiria ter talento praquelas tapeçarias. Só mais pra frente, no Marajó, que eu descobriria meu futuro talento: as cerâmicas.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "No Marajó tive tempo pra aprender e me especializar em tudo naquela Ilha, principalmente nas suas duas especialidades: cerâmicas e búfalos. Búfalos e seus derivados.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Aprendi a montar a búfalo, como a polícia na ilha, a fazer um bom churrasco de carne de búfalo, tirar leite de búfala e produzir os incríveis queijos marajoaras.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Nas cerâmicas, tentava reproduzir os padrões Mundurukus das tapeçarias da vovó e aprendia também os padrões marajoaras. Até, vocês sabem, eu casar com seu avô e vir morar aqui perto da família dele, em Cotijuba.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Lá atrás, vovó contava desde as origens dos nossos povos até os detalhes de como fomos parar ali, que eu pessoalmente não lembrava de forma tão clara.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Agora estou contando essa história pra vocês, pois sou uma anciã e vocês são crianças, tal como minha avó Jussara era anciã e eu criança, até que ela partiu, mas suas histórias continuaram vivas em mim.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Um dia eu partirei, mas vocês carregarão consigo a memória dos nossos povos enquanto lembrarem da nossa história. E, algum dia - ela me olhava de novo nessa hora - possam ser os próximos a contar.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Eu até me emociono ao lembrar. Quando ela me olhava depois de contar tudo isso, eu me sentia importante, me sentia como se carregasse toda uma população em minhas costas. Mas não doía, ao contrário, era encorajador! Eu adorava como a vovó fazia eu me sentir.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "O que começava com um leve entretenimento terminava com um sentimento de empoderamento repentino. Era uma sensação quase viciante, não conseguiria imaginar deixar de estar ali ao menos uma vez no ano naquela praia com a minha avó.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Isso até 7 anos atrás. Em 2020, bem, sabemos bem o que rolou naquele ano. A pandemia foi devastadora no Brasil, pior ainda com os mais velhos e, pior ainda, em lugares turísticos. Não tivemos uma política assim tão bem-sucedida de lockdown no nosso país.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Eu e os meus primos já não tínhamos tanto assim o hábito de nos reunir nas rodas de fim de tarde, e a vovó já não tava assim tão disposta como antigamente, e aquele sorriso leve foi sendo substituído por um sorriso mais pesado e cansado. Ainda assim eu fazia questão de ir todo ano pra Cotijuba pra ir fazer uma visita.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Mas infelizmente, naquele ano, tive que visitar por um motivo diferente.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "O movimento das praias continuou intenso ali nas praias da ilha de Cotijuba, inclusive a do Vai Quem Quer. Ficamos sabendo quando vovó Jussara já estava muito enferma em casa. Estávamos todos à sua volta, rodeados também de inúmeras prateleiras repletas de lindíssimos vasos marajoaras produzidos por ela ao longo da vida.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Eu mencionei que ela nos ensinava a pintar seus padrões, né? Isso porque nenhum de nós levava jeito pra cerâmica. A gente brincava com a argila e acabava jogando ela uns nos outros. Pelo visto, assim como vovó não levava jeito pras tapeçarias, mas levava pras cerâmicas, eu também não levo pra cerâmica, mas levo pra pintura.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Parece que os grafismos passam de geração a geração, mas nunca na mesma técnica (imagino qual será a arte da minha neta).",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Foi ali, cercada daquelas joias e de seus netos e filhos que ela proferiu suas últimas palavras: \"Façam uma fogueira como as das rodas de histórias. Quero ser cremada com meus ancestrais...\" e então fechou os olhos.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Eu vi presencialmente o perecimento de uma biblioteca viva pela doença trazida do homem branco. Toda aquela história se consolidou pra mim naquele momento.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Seu último pedido foi realizado e suas cinzas jazem em uma urna que era um dos artefatos mais antigos daquelas prateleiras (senão o mais antigo).",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Não havia sido produzida por ela própria, mas trazida por sua avó no popopô, que por sua vez também lhe havia sido passada por uma ancestral e, até onde sei, está conosco pelo menos desde a origem dos formigas vermelhas na bacia do Rio Tapajós.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Tem um formato diferente de todos os outros e carrega toda essa carga energética de todas essas gerações.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "O tempo passou e, além do garimpo ilegal e do jaguncismo acontecendo às margens do Tapajós desde gerações antes da minha avó, houve diversas propostas de construções de hidrelétricas,",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "sempre barradas por muita resistência dos Mundurukus e dos outros povos da região, que têm lutado bravamente e conquistado apoio de pessoas e órgãos pelo Brasil para terem o direito de continuar sobrevivendo",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "e, consequentemente, protegendo a mata e, de quebra, a toda a população.",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "Agora estão com esse decreto que prevê a total entrega do Rio Tapajós nas mãos dos latifundiários. Depois de tudo o que já fizeram ao logo de séculos e de tudo o que já tiraram...",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call screen jussara_cuia_card(
        "E então, tu vais ajudar a derrubar esse decreto?",
        imagem_cima=JCU_ARTE_TRES_FORMAS,
        zoom_cima=0.85,
        yal_cima=0.10,
    )

    call jussara_1_semana_depois from _call_jussara_1_semana_depois
    return
