import json

dados='{"nome": "renato lelis", "profissao": "desenvolvedor de sistemas"}'

dados_json = json.loads(dados)

print(type(dados_json))