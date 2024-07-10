def calcular_promedio_entero(numeros):
  
  suma = sum(numeros)
  promedio = suma // len(numeros)  
  return promedio


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

promedio = calcular_promedio_entero(numeros)
print(f"El promedio entero de los números en la lista es: {promedio}")