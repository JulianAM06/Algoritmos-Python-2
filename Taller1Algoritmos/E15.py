MV = int(input("Ingresa el Monto de Venta: "))

if MV >= 0 and MV < 1000:

    TB = (MV*0)/100

elif MV >= 1000 and MV < 5000:

    TB = (MV*3)/100

elif MV >= 5000 and MV < 20000:

    TB = (MV*5)/100

elif MV >= 20000:
    TB = (MV*8)/100

print("La bonificacion es de: ", MV)