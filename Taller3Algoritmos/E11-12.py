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
edadTotalMujeres = 0
totalPersonas = 0
totalMujeres = 0
totalHombres = 0
edadTotalHombres = 0
totalSoltero = 0
totalPersonaCasada = 0
totalViudos = 0
totalUnionLibre = 0
nombreMujerSistemas = []
edadMujeresSistemas = []
nombreHombreSistemas = []
edadHombreSistemas = []
nombreCasadoJoven = []
edadCasadoJoven = []
nombreUnionLibre = []

while i == True:

    nombre = input("Ingresa nombre: ").capitalize()
    edad = int(input("Ingresa edad: "))
    sexo = int(input("Ingresa =>\n1--Masculino\n2--Femenino\nPara conocer sexo: "))
    estadoCivil = int(input("Ingresa =>\n1--Soltero\n2--Casado\n3--Union Libre\n4--Viudo\nPara conocer Estado Civil: "))
    carrera = int(input("Ingresa =>\n1--Sistemas\n2--Programacion\n3--Mantenimiento\n4--Diseño\nPara conocer Carrera: "))
    salida = int(input("Ingresa =>\n1--Para Continuar Ingresando Datos\n2--Para Salir Programa\n=> "))

    totalPersonas = totalPersonas + 1

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

    if sexo == 2:

        totalMujeres = totalMujeres + 1

        edadTotalMujeres = edadTotalMujeres + edad

    if sexo == 1:

        totalHombres = totalHombres + 1

        edadTotalHombres = edadTotalHombres + edad
    
    if estadoCivil == 1:

        totalSoltero = totalSoltero + 1

    if estadoCivil == 2:

        totalPersonaCasada = totalPersonaCasada + 1

        nombreCasadoJoven.append(nombre)

        edadCasadoJoven.append(edad)

        edadMenorCasado = min(edadCasadoJoven)

        posicionEdadMenorCasado = edadCasadoJoven.index(edadMenorCasado)

    if estadoCivil == 4:

        totalViudos = totalViudos + 1

    if estadoCivil == 3:

        if edad > 80:

            totalUnionLibre = totalUnionLibre + 1

            nombreUnionLibre.append(nombre)




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

if totalMujeres != 0:

    print("El promedio de edad de Mujeres es: ", edadTotalMujeres/totalMujeres)

if totalHombres != 0:

    print("El promedio de edad de Hombres es: ", edadTotalHombres/totalHombres)

if totalSoltero != 0:

    print("La cantidad de Personas Solteras son: ", totalSoltero)

if totalPersonaCasada != 0:

    print("El nombre de la Persona Casada mas Joven es: ", nombreCasadoJoven[posicionEdadMenorCasado])

if  totalViudos != 0:

    print("El porcentaje de Viudos es: ", (totalViudos/totalPersonas) * 100)

if totalUnionLibre != 0:

    print("Las personas mayores de 80 años y tienen Union libre son: ", nombreUnionLibre[:])