x = True

while x == True:

    login = int(input("Ingresa\n1--Crear Cuenta\n2--Ingresar a Cuenta\n3--Recuperar Cuenta\n4--Salir\nPara saber que hacer: "))

    if login == 1:  

        print("-------Bienvenido Crea tu Cuenta-----------")
        nombre1 = input("Ingresa tu nombre: ")
        contraseña1 = input("Ingresa tu contraseña: ")
        print("--------Felicitaciones tu Cuenta ha sido Creada----------")

    elif login == 2:

        print("--------Genial!!!, ya tienes tu cuenta creada, Ingresa tus Credenciales----------")

        nombre2 = input("Ingresa tu nombre: ")
        contraseña2 = input("Ingresa tu contraseña: ")

        if nombre1 == nombre2 and contraseña1 == contraseña2:

            print("-------Bienvenido a tu cuenta--------")

        else:
            print("-------Tus credenciales son incorrectas-----------")

    elif login ==3:

        print("--------Recuperar Credenciales---------")

        nombre1 = input("Ingresa tu nombre: ")
        contraseña1 = input("Ingresa tu contraseña: ")

        print("------Credenciales Actualizadas Correctamente-------")

    elif login == 4:

        x = False

        print("--------Sesion Cerrada Correctamente-----------")

        





        


