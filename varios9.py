primerNumero = int(input("Ingresa primer numero: "))
segundoNumero = int(input("Ingresa segundo numero: "))
tercerNumero = int(input("Ingresa tercer numero: "))

if primerNumero > segundoNumero and primerNumero > tercerNumero and segundoNumero > tercerNumero:

    print(f"Mayor:{primerNumero} Medio:{segundoNumero} Menor:{tercerNumero}")

elif primerNumero > segundoNumero and primerNumero > tercerNumero and tercerNumero > segundoNumero:

    print(f"Mayor:{primerNumero} Medio:{tercerNumero} Menor:{segundoNumero}")

elif segundoNumero > primerNumero and segundoNumero > tercerNumero and primerNumero > tercerNumero:

    print(f"Mayor:{segundoNumero} Medio:{primerNumero}  Menor:{tercerNumero}")

elif segundoNumero > primerNumero and segundoNumero > tercerNumero and tercerNumero > primerNumero:

    print(f"Mayor:{segundoNumero} Medio:{tercerNumero}  Menor:{primerNumero}")

elif tercerNumero > primerNumero and tercerNumero > segundoNumero and segundoNumero > primerNumero:

    print(f"Mayor:{tercerNumero} Medio:{segundoNumero}  Menor:{primerNumero}")

elif tercerNumero > primerNumero and tercerNumero > segundoNumero and primerNumero > segundoNumero:

    print(f"Mayor:{tercerNumero} Medio:{primerNumero}  Menor:{segundoNumero}")

elif primerNumero == segundoNumero and primerNumero == tercerNumero: 

    print("Los numero son iguales")

elif primerNumero == segundoNumero and tercerNumero > segundoNumero:

    print("Primer y Segundo numero iguales, Tercer numero Mayor")

elif primerNumero == segundoNumero and tercerNumero < segundoNumero:

    print("Primer y Segundo numero iguales, Tercer numero Menor")

elif segundoNumero == tercerNumero and primerNumero > segundoNumero:

    print("Segundo y tercer numero iguales, Primer numero Mayor")

elif segundoNumero == tercerNumero and primerNumero < segundoNumero:

    print("Segundo y tercer numero iguales, Primer numero Menor")

elif primerNumero == tercerNumero and segundoNumero > primerNumero:

    print("Primer y tercer numero iguales, Segundo numero Mayor")

elif primerNumero == tercerNumero and segundoNumero < primerNumero:

    print("Primer y tercer numero iguales, Segundo numero Menor")


