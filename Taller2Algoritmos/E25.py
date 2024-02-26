def convertir_a_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numero_romano = ''
    i = 0
    while numero > 0:
        if numero >= valores[i]:
            numero_romano += romanos[i]
            numero -= valores[i]
        else:
            i += 1
    return numero_romano

numero = int(input("Ingresa un número menor a 5000: "))
if numero < 5000:
    numero_romano = convertir_a_romano(numero)
    print(f"El número {numero} en romano es: {numero_romano}")
else:
    print("El número ingresado es mayor o igual a 5000. Por favor ingresa un número menor.")