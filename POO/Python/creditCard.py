from payment import Payment
from datetime import datetime

class CreditCard(Payment):
    TypeCredicard = str
    ExpirationDate = datetime.today()
    CVV = str

    def __init__(self, id, TypeCredicard, ExpirationDate, CVV):
        super.__init__(id)
        self.TypeCredicard = TypeCredicard
        self.ExpirationDate = ExpirationDate
        self.CVV = CVV