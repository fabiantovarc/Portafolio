from Vehiculo import *
      
class Bicicleta:
    gama = str

    def __init__(self, gama):
        self.gama = gama

class  Bicicleta(Vehiculo):
    def __init__(self,tipoVehiculo, atributos, ruedas, color, gama):
        super().__init__(tipoVehiculo, atributos, ruedas ,color )
        self.gama = gama

    def __str__(self):
        return f" {super().__str__()}, [color:{self.gama}]"

    
vehiculo1 = Bicicleta("Bicicleta" ,"Todo terrreno" , 2, "azul", "Alta")
print(vehiculo1)