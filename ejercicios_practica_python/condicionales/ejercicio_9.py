"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""

def run():
    
    precio = 5
    
    edad = int(input("¿Cual es tu edad?: "))

    if edad <= 4:
        print("En hora buena! las personas menores de 4 años ingresan gratis")
        print("precio de la entrada es $0")
    elif edad >= 5 and edad <= 18:
        print("Los mayores de 4 años pagan su entrada ")
        print(f"El precio de entrada es {precio}€")
    else:
        print("Los mayores de 4 años pagan su entrada ")
        print(f"El precio de entrada es {precio* 2}€")


if __name__ == '__main__':
    run()