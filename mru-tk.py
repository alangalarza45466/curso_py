# -*- coding: utf-8 -*-
import tkinter as tk 
# funcion
def distancia_recorrida():
    velocity = entry_velocity.get()
    print(velocity)
    tiempo = entry_tiempo.get()
    label_distancia.configure(text=f"distancia recorrida: {float(velocity) * float(tiempo)}")

root = tk.Tk()

# configuracion root
root.minsize(1080,720)
root.resizable(0,0)

# elementos
# label
label_title = tk.Label(root,text="calcular distancia recorrida por un movil")
label_velocity = tk.Label(root,text="velocidad")
label_tiempo = tk.Label(root,text="tiempo")
label_distancia = tk.Label(root,text="distancia recorrida")
# caja txt
text_velocity = tk.StringVar()
text_tiempo = tk.StringVar()

# entrada de txt
entry_velocity = tk.Entry(root,width=20,textvariable=text_velocity)
entry_tiempo = tk.Entry(root,width=20,textvariable=text_tiempo)

# botones
bt = tk.Button(root,text="evaluar", command=lambda: distancia_recorrida())


# posicion de los elementos
# label
label_title.grid(row=0, column=0)
label_velocity.grid(row=1, column=0)
label_tiempo.grid(row=2,column=0)
label_distancia.grid(row=3,column=0)
# entrada de txt
entry_velocity.grid(row=1, column=1)
entry_tiempo.grid(row=2, column=1)

# botones
bt.grid(row=4,column=0, columnspan=2)

root.mainloop()