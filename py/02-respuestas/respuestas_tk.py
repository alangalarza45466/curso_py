# -*- coding: utf-8 -*-
import tkinter as tk

# funcion
def resp():
    try:
        resp_correcta = float(entry_respuesta_correcta.get())
        resp_incorrecta = float(entry_respuesta_incorrecta.get())
        resp_en_blanco = float(entry_respuesta_en_blanco.get())

        puntos = (resp_correcta * 3) + (resp_incorrecta * -1) + (resp_en_blanco * 0)
        text_puntos_finales.set(f"Resultado: {puntos} puntos")
    except ValueError:
        text_puntos_finales.set("Entrada inválida")

# crear ventana
root = tk.Tk()
root.title("promedio")
root.minsize(350,150)
root.resizable(0,0)

# cajas de texto
text_respuesta_correcta = tk.StringVar()
text_respuesta_incorrecta = tk.StringVar()
text_respuesta_en_blanco = tk.StringVar()
text_puntos_finales = tk.StringVar()

# elementos
label_respuesta_correcta = tk.Label(root,text="Ingrese las respuestas correctas:")
label_respuesta_incorrecta = tk.Label(root,text="Ingrese las respuestas incorrectas:")
label_respuesta_en_blanco = tk.Label(root,text="Ingrese las respuestas en blanco:")
label_puntos = tk.Label(root, textvariable=text_puntos_finales)

entry_respuesta_correcta = tk.Entry(root,width=20,textvariable=text_respuesta_correcta)
entry_respuesta_incorrecta = tk.Entry(root,width=20,textvariable=text_respuesta_incorrecta)
entry_respuesta_en_blanco = tk.Entry(root,width=20,textvariable=text_respuesta_en_blanco)

bt = tk.Button(root,text="Calcular", command=resp)

# Posición de elementos
label_respuesta_correcta.grid(row=0, column=0)
label_respuesta_incorrecta.grid(row=1, column=0)
label_respuesta_en_blanco.grid(row=2, column=0)
label_puntos.grid(row=3, column=0)

entry_respuesta_correcta.grid(row=0, column=1)
entry_respuesta_incorrecta.grid(row=1, column=1)
entry_respuesta_en_blanco.grid(row=2, column=1)

bt.grid(row=4, column=1)

root.mainloop()