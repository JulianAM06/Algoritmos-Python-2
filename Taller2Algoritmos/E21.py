menu = int(input("Ingresa\n1--Suma numeros pares desde 1 a 1000\n2--Suma numeros impares desde 1 a 1000\nPara saber que hacer: "))

S = 0

if menu == 1:

    for i in range(1,1001, 1):

        if i % 2 == 0:

            S = S + i

    print("Suma de numeros pares es: ", S)

elif menu == 2:

    for i in range (1, 1001, 1):

        if i % 2 != 0:

            S = S + i

    print("Suma de numeros impares es: ", S)

