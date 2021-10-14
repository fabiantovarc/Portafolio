"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
 El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres 
 con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte 
 al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
def run():

    sexo = str(input("Ingrese el sexo a cual pertenece, ¿hombre o mujer?: "))
    name = str(input("Ingrese el nombre de la persona "))

    # en esta condicional lo que se hace es pasar tanto el nombre como el sexo en minuscula
    # se compara los resultados si son iguales para definir su sexo y el grupo al que pertenece
    # de la misma forma que se hace con los numeros las operaciones 
    # si es mayor que o menor que, con el abecedario se puede implementar igualmente
    if (sexo.lower() == "hombre" and name.lower() < "m" ) or (sexo.lower() == "mujer" and name.lower() > "n" ):
        group = "A"

    else:
        group = "B"
    print("tu grupo es "+ group)


if __name__ == '__main__':
    run()