import random
def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("elije un numero aleatorio: "))
    while numero_aleatorio != numero_elegido:
        if numero_elegido < numero_aleatorio:
            print(" busca un numero mas grande")
        else:
            print(" busca un numero mas pequeño")
        numero_elegido = int(input (" elije otro numero: "))
    print(" ganaste")
    
if __name__ == '__main__':
    run()