NE = int(input("ingresa el numero de empleados: "))

SS = 0

for i in range(NE):
    
    SE = float(input("Ingresa sueldo: "))
    
    SS = SS + SE
    
P = SS/NE

print("Promedio de Sueldos: ", P)