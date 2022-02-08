from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self,alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
    
    def __str__(self):
        return f"Figura geometrica:[Alto {self.alto}, Ancho {self.ancho}, Color: {self.color}]"

    def calcular_area(self):
        return self.alto * self.ancho
    

    
if __name__ == '__main__':
    """
    
    alto = float(input("Ingrese la alto del rectangulo: "))
    ancho = float(input("Ingrese la ancho del rectangulo: "))
    color = str(input("Ingrese la base del color: "))
 
    print("Datos ingresados por el usuario".center(50,"-"))
    rectangulo1 = Rectangulo(alto, ancho, color)
    print(rectangulo1)
    print(f"El area de un rectangulo es: {rectangulo1.calcular_area()} ")
"""
    

    print("Impresion otros datos ".center(50,"-"))
    rectangulo2 = Rectangulo(alto =9, ancho= 5, color="Black")
    rectangulo2.ancho = 30
    print(rectangulo2)
    print(f"El area de un rectangulo es: {rectangulo2.calcular_area()} ")








