# -*- coding: utf-8 -*-
import tkinter as tk

# funcion
def resp():
    resp_correcta = entry_respuesta_correcta.get()
    resp_incorrecta = entry_respuesta_incorrecta.get()
    resp_en_blanco = entry_respuesta_en_blanco.get()

    resp_correcta_puntos = float(resp_correcta) * 3
    resp_incorrecta_puntos = float(resp_incorrecta) * -1
    resp_en_blanco_puntos = float(resp_en_blanco) * 0

# crear ventana
root = tk.Tk()

# configuracion root
root.title("promedio")
root.minsize(350,150)
root.resizable(0,0)

# elementos
# label
label_respuesta_correcta = tk.Label(root,text="ingrese las respuestas correctas: ")
label_respuesta_incorrecta = tk.Label(root,text="Ingrese las respuestas incorrectas: ")
label_respuesta_en_blanco = tk.Label(root,text="Ingrese las respuestas en blanco: ")

# caja de txt
text_respuesta_correcta = tk.StringVar()
text_respuesta_incorrecta = tk.StringVar()
text_respuesta_en_blanco = tk.StringVar()

# entrada de txt
entry_respuesta_correcta = tk.Entry(root,width=20,textvariable=text_respuesta_correcta)
entry_respuesta_incorrecta = tk.Entry(root,width=20,textvariable=text_respuesta_incorrecta)
entry_respuesta_en_blanco = tk.Entry(root,width=20,textvariable=text_respuesta_en_blanco)

# boton
bt = tk.Button(root,text="calcular")

# posicion de elementos
# label
label_respuesta_correcta.grid(row=0, column=0)
label_respuesta_incorrecta.grid(row=1, column=0)
label_respuesta_en_blanco.grid(row=2, column=0)

# entrada de txt
entry_respuesta_correcta.grid(row=0, column=1)
entry_respuesta_incorrecta.grid(row=1, column=1)
entry_respuesta_en_blanco.grid(row=2, column=1)

# boton
bt.grid(row=3, column=2)

root.mainloop()