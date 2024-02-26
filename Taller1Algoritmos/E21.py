CP = int(input("Ingresa cantidad de personas a evaluar por edad: "))
MAE = 0
MEE = 0

for i in range(CP):
    
    EDAD = int(input("Ingresa edad: "))
    
    if EDAD >= 18:
        
        MAE = MAE + 1
        
    else:
        
        MEE = MEE + 1
        
print("Personas Mayores de Edad: ", MAE)
print("Personas Menores de Edad: ", MEE)