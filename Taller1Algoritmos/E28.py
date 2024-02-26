CV = 0
CL = 0


for i in range(10):
        
    x = input("Ingresa una letra o vocal: ")
            
    if x == "A":
        CV = CV + 1
    elif x == "E":
        CV = CV + 1
    elif x == "I":
        CV = CV + 1
    elif x == "O":
        CV = CV + 1
    elif x == "U":
        CV = CV + 1
    elif x == "a":
        CV = CV + 1
    elif x == "e":
        CV = CV + 1
    elif x == "i":
        CV = CV + 1
    elif x == "o":
        CV = CV + 1
    elif x == "u":
        CV = CV + 1
    else:
        CL = CL + 1

print("Cantidad de vocales ingresadas: ", CV)
print("Cantidad de letras ingresadas: ", CL)