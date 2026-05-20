## Núcleo do arco Jussara. Passagens Twine em jussara_twine.rpy; módulos em modulos/

label jussara_arco_mirante:
    $ jussara_checkpoint("mirante_campus")
    call universidade_federal_do_para from _call_universidade_federal_do_para
    return

label jussara_fim_mirante:
    hide jussara
    with dissolve
    return
