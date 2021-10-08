"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta.
"""


def productos_run():

    producto = str(input("Ingrese los productos separados por comas: "))
#objeto.replace('a',  'b')
    print(producto.replace(',', '\n'))

if __name__ == '__main__':
    productos_run()