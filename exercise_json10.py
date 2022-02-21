import json

carros={
    "marca":"honda",
    "modelo":"hrv",
    "cor":"prata"
}

carros_json=json.dumps(carros)
print(carros_json)

#dumps= converte um elemento python(neste caso um dictionary em arquivo json).

#dictionary -> objeto python
#list -> array json
#tupla -> array json

