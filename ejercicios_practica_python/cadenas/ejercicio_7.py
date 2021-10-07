"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos 
decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
def producto_run():

    print("ingresa la sifras del producto en euros con dos decimales ")
    producto = input("Ingresa el valor del primer producto: ")

    print("El valor total introducido es de " + producto[:producto.find(",")] + " euros y " + producto[producto.find(",")+1:] + " centimos. " )


if __name__ == '__main__':
    producto_run()