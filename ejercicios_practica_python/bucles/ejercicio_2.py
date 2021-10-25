"""
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def run():

    num = int(input("Ingrese un numero entero positivo: "))
    if num > 0:
        for i in range(1, num+1, 2):
            print(i, end=", ")# "end=" lo que hace es implementar al final de la impresion de "I" una variable asignada
    else:
        print("El numero ingresado no es correcto. Intentalo nuevamente. ")


if __name__ == '__main__':
    run()