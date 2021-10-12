"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""

def condicional():

    edad = int(input("¿Cuál es tu edad?: "))
    if edad < 18: 
        print ("Eres menor de edad")
    else:
        print("Eres mayor de edad")


if __name__ == '__main__':
    condicional()