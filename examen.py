#Julian Alzate Monsalve
#2846458

#Ejercicio 1

n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))
n3 = int(input("Ingresa tercer numero: "))

if n1 == n2 or n2 == n3 or n3 == n1:
    print("Los numeros deben de ser diferentes")

else:
    if n1 > n2 and n1 > n3:
        print("Primer numero mayor")

    elif n2 > n1 and n2 > n3:
        print("Segundo numero mayor")

    elif n3 > n1 and n3 > n2:
        print("Tercer numero mayor")





#Ejercicio 2
#Forma 1

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

# Forma 2
    
x = int(input("Ingresa numero entre 1 - 5 para conocer la vocal correspondiente: "))

if x == 1:

    print("La vocal correspondiente de acuerdo al numero es A")

elif x == 2:

    print("La vocal correspondiente de acuerdo al numero es E")

if x == 3:

    print("La vocal correspondiente de acuerdo al numero es I")

if x == 4:

    print("La vocal correspondiente de acuerdo al numero es O")

if x == 5:

    print("La vocal correspondiente de acuerdo al numero es U")