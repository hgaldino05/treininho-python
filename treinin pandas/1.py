import pandas

marcas = {
  'Marcas': ["BMW", "Volvo", "Ford"],
  'Quantidade': [3, 7, 2]
}

listaMarcas = pandas.DataFrame(marcas)

print(listaMarcas)

a = ['a','b','c']

myvar = pandas.Series(a)
print("\n")
print(myvar)