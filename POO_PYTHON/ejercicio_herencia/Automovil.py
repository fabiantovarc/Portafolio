from Vehiculo import *

class Automovil:
    pasajeros = int
    puertas   = int

    def __init__(self, pasajeros, puertas):
        self.pasajeros = pasajeros
        self.puertas = puertas

class  Automovil(Vehiculo):
    def __init__(self,tipoVehiculo, atributos, ruedas, color, pasajeros, puertas):
        super().__init__(tipoVehiculo, atributos, ruedas ,color )
        self.pasajeros = pasajeros
        self.puertas = puertas

    def __str__(self):
        return f" {super().__str__()}, [Numero de Pasajeros:{self.pasajeros} puertas {self.puertas}]"

    
vehiculo1 = Automovil("Automovil" ,"Todo terrreno" , 4, "negro", 4, 4)
print(vehiculo1)