N = int (input("Ingresa un numero positivo y que sea diferente de cero: "))

if N > 0:

    R = N % 2

    if R == 0:
        print("Es Par")

    else:
        print("Es Impar")