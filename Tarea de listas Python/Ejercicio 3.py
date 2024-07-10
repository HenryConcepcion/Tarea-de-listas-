def es_primo(numero):
  
  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True

def encontrar_mayor_primo(numeros):
  
  mayor_primo = None  
  posicion_mayor_primo = None
  for i in range(len(numeros)):
    if es_primo(numeros[i]) and (mayor_primo is None or numeros[i] > mayor_primo):
      mayor_primo = numeros[i]
      posicion_mayor_primo = i
  return mayor_primo, posicion_mayor_primo


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

mayor_primo, posicion = encontrar_mayor_primo(numeros)
if mayor_primo is not None:
  print(f"El mayor número primo es {mayor_primo} y se encuentra en la posición {posicion}.")
else:
  print("No se encontraron números primos en la lista.")