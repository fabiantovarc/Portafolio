"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""


def run():


    num= int(input("Ingrese un numero entero positivo: "))
    #range(inicio, fin, paso)
    for i in range(1, num+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ") #imprime el numero y el espacio
        print("")
                


if __name__ == '__main__':
    run()

