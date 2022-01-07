from uberX import UberX
from uberPool import UberPool
from uberBlack import UberBlack
from account import Account
from driver import Driver
from car import Car


class mainDriver(Driver):
    def __init__(self,license,passegenger,name, document, email, password):
        super(Driver, self).__init__(license,passegenger,name, document, email, password)
        
    
    def __str__(self):
        return f"License: {self._license}, Passengers: {self._passegenger}, Name: {self.name}, Document: {self.document}, Email: {self.email}, Password: {self.password}"


        







if __name__ == "__main__":
    print("Impresion de Driver ".center(50,"-"))
    car1 = Driver("AMS2548", 4, "Pablo Hernandez", "12345678", "Pablo@gmail.com", "1234")
    print(car1)













"""
class  main(Car, Account):
    def __init__(self,name, document, email, password,license, driver):
        Account.__init__(self,name, document, email ,password)
        self.name         = name
        self.document     = document
        self.email        = email
        self.password     = password
        Car.__init__(self,license, driver)
        self.license      = license
        self.driver       = driver
            
    def __str__(self):
        return f"Account [Name: {self.name}, {self.document}, {self.email}, {self.password}, {self.license}, {self.driver}]"
     uberX = UberX("ADF875", Account("Felipe López", "GSG458"), "Chevrolet", "Spark")   
    """

    
    

        


"""
if __name__ == "__main__":
    print("Informacion de los carros:")
    print("car")

    car = Car("AMS234", Account("Andres Herrera", "ANDA876", "andres@gmail.com", "1234"), 4)
    print(vars(car))
    print(vars(car.driver))


    uberX = UberX("AXS452", Account("Pablo Ferrera", "10307846", "pablo@gmail.com", "1234"), "Chevrolet", "Spark")
    print(vars(uberX))
    print(vars(uberX.driver))


    user = User("Pablo Gonzales", "484854564", "correo@gmail.com", "12345")
    print(vars(user))
    print(vars(user.driver))
"""


    