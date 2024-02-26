num1 = float(input("Ingresa numero 1: "))
num2 = float(input("Ingresa numero 2: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2


if num2 != 0:
    div = num1/num2
else:
    print("No se puede realizar operacion")

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicacion es: ", multi)
print("La division es: ", div)