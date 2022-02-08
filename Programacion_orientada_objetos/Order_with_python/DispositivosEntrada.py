class DispositivosEntrada:
    tipoEntrada = str
    marca       = str
    precio      = float

    def __init__(self,tipoEntrada, marca, precio):
        self._tipoEntrada = tipoEntrada
        self._marca       = marca
        self._precio      = precio

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio
    
    def mostrar_detalles(self):
        return f" Marca: {self._marca}, Precio: {self._precio}, Tipo Entrada: {self._tipoEntrada}"


    def __str__(self):
        return f" Marca: {self._marca}, Precio: {self._precio}, Tipo Entrada: {self._tipoEntrada}"
        
if __name__ == '__main__':
    dis1 = DispositivosEntrada("usb","HP", 25000)
    print(dis1.mostrar_detalles())