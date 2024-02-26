"""def numeroRomano(numero):

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

    romano = numeros.get(numero, 1)
    return romano


x = int(input("Ingresa un numero entre 1 y 10 para conocer su equivalente en numero Romano: "))

romano = numeroRomano(x)

if romano != 1:

    print(f"El numero romano de {x} es: {romano}")

else:
    print("Recuerda que es un numero entre 1 a 10 :)")"""


x = int(input("Ingresa un numero entre 1 y 10 para conocer su equivalente en numero Romano: "))

if x == 1:

    print("El equivalente Romano es l")

elif x == 2:

    print("El equivalente Romano es ll")