n = int(input("Ingresa numero de dos cifras: "))

if n >=10 and n <= 99:
    CU = n % 10
    CD = n // 10

else:
    print("Recuerda ingresar un numero de dos cifras")

print(f"Cantidad de decenas {CD} y cantidad de unidades {CU}")