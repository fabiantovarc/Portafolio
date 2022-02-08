from FiguraGeometrica import *

class Color:
    color = str


    def __init__(self,color):
        self._color = color

    @property # decorador para convertir un metodo en propiedad (getter)
    def color(self):
        return self._color # se puede agregar una funcion para mostrar los valores y terminos de una persona
    
    @color.setter
    def color(self, color):
        self._color = color # se puede agregar una funcion para mostrar los valores y terminos de una persona

    def mostrar_detalles(self):
        print("cosas")
        print(f"Color: {self._color}")

    def __del__(self):
        print(f"Color: {self._color}")

if __name__ == '__main__':

    figura1 = Color( "Azul")
    print(figura1.color)

    figura1.mostrar_detalles()
    print(__name__)

