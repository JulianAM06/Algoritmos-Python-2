notas = []

for i in range(1,11):

    notas.append(float(input("Ingresa nota: ")))


total = sum(notas)

promedio = total / 10

print("El promedio es: ", round(promedio,2))
