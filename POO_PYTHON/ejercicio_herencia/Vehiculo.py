class  Vehiculo:
    tipoVehiculo = str
    atributos    = str
    ruedas       = int
    color        = str
    


    def __init__(self, tipoVehiculo, atributos, ruedas, color):
        self.tipoVehiculo = tipoVehiculo
        self.atributos = atributos
        self.ruedas = ruedas
        self.color = color
        

    def mostrar_detalles(self):
        print(f"Tipo vehiculo: {self.tipoVehiculo}, {self.atributos}, {self.ruedas}, {self.color}")

    def __str__(self):
        return f"Tipo vehiculo: {self.tipoVehiculo}, Atributos: {self.atributos}, No Ruedas: {self.ruedas}, Color {self.color}]"


if __name__ == '__main__':
    vehiculo1 = Vehiculo("Bicicleta", "Todo terreno", 2, "Negro")
    vehiculo1.mostrar_detalles()
