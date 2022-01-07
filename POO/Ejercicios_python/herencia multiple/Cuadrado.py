from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f"Figura geometrica:[Lados: {self.lado}, Color: {self.color}]"

if __name__ == '__main__':

    persona1 = Cuadrado(40, "Azul")
    persona1.alto = 40

    print(f"El area de un rectangulo es: {persona1.calcular_area()} ")


