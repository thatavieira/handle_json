import json

dados = {
    'nome': 'renato lelis',
    'profissao': 'desenvolvedor de sistemas'
}

with open('dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)
