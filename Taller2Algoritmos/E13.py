n = int(input("Ingresa 2 o 3 para conocer sus multiplos hasta el 100: "))
MD = 0
MT = 0

if n == 2: 

    for i in range(n,101, 2):

        print(i)

        MD = MD + 1

    print("Cantidade de multiplos: ", MD)

elif n == 3:

    for i in range(n,101, 3):

        print(i)

        MT = MT + 1
    
    print("Cantidade de multiplos: ", MT)