name = "adri"
name1 = "pepe"
#condicional que comprueba una variable
if name == "pepe":
    print("admin: ", name)
elif name == "adri":
    print("user: ", name)
#para comprobar la segunda variable name1 tendriamos que duplicar la condiconal anterio
#la funcion def eval (name) la funcion va arecibir un parametro entre los paretesis , este parametro sera las variables que creasmos que queremos comprobar su condicion 
def eval (name):
    if name == "pepe":
      print("admin: ", name)
    elif name == "adri":
      print("user: ", name)
    else:
       print("no se reconoce este usuario")

#llamar al a funcion y pasarle el parametro
eval (name)
eval (name1)
eval ("k")