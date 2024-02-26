n = int(input("Ingresa cantidad de trabajadores: "))

for i in range(1, n + 1):

    nombre = input("Ingresa nombre trabajador:")
    valorHora = int(input("Ingresa valor hora: "))
    horasLaborales = int(input("Ingresa horas laborales: "))
    deducciones = int(input("Ingresa dedudciones: "))
    bonificaciones = int(input("Ingresa bonificaciones: "))

    salarioNormal = valorHora * horasLaborales

    salarioTotal = (salarioNormal + bonificaciones) - deducciones

    print(f"El trabajador: {nombre} obtuvo un salario total de: {salarioTotal}")