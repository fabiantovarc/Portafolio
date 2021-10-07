"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""

"""
def correo_electronico():

    correo = str(input(" Ingrese el correo electronico: "))
    #El index da el numero de posicion de la palabra
    arroba = correo.index("@")
    #una vez sacado el numero se recomienda aumentar una cifra
    print(correo[0:arroba+1] + "ceu.es" )




if __name__ == '__main__':
    correo_electronico()
"""

def correo_electronico1():

    correo = str(input(" Ingrese el correo electronico: "))
    print(correo[:correo.find("@")] + "@ceu.es" )

if __name__ == '__main__':
    correo_electronico1()