class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas +=1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona [ID: {self.id_persona}, Nombre: {self.nombre}, Edad: {self.edad}]"


persona1 = Persona("David", 30)
print(persona1)
persona2 = Persona("Maria", 21)
perosna3 = Persona("Henry", 32)
print(f"Valor contador Personas {Persona.contador_personas}" )