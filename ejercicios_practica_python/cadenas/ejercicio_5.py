"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

def run():

    frase = str(input("Introduzca una frase: "))
    vocal = str(input("Introduzca una vocal: "))

    print(frase.replace(vocal, vocal.upper()))


if __name__ == '__main__':
    run()