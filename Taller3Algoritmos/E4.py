print("Sitema de Registro de Ventas")

n = int(input("Ingresa cantidad de ventas: "))

for i in range(1, n + 1):

    nombreArticulo = input("Ingresa nombre de articulo: ")
    precioUnidad = int(input("Ingresa precio del articulo: "))
    cantidadArticulos = int(input("Ingresa cantidad de articulos: "))

    valorTotal = precioUnidad * cantidadArticulos

    print(f"El nombre del articulo es: {nombreArticulo} y la venta total es de: {valorTotal}")