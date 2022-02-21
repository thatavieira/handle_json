import json

#{
#    "nome":"bruno",
#    "time":"aviadores",
#    "vivo":"true",
#    "energia":100,
#    "mochila":["pederneira","corda","linha","arame"],
#    "aeronaves":[
#        {"tipo":"transporte","habilidade":80},
#        {"tipo":"ataque","habilidade":100}
#        {"tipo":"reconhecimento","habilidade":50}
#    ]
#}


jogador_j='{"nome":"Bruno","time":"aviadores","vivo":"True","energia":100,"mochila":["pederneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'

jogador=json.loads(jogador_j)
print(jogador)

print(jogador["nome"])
print(jogador["mochila"])
print(jogador["time"])
print(jogador["vivo"])
print(jogador["energia"])
print(jogador["aeronaves"])

for x in jogador.values():
    print(x)

for  k,v in jogador.items():
   print(k,v)