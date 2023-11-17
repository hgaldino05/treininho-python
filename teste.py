def fatorial (n):
 if n == 1 or n == 0:
  return 1
 else:
  return n * fatorial(n - 1)

resultado = fatorial(4)
print (resultado)