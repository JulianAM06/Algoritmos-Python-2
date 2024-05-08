# 11.	Se tiene registrado la producción (unidades) logradas por un operario a lo largo de la semana (lunes a sábado). Elabore un algoritmo que nos muestre o nos diga si el operario recibirá incentivos sabiendo que el promedio de producción mínima es de 100 unidades.

PLU = int(input("Ingresar produccion del Lunes: "))
PMA = int(input("Ingresar produccion del Martes: "))
PMI = int(input("Ingresar produccion del Miercoles: "))
PJU = int(input("Ingresar produccion del Jueves: "))
PVI = int(input("Ingresar produccion del Viernes: "))
PSA = int(input("Ingresar produccion del Sabado: "))


PT = PLU + PMA + PMI + PJU + PVI + PSA

PROM = PT / 6

if PROM >= 100:
    print("El empleado recibira la bonificacion")

else:
    print("El empleado no recibira la bonificacion")











