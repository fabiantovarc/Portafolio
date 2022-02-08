from FiguraGeometrica import FiguraGeometrica
from Color import Color
from Cuadrado import Cuadrado


#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()


print("Creacion objeto cuadrado".center(50,"-"))
cuadrado1 = Cuadrado(lado = 5, color ="Verde")
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f"Calcular el area de un cuadrado  {cuadrado1.calcular_area()}")
print(cuadrado1)