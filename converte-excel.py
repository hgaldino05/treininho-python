import pandas as pd
import json

def txt_to_xls(txt_file, xls_file):
    with open(txt_file, 'r') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        # Substituindo aspas simples por aspas duplas
        line = line.replace("'", '"')
        # Convertendo a linha para um dicionário
        dict_line = json.loads(line)
        data.append(dict_line)

    # Convertendo a lista de dicionários para um DataFrame
    df = pd.DataFrame(data)

    # Salvando o DataFrame como um arquivo Excel
    df.to_excel(xls_file, index=False)

# Chamando a função
txt_to_xls('inventario.txt', 'inventario.xlsx')
