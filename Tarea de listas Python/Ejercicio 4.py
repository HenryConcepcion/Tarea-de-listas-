def es_primo(digito):
  
  if digito <= 1:
    return False
  if digito == 2 or digito == 3 or digito == 5 or digito == 7:
    return True
  return False

def contar_numeros_primo(numeros):
  
  contador = 0
  for numero in numeros:
    primer_digito = int(str(abs(numero))[0])  
    if es_primo(primer_digito):
      contador += 1
  return contador


numeros = []
for i in range(10):
  numeros.append(int(input(f"Ingrese el número {i+1}: ")))

cantidad_primos = contar_numeros_primo(numeros)
print(f"Hay {cantidad_primos} números que comienzan con un dígito primo en la lista.")