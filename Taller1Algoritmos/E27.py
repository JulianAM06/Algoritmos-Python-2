n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))
op = input("Ingresa\nSuma: +\nResta: -\nMultiplicacion: *\nDivision: /\nPara saber que operacion realizar: ")

if op == "+":

    R = n1 + n2

elif op == "-":

    R = n1 - n2

elif op == "*":
    
    R = n1 * n2

elif op == "/":
    if n2 != 0:
        R = n1 / n2
    else:
        print("La operacion no se puede realizar porque n2 debe ser diferente de cero")

print(R)