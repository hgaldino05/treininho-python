import pandas as pd

# Solicita o nome do arquivo CSV ao usuário
csv_file = input("Digite o nome do arquivo CSV a ser convertido: ")

# Remove a extensão .csv do nome do arquivo
csv_file_name = csv_file.split(".")[0]

# Lê o arquivo CSV
df = pd.read_csv(csv_file, encoding="latin1")

# Define o nome do arquivo XLSX
xlsx_file = csv_file_name + ".xlsx"

# Salva o arquivo XLSX
df.to_excel(xlsx_file, index=False)

print(f"O arquivo {csv_file} foi convertido com sucesso em {xlsx_file}!")
