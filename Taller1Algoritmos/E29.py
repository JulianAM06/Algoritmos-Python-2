cantidadVotos = int(input("Ingrese cantidad de Votos: "))

i = 0
votosCandidatoUno = 0
votosCandidatoDos = 0
votosCandidatoTres = 0
votosBlanco = 0
porcentajeVotosC1 = 0
porcentajeVotosC2 = 0
porcentajeVotosC3 = 0
porcentajeVotosBlanco = 0


if cantidadVotos > 0:
    
    
    while cantidadVotos > i:
        
        voto = int(input("Ingrese\nCandidato Uno--1\nCandidato Dos--2\nCandidato Tres--3\nVotos Blanco--4\nPara conocer el voto:"))
        
        if voto == 1:
            
            votosCandidatoUno += 1
            
        elif voto == 2:
            
            votosCandidatoDos += 1
            
        elif voto == 3:
            
            votosCandidatoTres += 1

        elif voto == 4:
            
            votosBlanco += 1
            
        else:
            
            print("El numero ingresado no lo reconoce el sistema")
            
        i = i + 1
        
        
    
    totalVotos =  votosCandidatoUno + votosCandidatoDos + votosCandidatoTres + votosBlanco 
    
    porcentajeVotosC1 = (votosCandidatoUno/totalVotos)*100
    porcentajeVotosC2 = (votosCandidatoDos/totalVotos)*100
    porcentajeVotosC3 = (votosCandidatoTres/totalVotos)*100
    porcentajeVotosBlanco = (votosBlanco/totalVotos)*100
    
    
    print("Cantidad de Votos del Candidato Uno es: ",votosCandidatoUno)
    print("Cantidad de Votos del Candidato Dos es: ",votosCandidatoDos)
    print("Cantidad de Votos del Candidato Tres es: ",votosCandidatoTres)
    print("Cantidad de Votos en Blanco" ,votosBlanco)
    print("Porcentaje de Votos del Candidato Uno es: ",porcentajeVotosC1)
    print("Porcentaje de Votos del Candidato Dos es: ",porcentajeVotosC2)
    print("Porcentaje de Votos del Candidato Tres es: ",porcentajeVotosC3)
    print("Porcentaje de Votos en Blanco: ", porcentajeVotosBlanco)
        

    if votosCandidatoUno > votosCandidatoDos and votosCandidatoUno > votosCandidatoTres and votosCandidatoUno >votosBlanco:
        
        print("El ganador es el Candidato Uno")
        
    elif votosCandidatoDos > votosCandidatoUno and votosCandidatoDos > votosCandidatoTres and votosCandidatoDos >votosBlanco:
        
        print("El ganador es el Candidato Dos")
        
    elif votosCandidatoTres > votosCandidatoUno and votosCandidatoTres > votosCandidatoDos and votosCandidatoTres >votosBlanco:
        
        print("El ganador es el Candidato Tres")

    else:
        print("Gano el Voto en Blanco")