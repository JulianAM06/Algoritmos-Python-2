n = int(input("Ingresa cantidad de personas a evaluar: "))

for i in range(1, n + 1):

    numeroCarne = int(input("Ingresa numero de carne: "))
    numeroMaterias = int(input("Ingresa cantidad de materias: "))
    estrato = int(input("Ingresa estrato social: "))
    valorMateria = 100000

    if numeroMaterias > 5 and estrato == 1:

        totalMaterias = numeroMaterias * valorMateria

        descuento = totalMaterias * 0.20

        totalMatricula = totalMaterias - descuento

        print(f"El estudiante con carne: {numeroCarne} tiene un descuento de: {descuento} para valor total de matricula de: {totalMatricula}")

    else:

        totalMatricula = numeroMaterias * valorMateria

        print(f"El estudiante con carne: {numeroCarne} tiene un total de matricula de: {totalMatricula}")



