from Order import Order
from Product import Product

product1 = Product("Guayaba", 15000)
product2 = Product("Melon", 10000)
product3 = Product("Blusa", 20000)
product4 = Product("Boxer", 5100)

products1 = [product1, product2]
products2 = [product3, product4]
orden1 = Order(products1)
orden2 = Order(products2)
print(f"{orden1} Total: {orden1.calcular_total()}")
print(f"{orden2} Total: {orden1.calcular_total()}")