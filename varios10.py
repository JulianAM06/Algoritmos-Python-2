i = True

while i == True:

    x = int(input("Ingresa\nNumeros Romanos--1\nVocales--2\nSalir--3\nPara conocer el proceso: "))

    if x == 1:

        def numeroRomano(numero):

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


        x = int(input("Ingresa un numero entre 1 y 10 para conocer su equivalente en numero Romano: "))

        if x >= 1 and x <= 10:

            romano = numeroRomano(x)

            print(f"El numero romano de {x} es: {romano}")

        else:
            print("-------Recuerda que es un numero entre 1 a 10 :(---------")

    elif x == 2:

        def determinarVocal(numero):

            vocales = {

                1: "A",
                2: "E",
                3: "I",
                4: "O",
                5: "U"

            }

            vocal = vocales.get(numero)
            return vocal


        x = int(input("Ingresa numero entre 1 - 5 para conocer la vocal correspondiente: "))

        if x >= 1 and x <= 5:

            vocal = determinarVocal(x)

            print("La vocal correspondiente de acuerdo al numero es: ", vocal)

        else: 
            print("-------------Recuerda que es un numero entre 1 y 5 :(-----------------")

    elif x == 3:

        print("----------------Hasta Pronto :)------------------")

        i = False
