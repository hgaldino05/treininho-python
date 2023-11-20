import pandas as pd

# Solicita o nome do arquivo XLSX ao usuário
xlsx_file = input("Digite o nome do arquivo XLSX a ser convertido: ")

# Remove a extensão .xlsx do nome do arquivo
xlsx_file_name = xlsx_file.split(".")[0]

# Lê o arquivo XLSX
df = pd.read_excel(xlsx_file)

# Define o nome do arquivo CSV
csv_file = xlsx_file_name + ".csv"

# Salva o arquivo CSV
df.to_csv(csv_file, index=False)

print(f"O arquivo {xlsx_file} foi convertido com sucesso em {csv_file}!")
