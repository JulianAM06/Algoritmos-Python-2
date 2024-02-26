def encontrarDivisores(numero):
  
  divisores = []

  for i in range(1, numero + 1):

    if numero % i == 0:
      
      divisores.append(i)

  return divisores


numero = int(input("Ingrese un número entero positivo para conocer sus divisores: "))

divisores = encontrarDivisores(numero)

print("Los divisores de", numero, "son:", divisores)