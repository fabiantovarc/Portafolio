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
    
    def __init__(self,nombre,monitores,ratones, teclados):
        self.idComputadora =    Computadora.generar_contadorR()
        self._nombre       =    nombre
        self._monitores    =    list(monitores)
        self._ratones      =    list(ratones)      
        self._teclados     =    list(teclados)

    def add_monitores(self, monitores):
        self._monitores.append(monitores)

    def add_ratones(self, ratones):
        self._ratones.append(ratones)

    def add_teclados(self, teclados):
        self._teclados.append(teclados)


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"ID Computador: {self.idComputadora} | \n [Monitor: {Monitor.__str__()}] | \n [Raton: {Raton.__str__()}] | \n [Teclado: {Teclado.__str__()}] "


if __name__ == '__main__':
    pantalla1 = Monitor("samsung",30,6000, "HDMI")
    raton1 = Raton("Tipo C", "DELUX", 150000)
    teclado1 = Teclado("Tipo C", "Genius", 200000)
