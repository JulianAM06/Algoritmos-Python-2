numeros = []

for i in range(1, 6):

    n = int(input("Ingresa numeros: "))

    numeros.append(n)

print("Numero maximo ingresado:", max(numeros))
print("Numero minimo ingresado: ", min(numeros))