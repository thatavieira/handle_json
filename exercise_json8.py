import json

jogador_dictionary={
    "nome":"bruno",
    "time":"aviadores",
    "vivo":"true",
    "energia":100,
    "mochila":["pederneira","corda","linha","arame"],
    "aeronaves": [
        {"tipo":"transporte", "habilidade": 80},
        {"tipo":"ataque", "habilidade": 100},
        {"tipo":"reconhecimento", "habilidade": 50}
    ]
}


jogador_j=json.dumps(jogador_dictionary)
print(jogador_j)



