import random

contador = 0

for i in range(1,101,1):

    x = random.randint(1,6)

    y = random.randint(1,6)

    suma = x + y

    if suma == 10:

        contador = contador + 1

print("La Cantidad de veces que la Suma de los dados es 10 son: ", contador)






