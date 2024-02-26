AN = int(input("Ingresa año de nacimiento: "))
AA = int(input("Ingresa año actual: "))
SIJP = int(input("Ingresa 1 si esta inscrito al SIJP, 0 si no: "))
SSRA = int(input("Ingresa 1 si esta inscrito SSRA, 0 si no: "))

E = AA - AN

if E > 17 and SIJP == 1 or SSRA == 1:
    print("Debe solicitar CUIL")
    
else:
    print("No debe solicitar CUIL")