from DispositivosEntrada import DispositivosEntrada
class Raton(DispositivosEntrada):
    contador_ratones = 0
    idRaton = int

    @classmethod
    def generar_contadorR(cls):
        cls.contador_ratones +=1
        return cls.contador_ratones

    def __init__(self,tipoEntrada, marca, precio):
        super(Raton, self).__init__(tipoEntrada, marca, precio)
        self.idRaton = Raton.generar_contadorR()
        self.tipoEntrada = tipoEntrada
        self.marca       = marca
        self.precio      = precio

    
    def mostrar_detalles(self):
        return f"Id Raton: {self.idRaton}, Marca: {self.marca}, Precio: {self.precio}, Tipo Entrada: {self.tipoEntrada}"


    def __str__(self):
        return f"Id Raton: {self.idRaton}, Marca: {self.marca}, Precio: {self.precio}, Tipo Entrada: {self.tipoEntrada}"

    

if __name__ == '__main__':
    raton1 = Raton("TIPO C","DELUX", 100000)
    print(raton1)
    raton2 = Raton("USB", "DELUX", 50000)
    print(raton2)