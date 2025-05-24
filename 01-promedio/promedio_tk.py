# -*- coding: utf-8 -*-
import tkinter as tk 

# funcion
def pro():
    pro_nota1 = entry_nota1.get()
    pro_nota2 = entry_nota2.get()
    pro_nota3 = entry_nota3.get()
    promedio_total = float(pro_nota1) + float(pro_nota2) + float(pro_nota3) / 3 
    label_pro_total.configure(text=f"promedio final: {promedio_total}")


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
label_pro_total  = tk.Label(root,text="promedio final: ")

# caja de txt
text_nota1 = tk.StringVar()
text_nota2 = tk.StringVar()
text_nota3 = tk.StringVar()

# entrada de txt
entry_nota1 = tk.Entry(root,width=20,textvariable=text_nota1)
entry_nota2 = tk.Entry(root,width=20,textvariable=text_nota2)
entry_nota3 = tk.Entry(root,width=20,textvariable=text_nota3)
# boton
bt = tk.Button(root,text="calcular", command=pro)
# posicion de los elementos
# label
label_nota3.grid(row=2, column=0)
label_nota2.grid(row=1, column=0)
label_nota1.grid(row=0, column=0)
label_pro_total.grid(row=3,column=0)
# entrada de txt
entry_nota1.grid(row=0, column=1)
entry_nota2.grid(row=1, column=1)
entry_nota3.grid(row=2, column=1)
# boton
bt.grid(row=3, column=2)

root.mainloop()