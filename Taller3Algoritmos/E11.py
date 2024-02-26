print("-------Bienvenido al Programa de Registros---------")
print("-------Ingresa los Datos de cada Persona---------")

i = True
cantidadMujeresSistemas = 0
cantidadHombresSistemas = 0
cantidadPersonasProgramacion = 0
edadTotalProgramacion = 0
totalPersonasMtto = 0
totalMenoresMtto = 0
totalMujerDiseño = 0
nombreMujerSistemas = []
edadMujeresSistemas = []
nombreHombreSistemas = []
edadHombreSistemas = []

while i == True:

    nombre = input("Ingresa nombre: ").capitalize()
    edad = int(input("Ingresa edad: "))
    sexo = int(input("Ingresa =>\n1--Masculino\n2--Femenino\nPara conocer sexo: "))
    estadoCivil = int(input("Ingresa =>\n1--Soltero\n2--Casado\n3--Union Libre\n4--Viudo\nPara conocer Estado Civil: "))
    carrera = int(input("Ingresa =>\n1--Sistemas\n2--Programacion\n3--Mantenimiento\n4--Diseño\nPara conocer Carrera: "))
    salida = int(input("Ingresa =>\n1--Para Continuar Ingresando Datos\n2--Para Salir Programa\n=> "))

    if salida == 2:

        i = False

        print("------Hasta Pronto---------")
        print("------Mostrare los Resultados----------")

    if salida == 1:

        print("---------Siguiente Registro----------")

    if carrera == 1:

        if sexo == 2:

            cantidadMujeresSistemas = cantidadMujeresSistemas + 1

            nombreMujerSistemas.append(nombre)

            edadMujeresSistemas.append(edad)

            edadMenorSistemas =min(edadMujeresSistemas)

            posicionEdadMenor = edadMujeresSistemas.index(edadMenorSistemas)
        
        if sexo == 1:

            cantidadHombresSistemas = cantidadHombresSistemas + 1

            nombreHombreSistemas.append(nombre)

            edadHombreSistemas.append(edad)

            edadMayorSistemas =max(edadHombreSistemas)

            posicionEdadMayor = edadHombreSistemas.index(edadMayorSistemas)

    if carrera == 2:

        if estadoCivil == 2:

            cantidadPersonasProgramacion = cantidadPersonasProgramacion + 1

            edadTotalProgramacion = edadTotalProgramacion + edad

    if carrera == 3:

        totalPersonasMtto = totalPersonasMtto + 1

        if edad >= 18:

            totalMenoresMtto = totalMenoresMtto + 1

    if carrera == 4:

        if sexo == 2:

            if edad >= 18:

                totalMujerDiseño = totalMujerDiseño + 1


if cantidadMujeresSistemas != 0:

    print("El nombre de la Mujer mas joven de Sistemas es: ", nombreMujerSistemas[posicionEdadMenor])

if cantidadHombresSistemas != 0:

    print("El nombre del Hombre mas viejo de Sistemas es: ", nombreHombreSistemas[posicionEdadMayor])

if cantidadPersonasProgramacion != 0:

    print("El promedio de edad de las Personas de Programacion es: ", edadTotalProgramacion/cantidadPersonasProgramacion)

if totalPersonasMtto != 0:

    print("El porcentaje de Menores de Edad en Mantenimiento es: ", (totalMenoresMtto/totalPersonasMtto) * 100)

if totalMujerDiseño != 0:

    print("La cantidad de Mujeres de Diseño Mayores de edad son: ", totalMujerDiseño)