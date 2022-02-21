import json

carros_json='{"marca":"honda", "modelo":"hrv", "cor":"prata"}'

carros=json.loads(carros_json)

print(carros)
print(carros["marca"])
print(carros["modelo"])
print(carros["cor"])

for x in carros:
    print(x)

for x in carros.values():
    print(x)

for k,v in carros.items():
    print(k,v)

for k,v in carros.items():
    print(k + " - " + v)
    