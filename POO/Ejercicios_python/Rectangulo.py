class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base   = base
 
    
    def calcular_area(self):
        return self.base * self.altura
        

altura = float(input("Ingrese la altura del rectangulo: "))
base = float(input("Ingrese la base del rectangulo: "))

rectangulo1 = Rectangulo(altura, base)
print(f"El area de un rectangulo es: {rectangulo1.calcular_area()} ")

