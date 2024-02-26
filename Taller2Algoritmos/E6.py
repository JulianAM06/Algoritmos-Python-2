x = int(input("Ingresa un numero natural: "))

if x > 0:

    for i in range(0, x + 1, 1):

        print(i)

elif x < 0:

    for i in range(0, x - 1, -1):

        print(i)
