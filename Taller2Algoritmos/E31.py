i = True

while i == True:

    n1 = int(input("Ingresa primer numero: "))

    n2 = int(input("Ingresa segundo numero: "))

    op = int(input("Ingresa =>\n1--Suma\n2--Resta\n3--Multiplicacion\n4--Division\n5--Salir\nPara saber que Operacion Realizar: "))

    if op == 5:

        i = False 

    elif op == 1:

        suma = n1 + n2

        print("La suma es: ", suma)

    elif op == 2:

        resta = n1 - n2

        print("La resta es: ", resta)

    elif op == 3:

        multi = n1 * n2

        print("La multiplicaciones: ", multi)

    elif op == 4:

        if n2 != 0:

            div = n1 / n2

            print("La division es: ", div)

        else:

            print("No se puede Dividir por Cero")

    