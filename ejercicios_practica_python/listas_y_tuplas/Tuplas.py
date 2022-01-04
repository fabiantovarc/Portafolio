def run():
    tupla = (13, 1, 8, 3, 2, 5, 8)
    lista = []
    for elemento in tupla:
        if elemento < 5:
            lista.append(elemento)
    print(lista)
if __name__ == '__main__':
    run()