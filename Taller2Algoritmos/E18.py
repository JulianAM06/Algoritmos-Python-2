frase = input("Introduce una frase: ")

letra = input("Introduce la letra que deseas contar dentro de la frase: ")

frase = frase.lower()
letra = letra.lower()

CL = 0

for i in frase:
    if i == letra:
        CL += 1

print("La letra", letra, "aparece", CL, "veces")