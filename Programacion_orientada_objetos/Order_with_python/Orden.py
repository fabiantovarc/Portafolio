from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from Computadora import Computadora

class Orden:
    contadorOrden = 0
    idOrden = int

    @classmethod
    def generar_contadorOrden(cls):
        cls.contadorOrden +=1
        return cls.contadorOrden
    def __init__(self,computadoras):
        self.idOrden = Orden.generar_contadorOrden()
        self._computadoras =list(computadoras)
    
    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f"Orden: {self.idOrden} \n Computadoras: \n{computadoras_str}"





    
