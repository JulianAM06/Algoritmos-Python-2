n = int(input("Ingresa un numero positivo diferente de cero: "))
F = 1

if n > 0:

    for i in range(1, n + 1):

        F = F * i

print("El factorial es: ",F)