"""
pide al usuario un numero y encuentra los divisores del numero
"""
def divisors(num):
    divisors = []
    for i in range(1, num + 1): # range(1, num + 1) es un rango de 1 a num + 1
        if num % i == 0: # si el residuo de num / i es 0
            divisors.append(i) # agrega i a divisors
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "debes ingresar un número" # assert es una condicion que se cumple o no
    print(divisors(int(num)))
    print("Termino mi programa")
    

if __name__ == '__main__':
    run()
