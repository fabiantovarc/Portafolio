from Vehiculo import *

#class Vehiculo(Bicicleta):
#    def __init__(self, Atributos, montaña):
#        super().__init__(color, ruedas, tipoVehiculo)
#        self
        
class Bicicleta:
    gama = str

    def __init__(self, gama):
        self.gama = gama

class  Bicicleta(Vehiculo):
    def __init__(self,tipoVehiculo, atributos, ruedas, color, gama):
        super().__init__(tipoVehiculo, atributos, ruedas ,color )
        self.gama = gama

    def __str__(self):
        return f" {super().__str__()}, [gama:{self.gama}]"

    
vehiculo1 = Bicicleta("Bicicleta" ,"Todo terrreno" , 2, "azul", "Alta")
print(vehiculo1)