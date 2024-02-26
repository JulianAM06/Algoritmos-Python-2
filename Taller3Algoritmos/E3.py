n = int(input("Ingresa cantidad de personas a revisar: "))

for i in range(1, n + 1):

    nombre = input("Ingresa nombre: ")
    edad = int(input("Ingresa edad: "))

    if edad >= 18:

        print(f"La persona {nombre} es mayor de edad: {edad}")

    else:

        print(f"La persona {nombre} es menor de edad: {edad}")