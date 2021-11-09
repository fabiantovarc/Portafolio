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

if __name__ == '__main__':
    run()