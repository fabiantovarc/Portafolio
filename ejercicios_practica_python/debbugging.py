# def divisors(num):
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     return divisors


# def run():
#     while True:
#         try:
#             num = int(input('Ingresa un número: '))
#             if num < 0:
#                 raise ValueError
#             print(divisors(num))
#             print("Terminó mi programa")
#             break
#         except ValueError:
#             print("Debes ingresar un entero positivo")


# if __name__ == '__main__':
#     run()

# vamos a utilizar  los assert statements
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un numero"
    assert num < 0, "Debes ingresar un numero positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")
    


if __name__ == '__main__':
    run()


