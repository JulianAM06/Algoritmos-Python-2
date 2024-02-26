print("Sitema de Registro de Ventas")

n = int(input("Ingresa cantidad de ventas: "))

for i in range(1, n + 1):

    nombreArticulo = input("Ingresa nombre de articulo: ")
    precioUnidad = int(input("Ingresa precio del articulo: "))
    cantidadArticulos = int(input("Ingresa cantidad de articulos: "))

    valorTotal = precioUnidad * cantidadArticulos

    if valorTotal > 50000:

        descuento = valorTotal * 0.10

        valorTotalDescuento = valorTotal - descuento

        print(f"El nombre del articulo es: {nombreArticulo}, como la venta fue mayor a 50.000 se realiza un descuento de: {descuento} y la venta total es de: {valorTotalDescuento}")

    else:

        print(f"El nombre del articulo es: {nombreArticulo} y la venta total es de: {valorTotal}")