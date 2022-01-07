from car import Car

class CarBasic(Car):
    brand = str
    model = str

    def __init__(self, license, driver,passegenger, brand, model):
        super(CarBasic, self).__init__(license, driver,passegenger)
        self.brand = brand
        self.model = model
        self.passegenger = passegenger