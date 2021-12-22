from car import Car
from account import Account
from uberX import UberX
from driver import Driver
from user import User

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

    