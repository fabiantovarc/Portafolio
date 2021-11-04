def run():
    "Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."
    eco = " "
    while eco != "salir":
        eco = input("Ingrese cualquier palabra o frase: ")
        print(eco)


if __name__ == '__main__':
    run()