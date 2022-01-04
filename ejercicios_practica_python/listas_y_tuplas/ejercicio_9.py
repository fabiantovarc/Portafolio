def main():
    nombre = str(input("Ingrese el nombre del libro: "))
    precio = float(input("Ingrese el valor del libro: "))
    autor = str(input("Ingrese el nombre del autor: "))
    envio = bool(input("Ingrese si el envio es gratis (true) o no (false): "))


    if envio == True:
        print(f"""
        ID: {id(nombre)}
        Libro: {nombre.upper()}
        Autor: {autor.upper()} 
        Precio: ${precio}
        envio: Gratis

        Gracias por su compra
        """)
        print("")
    else:
        print(f"""

        Libro: {nombre.upper()} 
        Autor: {autor.upper()} 
        Precio: ${precio}
        envio: $10.000 

        Gracias por su compra
        """)
if __name__ == '__main__':
    main()