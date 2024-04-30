def calcularBonificacion(numero):

    if numero >= 0 and numero < 1000:

        TB = (0 * numero)/100

    elif numero >= 1000 and numero < 5000:

        TB = (3 * numero)/100

    elif numero >= 5000 and numero < 20000:

        TB = (5 * numero)/100

    elif numero > 20000:

        TB = (8 * numero)/100

    return TB

MV = int(input("Ingresa monto de venta: "))

x = calcularBonificacion(MV)

print(x)
