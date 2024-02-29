x = int(input("Ingresa numero: "))

if x % 2 == 0:

    print("El numero es primo")

    for i in range(1, x + 1):

        print(f"{i} * {x}: ", i * x)

else:

    print("El numero No es Primo")

    for i in range(1, x + 1):

        print(f"{i} * {x}: ", i * x)

