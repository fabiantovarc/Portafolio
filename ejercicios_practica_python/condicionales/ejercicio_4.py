"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
def run():
    num = int(input("Ingrese el numero: "))
    result = num % 2 #El simbolo de % entrega el sobrante de la operacion
    if result == 0 :
        print("Es par ")
    else:
        print("Es impar: ")

if __name__ == '__main__':
    run()