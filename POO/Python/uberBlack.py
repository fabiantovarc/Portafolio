from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial   = []
    
    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super.__init__(typeCarAccepted,seatsMaterial)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial
