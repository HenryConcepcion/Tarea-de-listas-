def factorial(numero):
  
  if numero == 0:
    return 1
  else:
    return numero * factorial(numero - 1)


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

factoriales = []
for numero in numeros:
  factoriales.append(factorial(numero))

print(f"Los factoriales de los números son: {factoriales}")