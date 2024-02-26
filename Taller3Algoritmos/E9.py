n = int(input("Ingresa cantidad de vehiculos: "))

for i in range(1, n + 1):

    tipoVehiculo = int(input("Ingresa =>\n1--Bus\n2--Buseta\n3--Colectivo\nPara saber que vehiculo: "))
    cantidadPasajeros = int(input("Ingresa cantidad de pasajeros Transportados: "))

    pasajeBus = 400
    pasajeBuseta = 500
    pasajeColectivo = 800

    if tipoVehiculo == 1:

        dineroTotal = cantidadPasajeros * pasajeBus

        pagoConductor = dineroTotal * 0.20

        print(f"El numero de placa de vehiculo es: {tipoVehiculo}, recaudo {dineroTotal} y un pago para el conductor de {pagoConductor}")

    elif tipoVehiculo == 2:

        dineroTotal = cantidadPasajeros * pasajeBuseta

        pagoConductor = dineroTotal * 0.20

        print(f"El numero de placa de vehiculo es: {tipoVehiculo}, recaudo {dineroTotal} y un pago para el conductor de {pagoConductor}")

    elif tipoVehiculo ==3:

        dineroTotal = cantidadPasajeros * pasajeColectivo

        pagoConductor = dineroTotal * 0.20

        print(f"El numero de placa de vehiculo es: {tipoVehiculo}, recaudo {dineroTotal} y un pago para el conductor de {pagoConductor}")






