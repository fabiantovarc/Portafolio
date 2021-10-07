"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número 
de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

"""

def run():

    print("Escriba el numero de telefono con el siguiente formato +34-913724710-56 : ")
    numero = (str(input("prefijo-número-extension, maximo 9 digitos sin contar la extension y el prefijo : ")))
    numeros = numero[4:-3]
    print("El numero de telefono es "+ numeros)


if __name__ == '__main__':
    run()