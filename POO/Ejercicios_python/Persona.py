class Persona:

    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        #self.valores = valores
        #self.terminos = terminos

    
    @property # decorador para convertir un metodo en propiedad (getter)
    def nombre(self):
        #print("llamando metodo get nombre")
        return self._nombre # se puede agregar una funcion para mostrar los valores y terminos de una persona
    
    @nombre.setter
    def nombre(self, nombre):
        #print("llamando metodo set nombre") 
        self._nombre = nombre # se puede agregar una funcion para mostrar los valores y terminos de una persona
        

    @property # decorador para convertir un metodo en propiedad (getter)
    def apellido(self):
        #print("llamando metodo get nombre")
        return self._apellido # se puede agregar una funcion para mostrar los valores y terminos de una persona
    
    @apellido.setter
    def apellido(self, apellido):
        #print("llamando metodo set nombre") 
        self._apellido = apellido # se puede agregar una funcion para mostrar los valores y terminos de una persona

    @property # decorador para convertir un metodo en propiedad (getter)
    def edad(self):
        #print("llamando metodo get nombre")
        return self._edad # se puede agregar una funcion para mostrar los valores y terminos de una persona
    
    @edad.setter
    def edad(self, edad):
        #print("llamando metodo set nombre") 
        self._edad = edad # se puede agregar una funcion para mostrar los valores y terminos de una persona

    def mostrar_detalles(self):
        print(f"Persona: {self._nombre}, {self._apellido}, {self._edad}")
    
    def __del__(self):
        print(f"Persona: {self._nombre}, {self._apellido}")

if __name__ == '__main__':
    persona1 = Persona("juan", "Perez", 28)
    persona1.nombre = 'Pedro Gonzales'
    print(persona1.nombre)

    persona1.apellido = "Fernandez"
    print(persona1.apellido)

    persona1.edad = 30
    print(persona1.edad)


    persona1.mostrar_detalles()
    print(__name__)



"""
persona1 = Persona("Juan ", "Perez", 24, "44553322" , 2, 3, 5, m="manzana", p = "pera")
persona1.mostrar_detalles()
 
persona2 = Persona("Ana", "Suarez", 21)
persona2.mostrar_detalles()
 """
