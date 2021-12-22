from payment import Payment

class Paypal(Payment):
    TypeCredicard = str
    reference = str

    def __init__(self, id, TypeCredicard, reference):
        super.__init__(id)
        self.TypeCredicard = TypeCredicard
        self.reference = reference