def contar_negativos(numeros):
  
  contador = 0
  for numero in numeros:
    if numero < 0:
      contador += 1
  return contador


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

cantidad_negativos = contar_negativos(numeros)
print(f"Hay {cantidad_negativos} números negativos en la lista.")