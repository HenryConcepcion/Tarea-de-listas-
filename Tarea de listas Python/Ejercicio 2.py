def encontrar_mayor_par(numeros):
  
  mayor_par = None  
  posicion_mayor_par = None
  for i in range(len(numeros)):
    if numeros[i] % 2 == 0 and (mayor_par is None or numeros[i] > mayor_par):
      mayor_par = numeros[i]
      posicion_mayor_par = i
  return mayor_par, posicion_mayor_par


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

mayor_par, posicion = encontrar_mayor_par(numeros)
if mayor_par is not None:
  print(f"El mayor número par es {mayor_par} y se encuentra en la posición {posicion}.")
else:
  print("No se encontraron números pares en la lista.")