def intentando():
     pass

def run(string):
     print("""
Ingresar el primer nombre de las dos personas
     """)
     nombre = str(input("¿Cual es el nombre de la primera persona?: "))
     nombre1 = str(input("¿Cual es tu nombre de la segunda persona?: "))
     edad = int(input("¿Cuantos años tienes de la primera persona?: "))
     edad1 = int(input("¿Cuantos años tienes de la segunda persona?: "))
     
     while edad > edad1:
          print(nombre, " Es mayor que ", nombre1 )
     if edad < edad1:
          print(nombre, " Es menor que ", nombre1)
     else:
          print(nombre, " Tiene la misma edad que ", nombre1)
     return
try:
     print(run(""))
except TypeError:
     print("no se puede dejar el espacio en blanco")


if __name__ == '__main__':
     run()
