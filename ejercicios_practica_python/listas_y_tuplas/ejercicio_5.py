"""
ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
def run():
    list  = [1,2,3,4,5,6,7,8,9,10]
    list.reverse()
    for i in range(len(list)):
        print(list[i], end=', ')
    print()

if __name__ == '__main__':
    run()