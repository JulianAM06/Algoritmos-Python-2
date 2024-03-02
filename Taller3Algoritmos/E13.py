print("-------Bienvenido al Programa de Registros Autobuses---------")
print("--------------------Ingresa los Datos----------------")

i = True
liquiColectivo = 0
liquiMicrobus = 0
liquiBuseta = 0
liquiBus = 0
cantidadColectivo = 0
cantidadPasajerosMicrobus = 0
totalPasajeros = 0
cantidadMicrobus = 0
liquiTotalBuses = 0
liquiTotalBuseta = 0
liquiTotalMicrobus = 0
liquiTotalColectivo = 0
liquidacionesBuseta = []
placasBuseta = []


while i == True:

    placa = input("Ingresa placa del vehiculo: ").upper()
    propietario = input("Ingresa el nombre del propietario: ")
    tipoVehiculo = int(input("Ingresa =>\n1--Colectivo\n2--Microbus\n3--Buseta\n4--Bus\nPara saber tipo de Vehiculo: "))
    cantidadPasajeros = int(input("Ingresa cantidad de pasajeros: "))
    valorPasaje = int(input("Ingresa valor de cada pasaje: "))
    salida = int(input("Ingresa =>\n1--Para Continuar Ingresando Datos\n2--Para Salir Programa\n=> "))

    totalPasajeros = totalPasajeros + cantidadPasajeros

    if salida == 2:

        i = False

        print("------Hasta Pronto---------")
        print("------Mostrare los Resultados----------")

    if salida == 1:

        print("---------Siguiente Registro----------")


    if tipoVehiculo == 1:

        liquiColectivo = cantidadPasajeros * valorPasaje

        liquiTotalColectivo = liquiTotalColectivo + liquiColectivo

        if cantidadPasajeros > 100:

            cantidadColectivo = cantidadColectivo + 1

    elif tipoVehiculo == 2:

        cantidadMicrobus = cantidadMicrobus + 1

        cantidadPasajerosMicrobus = cantidadPasajerosMicrobus + cantidadPasajeros

        liquiMicrobus = cantidadPasajeros * valorPasaje

        liquiTotalMicrobus = liquiTotalMicrobus + liquiMicrobus

    elif tipoVehiculo == 3:

        liquiBuseta = cantidadPasajeros * valorPasaje

        liquiTotalBuseta = liquiTotalBuseta + liquiBuseta

        liquidacionesBuseta.append(liquiBuseta)

        placasBuseta.append(placa)

        liquiMayorBuseta = max(liquidacionesBuseta)

        posicionLiquiMayor = liquidacionesBuseta.index(liquiMayorBuseta)

    elif tipoVehiculo == 4:

        liquiBus = cantidadPasajeros * valorPasaje

        liquiTotalBuses = liquiTotalBuses + liquiBus

liquiTotalEmpresa = liquiColectivo + liquiTotalMicrobus + liquiTotalBuseta + liquiTotalBuses

print("La Liquidacion Total del dia es: ", liquiTotalEmpresa)

if cantidadColectivo != 0:

    print("La cantidad de Colectivos que transportaron mas de 100 pasajeros son: ",cantidadColectivo)

if cantidadPasajerosMicrobus != 0:

    print("El promedio de pasajeros que han viajado en Microbus es: ",cantidadPasajerosMicrobus/cantidadMicrobus)

if liquiBuseta != 0:

    print("La placa de la Buseta que mas Dinero recolecto es: ", placasBuseta[posicionLiquiMayor])

if liquiBus != 0:

    print("La cantidad total de liquidacion de los Buses es: ", liquiTotalBuses)

        



    