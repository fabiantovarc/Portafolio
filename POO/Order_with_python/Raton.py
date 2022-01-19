class Raton:
    contador_ratones = 0
    idRaton = int
    nombreRaton = str
    precioRaton = int

    @classmethod
    def generar_contador(cls):
        cls.contador_ratones +=1
        return cls.contador_ratones

    def __init__(self, nombreRaton, precioRaton):
        self.idRaton = Raton.generar_contador()
        self._nombreRaton = nombreRaton
        self._precioRaton = precioRaton

    @property
    def nombreRaton(self):
        return self._nombreRaton

    @nombreRaton.setter
    def nombreRaton(self, nombreRaton):
        self._nombreRaton = nombreRaton

    @property
    def precioRaton(self):
        return self._precioRaton

    @precioRaton.setter
    def precioRaton(self, precioRaton):
        self._precioRaton = precioRaton
    
    def mostrar_detalles(self):
        return f"Id Raton: {self.idRaton}, Nombre: {self._nombreRaton}, Precio: {self._precioRaton}, Contador: {Raton.contador_ratones}"


    def __str__(self):
        return f"Id Raton: {self.idRaton}, Nombre: {self._nombreRaton}, Precio: {self._precioRaton}, Contador: {Raton.contador_ratones}"

    

if __name__ == '__main__':
    raton1 = Raton("Curvado", 15000)
    print(raton1)
    raton2 = Raton("GX", 1000)
    print(raton2)