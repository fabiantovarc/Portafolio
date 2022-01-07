
class FiguraGeometrica:
    alto = int
    ancho = int

    def __init__(self, alto, ancho):
        if self._validar_valor(alto):
            self._alto   = alto
        else:   #validacion de prueba por si el usuario manda valores superiores a los que no se esperan recibir
            self._alto   = 0
            print(f"valor erroneo {self._alto}")
        if self._validar_valor(ancho):
            self._ancho   = ancho
        else:   #validacion de prueba por si el usuario manda valores superiores a los que no se esperan recibir
            self._ancho = 0
            print(f"valor erroneo {self._ancho}")

        
    @property # decorador para convertir un metodo en propiedad (getter)
    def alto(self):
        return self._alto # se puede agregar una funcion para mostrar los valores y terminos de una persona
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
             self._alto = alto # se puede agregar una funcion para mostrar los valores y terminos de una persona
        else:
            print(f"Valor erroneo {self._alto}")
        

    """ set y get de ancho"""
    @property # decorador para convertir un metodo en propiedad (getter)
    def ancho(self):
        return self._ancho # se puede agregar una funcion para mostrar los valores y terminos de una persona

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
             self._ancho = ancho # se puede agregar una funcion para mostrar los valores y terminos de una persona
        else:
            print(f"Valor erroneo {self._ancho}")

    def mostrar_detalles(self):
        print(f"Alto: {self._alto}, Ancho: {self._ancho}")

    def __del__(self):
        print(f"Alto: {self._alto}, Ancho: {self._ancho}")


    def __str__(self):
        return f"Figura geometrica:[Alto {self._alto}, Ancho {self._ancho}]"

    def _validar_valor(self,valor ): # solo se debe usar en esta clase
        return True if 0 < valor < 10 else False # el valor que se recibe solo se permite que este entre 0 a 100



if __name__ == '__main__':

    persona1 = FiguraGeometrica(40, 20)
    persona1.alto = 40
    print(persona1.alto)

    persona1.ancho = 20
    print(persona1.ancho)


    persona1.mostrar_detalles()
    print(__name__)