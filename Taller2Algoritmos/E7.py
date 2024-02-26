i = True
T = 0

while i == True:

    x = input("Ingresa frases, si deseas salir ingresa S: ")

    if x == "S":

        i = False

    elif x == "s":

        i = False

    else: 

        T = T + 1

print("La cantidad de frases ingresadas son: ", T)