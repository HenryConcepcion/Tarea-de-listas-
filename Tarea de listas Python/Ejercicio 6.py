def encontrar_posiciones_mas_de_tres_digitos(numeros):
  
  posiciones = []
  for i in range(len(numeros)):
    if len(str(abs(numeros[i]))) > 3:
      posiciones.append(i)
  return posiciones


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

posiciones = encontrar_posiciones_mas_de_tres_digitos(numeros)
print(f"Los números con más de 3 dígitos se encuentran en las posiciones: {posiciones}")