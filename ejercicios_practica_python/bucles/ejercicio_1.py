"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)..
"""

def run():

    edad = int(input("Ingrese su edad: "))
    for i in range(edad):
        print(f"Has cumplido {i+1} años")
   

if __name__ == '__main__':
    run()