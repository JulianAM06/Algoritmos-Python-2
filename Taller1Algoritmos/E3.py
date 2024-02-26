# 3.	Elaborar un algoritmo que solicite el número de respuestas correctas, incorrectas y en blanco, correspondientes a postulantes, y muestre su puntaje final considerando, que por cada respuesta correcta tendrá 4 puntos, respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.

repuestasCorrectas = int(input("Ingresa cantidad de respuestas correctas:"))
repuestasIncorrectas = int(input("Ingresa cantidad de respuestas incorrectas:")) 
respuestasBlanco = int(input("Ingresa cantidad de respuestas en blanco:"))

puntajeRespuestasCorrectas = repuestasCorrectas * 4

puntaFinal = puntajeRespuestasCorrectas - repuestasIncorrectas 

print("El puntaje final es: ", puntaFinal)