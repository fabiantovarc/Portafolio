"""
En una determinada empresa, sus empleados son evaluados al final de cada año.
 Los puntos que pueden obtener en la evaluación comienzan en 0.0 y 
 pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos 
 que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no 
 valores intermedios entre las cifras mencionadas. A continuación se muestra 
 una tabla con los niveles correspondientes a cada puntuación. La cantidad de 
 dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

    Nivel	      Puntuación
Inaceptable	        0.0
Aceptable	        0.4
Meritorio	        0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.
"""
def run():
    bonificacion = 2400
    inaceptable = 0
    aceptable = 0.4
    meritorio = 0.6
    prueba = "creo"

    print("""
        Nivel	      Puntuación
    Inaceptable	        0.0
    Aceptable	        0.4
    Meritorio	        0.6 o más
    
    """)
    puntuacion = float(input("Ingrese la puntuacion obtenida: "))

    if puntuacion == inaceptable:
        nivel = "inaceptable"
    elif puntuacion == aceptable:
        nivel = "aceptable"
    elif puntuacion >= meritorio:
        nivel = "meritorio"
    else:
        nivel = ""
        print("Esta puntuación no es válida")

    print("Tu nivel de rendimiento es " + nivel)
    # %.2f sirve para implementar el float en la impresion, sin el 
    print("Te corresponde cobrar %.2f€" % (puntuacion * bonificacion))

            

if __name__ == '__main__':
    run()


