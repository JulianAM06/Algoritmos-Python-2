print("-------Bienvenido al Programa de Registros---------")
print("-------Ingresa los Datos de cada Trabajador---------")

i = True
totalHombresContabilidad = 0
totalHijosContabilidad = 0
personaSistemas = 0
totalPersonalVentas = 0
totalSolterasVentas = 0
totalNombresSalarios = []
nombreSistemas = []
salarioSistemas = []


while i == True:

    nombre = input("Ingresa nombre: ").capitalize()
    edad = int(input("Ingresa edad: "))
    sexo = int(input("Ingresa =>\n1--Masculino\n2--Femenino\nPara conocer sexo: "))
    numeroHijos = int(input("Ingresa numero de hijos: "))
    estadoCivil = int(input("Ingresa =>\n1--Soltero\n2--Casado\n3--Union Libre\nPara conocer Estado Civil: "))
    seccion = int(input("Ingresa =>\n1--Planta\n2--Ventas\n3--Sistemas\n4--Contabilidad\n5--Administracion\nPara conocer la Seccion a la que Pertenece: "))
    valorHora = int(input("Ingresa el valor de la hora laboral: "))
    horasLaboradas = int(input("Ingresa la cantidad de horas laboradas: "))
    salida = int(input("Ingresa =>\n1--Para Continuar Ingresando Datos\n2--Para Salir Programa\n=> "))

    if salida == 2:

        i = False

        print("------Hasta Pronto---------")
        print("------Mostrare los Resultados----------")

    if salida == 1:

        print("---------Siguiente Registro----------")


    totalNombresSalarios.append(nombre)

    salario = valorHora * horasLaboradas

    deducciones = salario * 0.085

    bonificaciones = 17250 + (6000 * numeroHijos)

    totalNombresSalarios.append(salario + bonificaciones - deducciones)

    if seccion == 4:

        if sexo == 1:

            totalHombresContabilidad = totalHombresContabilidad + 1

            totalHijosContabilidad = totalHijosContabilidad + numeroHijos

    elif seccion == 3:

        personaSistemas = personaSistemas + 1

        nombreSistemas.append(nombre)

        salario = valorHora * horasLaboradas

        deducciones = salario * 0.085

        bonificaciones = 17250 + (6000 * numeroHijos)

        salarioSistemas.append(salario + bonificaciones - deducciones)

        salarioMayorSistemas = max(salarioSistemas)

        posicionSalarioMayor = salarioSistemas.index(salarioMayorSistemas)

    elif seccion == 2:

        totalPersonalVentas = totalPersonalVentas + 1

        if estadoCivil == 1:

            totalSolterasVentas = totalSolterasVentas + 1



if totalHombresContabilidad != 0:

    print("El Promedio de Hijos de Hombres en el area de Contabilidad es: ", totalHijosContabilidad/totalHombresContabilidad)

if personaSistemas != 0:

    print("El nombre de la Persona de Sistemas con mas Salario es: ", nombreSistemas[posicionSalarioMayor])

if totalPersonalVentas != 0:

    print("El porcentaje de personas Solteras sobre el Total de Personal de Ventas es: ", (totalSolterasVentas/totalPersonalVentas) * 100)

for i in totalNombresSalarios:

    print(i)



