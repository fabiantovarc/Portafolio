#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

def main():
    list_1 = [1,2,3]
    list_2 = [-1,0,2]

    list_3 = list_2 + list_1 # juntamos las dos listas en una sola
    list_3.sort()# organizamos la lista de menor a mayor
    print(list_3)


if __name__ == '__main__':
    main()
