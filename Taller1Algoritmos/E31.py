def conocerMes(numero):

    meses = {

        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    mes = meses.get(numero,1)
    return mes

NM = int(input("Ingresa un numero del 1 al 12 para conocer el mes al que pertenece: "))

mes = conocerMes(NM)

print("El mes seleccionado de acuerdo al numero es: ", mes)