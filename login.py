x = True

while x == True:

    m = int(input("Ingresa =>\n1--Crear Cuenta\n2--Ingresar Cuenta\n3--Recuperar Cuenta\n4--Salir\nPara saber que deseas hacer: "))

    if m == 1:

        print("-------Bienvenido Crea tu Cuenta--------")
        N1 = input("Ingresa tu nombre: ")
        C1 = input("Ingresa tu contraseña: ")

        print("------Cuenta Creada Correctamente--------")


    elif m == 2:

        print("------Genial ya estas registrado, ingresa a tu cuenta-------")
        N2 = input("Ingresa tu nombre: ")
        C2 = input("Ingresa tu contraseña: ")

        if N1 == N2 and C1 == C2:

            print("----Genial!!!!!...Bienvenido a tu cuenta :)------")

        else:

            print("------Credenciales incorrectas! :(--------------")

    elif m == 3:

        print("-------Bienvenido Crea Nuevamente tus Credenciales--------")

        N1 = input("Ingresa tu nombre: ")
        C1 = input("Ingresa tu contraseña: ")

        print("-------Credenciales Creadas Nuevamente--------")

    elif m == 4:

        print("------Hasta Pronto :)-----------")

        x = False




    

    

