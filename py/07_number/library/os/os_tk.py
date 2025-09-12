from tkinter import Tk, Entry, Label, Button
import os

def create_folder (name):
    #comprobar si existe la carpeta
    if not os.path.exists(name):
     os.mkdir(name)


root = Tk()
root.title("")
root.minsize(350, 350)
root.resizable(0, 0)

Label(root, text="Nombre de la carpeta:").grid(column=0, row=0)

entry_name = Entry(root, width=20)
entry_name.grid (column=1, row=0)

Button(root, text="Crear carpeta", command=lambda: create_folder(entry_name.get())).grid(column=1, row=2)

root.mainloop()