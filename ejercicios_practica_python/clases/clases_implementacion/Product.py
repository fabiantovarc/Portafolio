

class Product:
    counter_product = 0


    def __init__(self, name, price):
        Product.counter_product +=1
        self._id_product = Product.counter_product
        self._name = name
        self._price = price


    def __str__(self):
        return f"Id product: {self._id_product}, Name: {self._name}, Price: {self._price}"

    @property
    def price(self):
        return self._price

    
if __name__ == '__main__':
    product1 = Product("Guayaba", 15000)
    product2 = Product("Melon", 10000)