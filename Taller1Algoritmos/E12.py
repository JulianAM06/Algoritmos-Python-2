n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))
n3 = int(input("Ingresa tercer numero: "))

if n1 == n2 or n2 == n3 or n3 == n1:
    print("Los numeros deben de ser diferentes")

else:
    if n1 > n2 and n1 > n3:
        print("Primer numero mayor")

    elif n2 > n1 and n2 > n3:
        print("Segundo numero mayor")

    elif n3 > n1 and n3 > n2:
        print("Tercer numero mayor")


