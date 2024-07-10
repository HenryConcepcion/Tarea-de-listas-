def contar_divisores_exactos(numero, lista_numeros):
  
  contador = 0
  for divisor in lista_numeros:
    if numero % divisor == 0:
      contador += 1
  return contador


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

numero_a_dividir = int(input("Ingrese el número para buscar divisores: "))

cantidad_divisores = contar_divisores_exactos(numero_a_dividir, numeros)
print(f"El número {numero_a_dividir} tiene {cantidad_divisores} divisores exactos en la lista.")