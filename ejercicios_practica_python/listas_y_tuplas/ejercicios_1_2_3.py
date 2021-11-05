"""ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla."""
"""ejercicio 2
scribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""
"""ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y 
después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas 
de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
def run():
    my_dict = {"Matemáticas": 4.4, "Física": 5.0, "Química": 3.8, "Historia": 3.5, "Lenguaje": 3.9}
    for i,v in my_dict.items():
        print(f" yo estudio {i} y mi puntaje es {v}")
if __name__ == '__main__':
    run()