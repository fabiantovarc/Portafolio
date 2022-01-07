class Cubo:
    def __init__(self, altura, ancho, profundidad):
        self.altura        = altura
        self.ancho         = ancho
        self.profundidad   = profundidad


    def calcular_volumen(self):
        return self.altura * self.ancho * self.profundidad

altura = float(input("Ingrese la altura del Cubo: "))
ancho = float(input("Ingrese la ancho del Cubo: "))
profundidad = float(input("Ingrese la profundidad del Cubo: "))

cubo1 = Cubo(altura, ancho, profundidad)
print(f"La profundidad de un Cubo es: {cubo1.calcular_volumen()} ")