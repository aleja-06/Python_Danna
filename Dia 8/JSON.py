import json
data = {}#Diccionario
data["clientes"] = [] #Lista
data["clientes"].append({
    "nombre": "danna",
    "edad":18,
    "altura":1.55,
    "importe":2.55
})

data["clientes"] = [] #Lista
data["clientes"].append({
    "nombre": "Andrea",
    "edad":22,
    "altura":1.60,
    "importe":2.55
})

data["clientes"].append({
    "nombre": "andrea",
    "edad":20,
    "altura":1.72,
    "importe":2.55
})
with open("data.json", "w") as file:
    json.dump(data, file , indent=4)