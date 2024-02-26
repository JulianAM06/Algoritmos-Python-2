def conocerDescuento(numero):

    descuentos = {

        1: "Descuento 0%",
        2: "Descuento 10%",
        3: "Descuento 25%",
        4: "Descuento 50%",
        5: "Descuento 100%"

    }


    descuento = descuentos.get(numero, -1)
    return descuento



compraTotal = int(input("Ingresa el valor de la compra total: "))
bolita = int(input("Ingresa\n1--Bolita Blanca\n2--Bolita Verde\n3--Bolita Amarilla\n4--Bolita Azul\n5--Bolita Roja\nPara conocer el descuento al cliente:"))

#\n sirve para realizar un salto de pagina

validarDescuento = conocerDescuento(bolita)

if validarDescuento == "Descuento 0%":

    valorPagoDescuento = compraTotal

elif validarDescuento == "Descuento 10%":

    descuento = compraTotal * 0.10

    valorPagoDescuento = compraTotal - descuento

elif validarDescuento == "Descuento 25%":

    descuento = compraTotal * 0.25

    valorPagoDescuento = compraTotal - descuento

elif validarDescuento == "Descuento 50%":

    descuento = compraTotal * 0.50

    valorPagoDescuento = compraTotal - descuento

elif validarDescuento == "Descuento 100%":

    valorPagoDescuento = compraTotal - compraTotal

else:
    print("El numero de la bolita no existe")


print("El valor total a pagar con descuento es: ", valorPagoDescuento)