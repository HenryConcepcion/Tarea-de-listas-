def es_primo(numero):
  
  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True

def contar_digitos_pares(numero):
  
  contador = 0
  for digito in str(abs(numero)):
    if int(digito) % 2 == 0:
      contador += 1
  return contador

def encontrar_primo_mas_digitos_pares(numeros):
  
  primo_mas_pares = None
  posicion_mas_pares = None
  for i in range(len(numeros)):
    if es_primo(numeros[i]):
      cantidad_pares = contar_digitos_pares(numeros[i])
      if primo_mas_pares is None or cantidad_pares > contar_digitos_pares(primo_mas_pares):
        primo_mas_pares = numeros[i]
        posicion_mas_pares = i
  return primo_mas_pares, posicion_mas_pares


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

primo_mas_pares, posicion = encontrar_primo_mas_digitos_pares(numeros)
if primo_mas_pares is not None:
  print(f"El número primo con más dígitos pares es {primo_mas_pares} y se encuentra en la posición {posicion}.")
else:
  print("No se encontraron números primos en la lista.")