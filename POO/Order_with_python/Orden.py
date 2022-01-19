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

    def __init__(self,computaras):
        self.idOrden = Orden.generar_contadorOrden()
        self._computadoras =list(computaras)

    
