# -*- coding: utf-8 -*-
import tkinter as tk 

# crear ventana
root = tk.Tk()
# configuracion root
root.title("promedio")
root.minsize(350,150)
root.resizable(0,0)

# elementos
# label
label_nota1 = tk.Label(root,text="Ingrese la primera nota: ")
label_nota2 = tk.Label(root,text="Ingrese la segunda nota: ")
label_nota3 = tk.Label(root,text="Ingrese la tercera nota: ")

# caja de txt
text_nota1 = tk.StringVar()
text_nota2 = tk.StringVar()
text_nota3 = tk.StringVar()

# entrada de txt
entry_nota1 = tk.Entry(root,width=20,textvariable=text_nota1)
# posicion de los elementos
# label
label_nota3.grid(row=2, column=0)
label_nota2.grid(row=1, column=0)
label_nota1.grid(row=0, column=0)
# entrada de txt
entry_nota1.grid(row=0, column=1)

root.mainloop()