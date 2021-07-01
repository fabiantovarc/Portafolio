"""
fibonaci
def fibonnaci(n):
    print(n)
    if n == 0 or n == 1:
        return 1
    return fibonnaci (n - 1) + fibonnaci(n - 2)

if __name__ == '__main__':
    fibonnaci()"""
""" ejemplo de funciones dentro de otras funciones

def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

    nums = [1, 2, 3]
    aplicar_operacion(multiplicar_por_dos, nums)
    aplicar_operacion(sumar_dos, nums)
"""
def tupla_my():
    my_tupla = ("coño", "joder", "lo vamos a lograr")
    x, y ,z = my_tupla
    print(my_tupla)
    print(x,y,z)


if __name__ == '__main__':
    tupla_my()

