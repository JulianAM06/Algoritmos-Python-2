def vocales(numero):

    numeros = {
        1: 'a',
        2: 'e',
        3: 'i',
        4: 'o',
        5: 'u',
    }

    vocal = numeros.get(numero)
    return vocal

x = int(input("Ingresa numero de 1 a 5 para conocer su vocal: "))

if x >= 1 and x <= 5:

    numero = vocales(x)

    print(numero)

else:

    print("Ingresa numeros entre 1 y 5 :)")