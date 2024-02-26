# Ingrese 3 numeros, y encontrar cual es el mayor, mitad y menor
# and = y
# or = o
# print = escribir

primerNumero = int(input("Ingresa primer numero: "))
segundoNumero = int(input("Ingresa segundo numero: "))
tercerNumero = int(input("Ingresa tercer numero: "))

if primerNumero > segundoNumero and primerNumero > tercerNumero and segundoNumero > tercerNumero:

    print("Primer numero Mayor, Segundo numero Medio, Tercer numero Menor")

if primerNumero > segundoNumero and primerNumero > tercerNumero and tercerNumero > segundoNumero:

    print("Primer numero Mayor, Tercer numero Medio, Segundo numero Menor")

if segundoNumero > primerNumero and segundoNumero > tercerNumero and primerNumero > tercerNumero:

    print("Segundo numero Mayor, Primer numero Medio, Tercer numero Menor")

if segundoNumero > primerNumero and segundoNumero > tercerNumero and tercerNumero > primerNumero:

    print("Segundo numero Mayor, Tercer numero Medio, Primer numero Menor")

if tercerNumero > primerNumero and tercerNumero > segundoNumero and segundoNumero > primerNumero:

    print("Tercer numero Mayor, Segundo numero Medio, Primer numero Menor")

if tercerNumero > primerNumero and tercerNumero > segundoNumero and primerNumero > segundoNumero:

    print("Tercer numero Mayor, Primer numero Medio, Segundo numero Menor")

if primerNumero == segundoNumero and primerNumero == tercerNumero: 

    print("Los numero son iguales")

if primerNumero == segundoNumero and tercerNumero > segundoNumero:

    print("Primer y Segundo numero iguales, Tercer numero Mayor")

if primerNumero == segundoNumero and tercerNumero < segundoNumero:

    print("Primer y Segundo numero iguales, Tercer numero Menor")

if segundoNumero == tercerNumero and primerNumero > segundoNumero:

    print("Segundo y tercer numero iguales, Primer numero Mayor")

if segundoNumero == tercerNumero and primerNumero < segundoNumero:

    print("Segundo y tercer numero iguales, Primer numero Menor")

if primerNumero == tercerNumero and segundoNumero > primerNumero:

    print("Primer y tercer numero iguales, Segundo numero Mayor")

if primerNumero == tercerNumero and segundoNumero < primerNumero:

    print("Primer y tercer numero iguales, Segundo numero Menor")


