respuestas_correctas = input("ingrese las respuestas correctas: ")
respuestas_incorrectas = input("ingrese las respuestas incorrectas: ")
respuestas_en_blanco = input("ingrese las respuestas en blanco: ")

respuesta_correcta_punto = float(respuestas_correctas) * 3
respuesta_incorrecta_punto = float(respuestas_incorrectas) * -1
respuesta_en_blanco_punto = float(respuestas_en_blanco) * 0
r = (respuestas_correctas) + float(respuestas_incorrectas) + float(respuestas_en_blanco)
print(f"respuestas del alumno: {r}")