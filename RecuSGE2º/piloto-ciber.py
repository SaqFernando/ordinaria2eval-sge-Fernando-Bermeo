import pandas as pd
import json

with open('reservas.json', 'r') as file:
    data = json.load(file)

with open('secure-users.json', 'r') as file:
    dataus = json.load(file)

def json_to_dataframe(data , dataus):
    rows = []
    for reserva in data:
        reservaId = reserva['reservaId']
        userId = reserva['userId']
        date = reserva['date']
        hours = reserva['hours']
        salaId = reserva['sala']['salaId']
        suite = reserva['sala']['suite']
        plazas = reserva['sala']['plazas']
        rows.append({'Reserva Id':reservaId, 'User Id':userId,'Date':date, 'Hours':hours, 'Sala Id':salaId, 'Suite':suite, 'Plazas':plazas})
    df = pd.DataFrame(rows)
    return df


def identificador(data, dataus):
    comparacion1 = []
    comparacion2 = []
    nombres = []
    for usuario in dataus:
        id = usuario['id']
        nombre = usuario['nombre']
        comparacion1.append(id)
        nombres.append(nombre)
    for reserva in data:
        userId = reserva['userId']
        comparacion2.append(userId)

    for i in range(11):
        if comparacion1[i] != comparacion2[i]:
            nombres.pop()

    return nombres




identificador(data,dataus)


df = json_to_dataframe(data, dataus)

df.to_excel("ciber_excel.xlsx", index=False)
