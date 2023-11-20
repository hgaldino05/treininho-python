import pandas as pd

# Lendo o arquivo csv
df = pd.read_csv('arquivo.csv', encoding='latin1')


# Salvando como xlsx
df.to_excel('arquivo.xlsx', index=False)
