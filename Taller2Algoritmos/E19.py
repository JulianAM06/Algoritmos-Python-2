import time

horas = int(input("Introduce la hora: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

while True:
        
    print(f"Hora:{horas} Minuto:{minutos} Segundo:{segundos}")
    time.sleep(1)
    segundos += 1

    if horas == 24:
        horas = 0

    elif minutos == 60:
        minutos = 0
        horas += 1

    elif segundos == 60:
        segundos = 0
        minutos += 1

    

   



