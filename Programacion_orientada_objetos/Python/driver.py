from account import Account
from car import Car


class Driver(Car,Account):
    def __init__(self,license,passegenger,name, document, email, password):
        Car.__init__(self, license, passegenger)
        Account.__init__(self,name, document, email, password)



    def __str__(self):
        return f"License: {self._license}, Passengers: {self._passegenger}, Name: {self.name}, Document: {self.document}, Email: {self.email}, Password: {self.password}"

    def mostrar_detalles(self):
        print(f"[[Car: Licencia: {self._license}, Passengers: {self._passegenger}], [ Account: Name: {self.name}, Document: {self.document}, Email: {self.email}, Password: {self.password}]]")

if __name__ == "__main__":
    car2 = Car("AMS234", 4)
    print(car2.mostrar_detalles())

    print("Impresion de Driver ".center(50,"-"))
    car1 = Driver("AMS2548", 4, "Pablo Hernandez", "12345678", "Pablo@gmail.com", "1234")
    print(car1)
