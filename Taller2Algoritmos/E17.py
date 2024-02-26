n1 = int(input("Ingresa un numero cualquiera: "))
n2 = int(input("Ingresa un numero mayor al anterior: "))

CP = 0
SP = 0

if n1 > n2:

    print("Recuerda que el segundo numero debe ser mayor al primero")

else:
    for i in range(n1, n2 + 1, 1):

        print(i)

        if i % 2 == 0:

            CP = CP + 1

            SP = SP + i

    print("Cantidad de numeros pares: ",CP)
    print("Suma de los numero pares: ",SP)