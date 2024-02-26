
#10.	Elabora un algoritmo que solicite la edad de 2 hermanos y muestre un mensaje indicando la edad del mayor y cuantos años de diferencia tiene con el menor.


edadPrimerHermano = int(input("Ingresa edad primer hermano: "))
edadSegundoHermano = int(input("Ingresa edad segundo hermano: "))

#  Mayor > Menor
#  Menor < Mayor
# if = si
# elif = sino si
# else = sino


if edadPrimerHermano > edadSegundoHermano:

    diferenciaEdad = edadPrimerHermano - edadSegundoHermano

    print("El mayor es el Primer Hermano: ",edadPrimerHermano)

    print("La diferencia de edad entre los hermanos es: ", diferenciaEdad)


if edadSegundoHermano > edadPrimerHermano:

    diferenciaEdad = edadSegundoHermano - edadPrimerHermano

    print("El mayor es el Segundo Hermano: ",edadSegundoHermano)

    print("La diferencia de edad entre los hermanos es: ", diferenciaEdad)

else:
    print("Los hermanos tienen la misma edad")









