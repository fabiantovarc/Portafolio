from Product import Product

class Order:
    counter_order = 0

    def __init__(self, products):
        Order.counter_order += 1
        self._id_order = Order.counter_order
        self._products = list(products)

    def add_product(self, product):
        self._products.append(product)

    
    def calcular_total(self):
        total = 0
        for product in self._products:
            total += product.price
        return total 

    
    def __str__(self):
        products_str = ""
        for product in self._products:
            products_str += product.__str__() + " / "
        return f"Order: {self._id_order} \nProducts: {products_str}"


if __name__ == '__main__':
    product1 = Product("Guayaba", 15000)
    product2 = Product("Melon", 10000)
    products = [product1, product2]
    orden2 = Order(products)
    print(orden2)