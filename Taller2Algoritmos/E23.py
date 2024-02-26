fila = int(input("Ingresa numero de filas para almacenar los numeros del 1 al 100: ")) 
columna = int(input("Ingresa numero de columnas para almacenar los numeros del 1 al 100: ")) 

matrix = []

i = 0

CC = fila * columna

if CC == 100:

    for j in range(fila): 
        fila = []
        for elemento in range(columna):
                i += 1
                fila.append(i)
        matrix.append(fila)

    for fila in matrix:
        for elemento in fila:
            print(elemento, end="  ")
        print() 

else:
     print("Debes ingresar cantidad de filas y columnas para almacenar los 100 numeros")