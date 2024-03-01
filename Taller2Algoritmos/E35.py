notas = []

for i in range(1,11):

    notas.append(float(input("Ingresa nota: ")))

total = sum(notas)

promedio = total / 10

print("El promedio es: ", round(promedio,2))

x = float(input("Ingresa nota a buscar: "))

busqueda = x in notas

if busqueda == True:

    print("La Nota se encuentra en la lista")

else:

    print("La Nota No se encuentra en la lista")