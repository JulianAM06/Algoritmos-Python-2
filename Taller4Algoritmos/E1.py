def convertirRomano(numero):

    numeros = {
        1: 'l',
        2: 'll',
        3: 'lll',
        4: 'lV',
        5: 'V',
        6: 'Vl',
        7: 'Vll',
        8: 'Vlll',
        9: 'lX',
        10: 'X'
    }

    romano = numeros.get(numero)
    return romano

x = int(input("Ingresa numero de 1 a 10 para convertir a Romano: "))

if x >= 1 and x <= 10:

    numero = convertirRomano(x)

    print(numero)

else:

    print("Ingresa numeros entre 1 y 10 :)")