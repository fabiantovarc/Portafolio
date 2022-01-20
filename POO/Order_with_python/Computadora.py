from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado

class Computadora:
    contadorComputadora = 0
    idComputadora       = int
    nombre              = str
    monitores           = []
    ranotes             = []
    teclados            = []


    @classmethod
    def generar_contadorC(cls):
        cls.contadorComputadora +=1
        return cls.contadorComputadora
    
    def __init__(self,nombre,monitor,raton, teclado):
        self.idComputadora =    Computadora.generar_contadorC()
        self._nombre       =    nombre
        self._monitor      =    monitor
        self._raton        =    raton   
        self._teclado      =    teclado


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"""ID Computador: {self.idComputadora}, Nombre: {self._nombre}  \n [Monitor: {self._monitor}] | \n [Raton: {self._raton}] | \n [Teclado: {self._teclado}] \n \n """


if __name__ == '__main__':
    pantalla1 = Monitor("samsung",30,6000, "HDMI")
    raton1 = Raton("Tipo C", "DELUX", 150000)
    teclado1 = Teclado("Tipo C", "Genius", 200000)
    computador1 = Computadora("Gigabyte", pantalla1, raton1, teclado1)
    print(computador1)
    pantalla2 = Monitor("LG", 30 , 15000000, "HDMI")
    raton2 = Raton("USB", "Logitect", 5000000)
    teclado2 = Teclado("Tipo c", "Force", 500000)
    computador2 = Computadora("Thermaltek", pantalla2, raton2, teclado2)
    print(computador2)