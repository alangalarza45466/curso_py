respuestas_correctas = 1
respuestas_incorrectas = 2
respuestas_en_blanco = 2

respuestas_correctas_puntos = respuestas_correctas * 3
respuestas_incorrectas_puntos = respuestas_incorrectas * -1
respuestas_en_blanco_puntos = respuestas_en_blanco * 0

r = (respuestas_correctas) + float(respuestas_incorrectas) + float(respuestas_en_blanco)

print(f"respuestas del alumno: {r}")