TP = 0
TI = 0

for i in range(1, 101, 1):

    print(i)

    if i % 2 == 0:

        TP = TP + i  

    else:
        TI = TI + i

print("Suma de los numeros pares: ", TP)
print("Suma de los numeros impares: ", TI)