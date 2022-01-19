class Monitor:
    contadorMonitores = 0
    idMonitor = int
    marca   = str
    tamano  = float
    precio  = float
    tipoEntrada = str

    @classmethod
    def generar_contadorM(cls):
        cls.contadorMonitores +=1
        return cls.contadorMonitores

    def __init__(self,marca,tamano, precio, tipoEntrada):
        self.idMonitor     = Monitor.generar_contadorM()
        self._marca        = marca
        self._tamano       = tamano
        self._precio       = precio
        self._tipoEntrada  = tipoEntrada

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano
    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano
    
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def tipoEntrada(self):
        return self._tipoEntrada
    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada
    
    def mostrar_detalles(self):
        return f" Marca: {self._marca}, Tamaño:{self._tamano}, Precio: {self._precio}, Tipo Entrada: {self._tipoEntrada}"


    def __str__(self):
        return f" Marca: {self._marca}, Tamaño:{self._tamano}, Precio: {self._precio}, Tipo Entrada: {self._tipoEntrada}"
        
if __name__ == '__main__':
    dis1 = Monitor("SAMSUNG",25,600000,"HDMI")
    print(dis1.mostrar_detalles())