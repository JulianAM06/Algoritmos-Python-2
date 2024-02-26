#Introducir dos números por teclado. Imprimir los números naturales que hay entre ambos números empezando por el m s pequeño, contar cuantos hay y cuántos de ellos son pares. Calcular la suma de los impares. 

n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

T = 0
P = 0
I = 0



if n1 > n2:

    for i in range(n2, n1 + 1, 1):

        print(i)

        T = T + 1

        if T % 2 == 0:

            P = P + 1

        if T % 2 != 0:

            I = I + i
             

    print("La cantidad de numeros que hay son: ",T)

    print("La cantidad de numeros pares son: ",P)

    print("La suma de los numeros impares es: ", I)



elif n1 < n2:

    for i in range(n1, n2 + 1, 1):

        print(i)

        T = T + 1

        if T % 2 == 0:

            P = P + 1

        if T % 2 != 0:

            I = I + i

    print("La cantidad de numeros que hay son: ",T)
    
    print("La cantidad de numeros pares son: ",P)

    print("La suma de los numeros impares es: ", I)