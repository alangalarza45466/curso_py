import tkinter as tk

# funcion
def part():
    try:
        part_ganados = float(entry_partidos_ganados.get())
        part_empatados = float(entry_partidos_empatados.get())
        part_perdidos = float(entry_partidos_perdidos.get())

        puntos = (part_ganados * 3) + (part_empatados * 1) + ( part_perdidos * 0)
        text_puntos_finales.set(f"Resultado: {puntos} puntos")
    except ValueError:
        text_puntos_finales.set("Ingrese números validos 🤬")

# crear ventana
root = tk.Tk()
root.title("promedio")
root.minsize(350,150)
root.resizable(0,0)

# caja de txt
text_partidos_ganados = tk.StringVar()
text_partidos_empatados = tk.StringVar()
text_partidos_perdidos = tk.StringVar()
text_puntos_finales = tk.StringVar()

# elementos
# label
label_partidos_ganados = tk.Label(root,text="Ingrese los partidos ganados: ")
label_partidos_empatados = tk.Label(root,text="Ingrese los partidos empatados: ")
label_partidos_perdidos = tk.Label(root,text="Ingrese los partidos perdidos: ")
label_puntos = tk.Label(root, textvariable=text_puntos_finales)

# entry
entry_partidos_ganados = tk.Entry(root,width=20,textvariable=text_partidos_ganados)
entry_partidos_empatados = tk.Entry(root,width=20,textvariable=text_partidos_empatados)
entry_partidos_perdidos = tk.Entry(root,width=20,textvariable=text_partidos_perdidos)

# boton
bt = tk.Button(root,text="Calcular", command=part)

# posicion de elementos
# label
label_partidos_ganados.grid(row=0,column=0)
label_partidos_empatados.grid(row=1,column=0)
label_partidos_perdidos.grid(row=2,column=0)
label_puntos.grid(row=3, column=0)
# entry
entry_partidos_ganados.grid(row=0,column=1)
entry_partidos_empatados.grid(row=1,column=1)
entry_partidos_perdidos.grid(row=2,column=1)
# bt
bt.grid(row=3,column=1)

root.mainloop()