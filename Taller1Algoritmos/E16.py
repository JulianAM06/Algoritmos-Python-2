
def determinarVocal(numero):

    vocales = {

        1: "A",
        2: "E",
        3: "I",
        4: "O",
        5: "U"

    }

    vocal = vocales.get(numero, -1)
    return vocal


x = int(input("Ingresa numero entre 1 - 5 para conocer la vocal correspondiente: "))

if x >= 1 and x <= 5:

    vocal = determinarVocal(x)

    print("La vocal correspondiente de acuerdo al numero es: ", vocal)

else: 
    print("Recuerda que es un numero entre 1 y 5")


