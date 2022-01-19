from DispositivosEntrada import DispositivosEntrada

class Teclado(DispositivosEntrada):
    contador_teclado = 0
    idTeclado = str
    
    @classmethod
    def generar_contadorTeclado(cls):
        cls.contador_teclado +=1
        return cls.contador_teclado

    def __init__(self,tipoEntrada, marca, precio):
        super(Teclado, self).__init__(tipoEntrada, marca, precio)
        self.idTeclado = Teclado.generar_contadorTeclado()
        self.tipoEntrada = tipoEntrada
        self.marca       = marca
        self.precio      = precio

    def mostrar_detalles(self):
        return f"[Id Teclado: {self.idTeclado}, Marca: {self.marca}, Precio: {self.precio}, Tipo Entrada: {self.tipoEntrada}]"


    def __str__(self):
        return f"[Id Teclado: {self.idTeclado} Marca: {self.marca}, Precio: {self.precio}, Tipo Entrada: {self.tipoEntrada}]"

if __name__ == '__main__':
    teclado1 = Teclado("USB", "SAMSUNG", 150000)
    teclado2 = Teclado("Tipo C", "LG", 250000)
    print(teclado1)
    print(teclado2)


    