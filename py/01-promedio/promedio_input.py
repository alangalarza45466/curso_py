# -*- coding: utf-8 -*-
# la funcion input() convierte cualquier valor a cadena de texto
# convertir  un valor numerico de str a tipo entero o flotante
# funciones int() y float()
n1 = input("ingrese la primera nota: ")
n2 = input("ingrese la segunda nota: ")
n3 = input("ingrese la tercera nota: ")
p = float(n1) + float(n2) + float(n3) / 3
print(f"promedios del alumno: {p}")