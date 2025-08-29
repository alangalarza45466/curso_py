from tkinter import Tk, Label, StringVar, Entry, Button

# function
def pro():
    try:
        pro_numero_1 = float(entry_numero_1.get())
        pro_numero_2 = float(entry_numero_2.get())
        
        promedio = (pro_numero_1 + pro_numero_2) / 2
        label_promedio.config(text=f"Promedio de los dos números: {int (promedio)}"), {promedio}")
    except ValueError:
        label_promedio.config(text="Error: ingrese solo números")

root = Tk()
root.title("Doble número")
root.minsize(350, 350)
root.resizable(0, 0)

Label(root, text="Número 1").grid(column=0, row=0)
Label(root, text="Número 2").grid(column=0, row=1)

entry_numero_1 = Entry(root, width=20)
entry_numero_1.grid(column=1, row=0)

entry_numero_2 = Entry(root, width=20)
entry_numero_2.grid(column=1, row=1)

Button(root, text="Calcular el promedio", command=pro).grid(column=1, row=2)

label_promedio = Label(root, text="Promedio: ")
label_promedio.grid(column=0, row=3)

root.mainloop()
