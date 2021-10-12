"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

def run():


    contraseña  = str(input("Ingrese la contraseña: "))

    contra = str(input("Ingrese nuevamente la contraseña: "))

    if contra.lower() == contraseña.lower(): #El formato .lower se realiza para convertir las palabras de string en minusculas
        print("Las dos contraseñan coinciden")
    else:
        print("No coinciden las contraseñas")


if __name__ == '__main__':
    run()