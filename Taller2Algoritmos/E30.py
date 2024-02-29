import random

print("------Bienvenido a la Carrera de Caballos------")

z = int(input("Ingresa la cantidad de kilometros de la Carrera de Caballos: "))

i = True

while i == True:

    x = random.randint(1,z)

    y = random.randint(1,z)

    if x == z:

        print("Caballo 1 Ganador")

        i = False

    elif y == z:

        print("Caballo 2 Ganador")

        i = False

