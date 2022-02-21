import json

carros_dictionary={
    "marca": "honda",
    "modelo": "hrv",
    "cor": "prata"
}
#dictionary -> objeto json

carros_list=["honda", "volkswagem", "ford", "fiat", "chevrolet"]
#list -> array json

carros_tupla=("honda", "volkswagem", "ford", "fiat", "chevrolet")
#tupla -> array jason

carros_j=json.dumps(carros_dictionary)
print(carros_j)

carros_j=json.dumps(carros_list)
print(carros_j)

carros_j=json.dumps(carros_list)
print(carros_list)

carros_j=json.dumps(carros_dictionary,indent=4)
print(carros_j)

carros_j=json.dumps(carros_dictionary,indent=4,separators=(": ","="))
print(carros_j)

carros_j=json.dumps(carros_dictionary,indent=4,separators=(": ","="),sort_keys=True)
print(carros_j)