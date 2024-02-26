x = int(input("Ingresa numero limite: "))

T = 0

for i in range(3, x + 1, 3):

    T = T + 1

    print(i)

print("La cantidad de multiplos del 3 son: ", T)