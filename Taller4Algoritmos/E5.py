def calculadora(numero1, numero2, signo):

    if signo == '+':

        x = numero1 + numero2
    
    elif signo == '-':

        x = numero1 - numero2

    elif signo == '*':

        x = numero1 * numero2

    elif signo == '/':

        x = numero1 / numero2

    return x

n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))
signo = input("Ingresa\n(+)--Sumar\n(-)--Restar\n(*)--Multiplicar\n(/)--Dividir\nPara conocer Operacion: ")

z = calculadora(n1, n2, signo)

print(z)