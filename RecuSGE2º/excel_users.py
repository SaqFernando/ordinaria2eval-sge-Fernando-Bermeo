import pandas as pd
import json
import hashlib

with open('secure-users.json', 'r') as file:
    data = json.load(file)

def json_to_dataframe(data):
    rows = []
    for user in data:
        id = user['id']
        nombre = user['nombre']
        password = user['password']
        rows.append({'ID' : id, 'Nombre' : nombre, 'Password': password})
    df = pd.DataFrame(rows)
    return df

df = json_to_dataframe(data)

df.to_excel("usuarios.xlsx", index=False)