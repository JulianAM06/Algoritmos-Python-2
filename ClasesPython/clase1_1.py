#Estructuras Basicas de Python
#input = Entrada por teclado
# "..." = Comentarios en Python
# = => Asignacion
# ==  => Comparacion
#imprimir = print
#limpiar consola = cls
#redondeo de numeros = round

#Tipos de Datos
#Numero Entero = int
#Numero Decimal = float
#Letras = string => str
#Booleano = True o False
#Suma = +
#Resta = -
#Multiplicacion = *
#Division = /
# mayor > menor
# menor < mayor
# mayor igual >=
# menor igual <=
# != => diferente de


#Condicionales
#si = if
#sino = else
#sino si = elif

#Ciclos
#para = for
#mientras = while
#haga mientras = do while

#Funciones = def
#get = conseguir o buscar
#return = devolver

#Claves Python
#1. Si no se pone el tipo de dato, automaticamente se toma como un string o cadena de caracteres
#2. Si se pone float me recibe numeros enteros

#Diccionarios
#clave - valor
#{}


n1 = float(input("Ingresa primera nota: "))
n2 = float(input("Ingresa segunda nota: "))
n3 = float(input("Ingresa tercera nota: "))

sumarNotaS = n1 + n2 + n3

promedioNotas = round(sumarNotaS / 3, 4)

print("El promedio es: ", promedioNotas)

