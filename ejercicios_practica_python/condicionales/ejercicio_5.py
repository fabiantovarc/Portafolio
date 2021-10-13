"""
 Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
 iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al 
 usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.   
"""
def run():

    age = int(input("Ingresa tu edad: "))
    money = int(input("Ingresa el valor del ingreso mensual que obtines: "))

    if age >= 18 and money >= 1000: 
        print("Cumples con los requisitos para tributar ")
    else:
        print("No puedes tributar ")
"""

    if age >= 18:
        print("Cumples con la edad requerida para tributar")
        if money >= 1000:
            print("Tienes ingresos requerida para tributar")
        else:
            print("No tienes los ingresos necesarios para tributar")
    else:
        print("No cumples con la condicion de ser mayor de edad para tributar")

"""
if __name__ == '__main__':
    run()