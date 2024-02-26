L1 = float(input("Ingresa medida en centimeteros del lado 1 del triangulo: "))
L2 = float(input("Ingresa medida en centimeteros del lado 2 del triangulo: "))
L3 = float(input("Ingresa medida en centimeteros del lado 3 del triangulo: "))

if L1 != L2 and L1 != L3 and L2 != L3:
    print("Tringulo Escaleno!")

elif L1 == L2 and L2 == L3:
    print("Tringulo Equilatero!")

else:
    print("Tringulo Isosceles!")