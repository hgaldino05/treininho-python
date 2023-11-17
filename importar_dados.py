import xlwings as xw

# Abre a planilha do Excel
wb = xw.Book(r"C:\Users\henrique.couto\Documents\inventario-teste.xlsx")


# Importa os dados do arquivo .txt
wb.sheets["inventario"].range("A1:H2800").value = xw.Range(r"C:\Users\henrique.couto\Downloads\inventario.txt").importrange("A1:H2800")

# Salva a planilha do Excel
wb.save()