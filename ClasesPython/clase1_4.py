#Creamos la funcion para validar la vocal

def determinarVocal(numero):

    vocales = {
        
        1: "A", 
        2: "E", 
        3: "I", 
        4: "O",
        5: "U"
        
    }

    vocal = vocales.get(numero, 0)
    return vocal




#Apartir de aca empieza el programa

numero = int(input("Ingresa un numero para saber a que vocal corresponde: "))

conocerVocal = determinarVocal(numero)

if conocerVocal != 0:
    print("La vocal es: ", conocerVocal)

else: 
    print("El numero no corresponde a una vocal")


#print (f"El nombre del empleado es: {empleado} y el pago total es: {pagoTotal}")