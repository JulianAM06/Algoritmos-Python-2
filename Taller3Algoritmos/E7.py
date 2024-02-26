n = int(input("Ingresa cantidad de personas a evaluar: "))

for i in range(1, n + 1):

    nombre = input("Ingresa nombre de persona: ")
    edad = int(input("Ingresa edad: "))
    estatura = float(input("Ingresa estatura en metros: "))

    if edad >= 18 and estatura >= 1.80:

        print("El nombre es: ", nombre)