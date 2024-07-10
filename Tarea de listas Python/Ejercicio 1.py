def encontrar_mayor(numeros):
  
  mayor = numeros[0] 
  posicion_mayor = 0
  for i in range(1, len(numeros)):
    if numeros[i] > mayor:
      mayor = numeros[i]
      posicion_mayor = i
  return mayor, posicion_mayor


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

mayor, posicion = encontrar_mayor(numeros)
print(f"El mayor número es {mayor} y se encuentra en la posición {posicion}.")