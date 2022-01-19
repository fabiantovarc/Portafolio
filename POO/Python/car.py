class Car():
    count_car        = 0
    license          = str
    passegenger      = int
    
    @classmethod
    def _generate_id_car(cls):
        cls.generate_id_car +=1
        return cls.generate_id_car

    def __init__(self, license, passegenger):
        self.id_car         = Car.generate_id_car
        self._license       = license
        self._passegenger   = passegenger

    @property
    def license(self):
        return self._license
    
    @license.setter
    def license(self, license):
        self._license = license

    @property
    def passegenger(self):
        return self._passegenger

    @passegenger.setter
    def passegenger(self, passegenger):
        self._passegenger = passegenger

    def mostrar_detalles(self):
        print(f"[Licencia: {self._license}, Passengers: {self._passegenger}]")

    def __str__(self):
        return f"[Licencia: {self._license}, Passengers: {self._passegenger}]"


if __name__ == "__main__":
    car2 = Car("AMS234", 4)
    print(car2.mostrar_detalles())




 

    