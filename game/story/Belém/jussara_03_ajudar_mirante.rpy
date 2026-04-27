## == Jussara — quero ajudar, redes, pix, SP, envolvida na causa ==

label quero_ajudar:
    j "Égua! Que bom ouvir isso de você também! Temos inúmeras formas de ajudar."
    j "Você pode acompanhar os perfis das causas nas redes, já que a mídia hegemônica praticamente ignora ou diminui a causa. Por isso é importante ajudar na comunicação e combater a desinformação por aí."
    j "Você também pode fazer um pix solidário, ajudar na compra de alimentos, água e materiais para as ocupações, que contem com secretarias, com escolas, cozinha, segurança..."
    j "E então, como pretende ajudar?"

    menu:
        "Agitar nas redes":
            call agitar_nas_redes from _call_agitar_nas_redes
        "Pix solidário para ajudar nas ocupações":
            call pix_solidario from _call_pix_solidario
        "Ajudar a disseminar em SP, o maior hub do Brasil":
            call disseminar_em_sp from _call_disseminar_em_sp
    return

label agitar_nas_redes:
    j "Ah, que legal! Isso aí, obrigado pela sua participação e engajamento! Espero encontrar mais pessoas como tu por aqui."
    return

label pix_solidario:
    j "Isso é muito bom! Tu vais estar ajudando uma grande quantidade de gente, em consequência ajudando a todos nós. Agradecemos de coração pela determinação!"
    return

label disseminar_em_sp:
    j "Sério? Isso seria incrível!"

    menu:
        "Você está pessoalmente envolvida na causa?":
            call envolvida_na_causa from _call_envolvida_na_causa_1
    return

label envolvida_na_causa:
    j "Há um significado espiritual muito grande desse Rio para esses povos. Para os Mundurucus, por exemplo, é o berço do seu povo. A destruição desse rio seria a destruição dos seus ancestrais."
    j "Bom, respondendo à sua pergunta, particularmente tenho um pé de envolvimento pessoal nessa causa. Sou descendente direta de povos originários. Minha avó, que já descansa em paz, costumava me contar a história de seus ancestrais pra me fazer dormir."
    j "Sempre lembro de sua voz doce e firme, me ditando com muita emoção as desventuras de heroísmos dos nossos ancestrais..."

    menu:
        "Me conta a história":
            call contar_historia_artefato from _call_contar_historia_artefato
        "Hmm...":
            call contar_historia_artefato from _call_contar_historia_artefato_1
    return