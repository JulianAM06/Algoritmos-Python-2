print("-------Bienvenido al Programa de Registros---------")
print("-------Ingresa los Datos de cada Persona---------")

i = True
totalEdadFut = 0
totalPersonasCicli = 0
totalMujeresCicli = 0
cantidadPersonasFutbol = 0
cantidadAltasNatacion = 0
totalEdadPersonas = 0
cantidadMujeresPatinaje = 0
totalPersonas = 0
estatMujeresPatinaje = []
nombreMujerPatinaje = []

while i == True:

    nombre = input("Ingresa nombre: ").capitalize()
    edad = int(input("Ingresa edad: "))
    estatura = float(input("Ingresa estatura en centimetros: "))
    sexo = int(input("Ingresa =>\n1--Masculino\n2--Femenino\nPara conocer sexo: "))
    deporte = int(input("Ingresa =>\n1--Natacion\n2--Futbol\n3--Ciclismo\n4--Patinaje\n5--Otro Deporte\nPara conocer deporte: "))
    salida = int(input("Ingresa =>\n1--Para Continuar Ingresando Datos\n2--Para Salir Programa\n=> "))

    if salida == 2:

        i = False

        print("------Hasta Pronto---------")
        print("------Mostrare los Resultados----------")

    if salida == 1:

        print("---------Siguiente Registro----------")

    totalEdadPersonas = totalEdadPersonas + edad

    totalPersonas = totalPersonas + 1

    if deporte == 2:

        totalEdadFut = totalEdadFut + edad

        cantidadPersonasFutbol = cantidadPersonasFutbol + 1

    elif deporte == 3:

        totalPersonasCicli = totalPersonasCicli + 1

        if sexo == 2:

            totalMujeresCicli = totalMujeresCicli + 1

    elif deporte == 4:

        if sexo == 2:

            cantidadMujeresPatinaje = cantidadMujeresPatinaje + 1

            nombreMujerPatinaje.append(nombre)

            estatMujeresPatinaje.append(estatura)

            alturaMayorPatinaje =max(estatMujeresPatinaje)

            posicionAlturaMayor = estatMujeresPatinaje.index(alturaMayorPatinaje)

    elif deporte == 1:

        if estatura > 180:

            cantidadAltasNatacion = cantidadAltasNatacion + 1


if totalEdadFut != 0:

    print("El promedio de edad de los que prefieren futbol es: ", totalEdadFut/cantidadPersonasFutbol)


if totalPersonasCicli != 0:

    print("El porcentaje de mujeres que prefieren ciclismo es: ", (totalMujeresCicli/totalPersonasCicli) * 100)

if cantidadAltasNatacion != 0:

    print("La cantidad de Personas que practican Natacion y tienen una altura mayor a 180 cms son: ", cantidadAltasNatacion)

if cantidadMujeresPatinaje != 0:

    print("El nombre de la mujer mas alta en patinaje es: ", nombreMujerPatinaje[posicionAlturaMayor])


print("El promedio de edad de las personas registradas es: ", round((totalEdadPersonas/totalPersonas),2))

    




