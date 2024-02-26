empleado = input("Ingresa nombre del empleado: ")
horasLaboradas = int(input("Ingresa cantidad de horas laboradas: "))

valorHora = 50

pagoParcial = horasLaboradas * valorHora

if pagoParcial > 2400:

    pagoTotal = pagoParcial - 84

else:

    valorSeguroSocial = pagoParcial * 0.035 

    pagoTotal = pagoParcial - valorSeguroSocial

print(f"El nombre del empleado es: {empleado} y su pago total es: {pagoTotal}")
    

