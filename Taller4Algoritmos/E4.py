def validarEdad(numero):

    if numero <= 11:

        E = 'Niño'

    elif numero >= 12 and numero <= 17:

        E = 'Adolescente'

    elif numero >= 18 and numero <= 64:

        E = 'Adulto'

    elif numero >= 65:

        E = 'Viejo'

    return E



x = int(input("Ingresa edad a validar: "))

edad = validarEdad(x)

print(edad)