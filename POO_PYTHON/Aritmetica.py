class Aritmetica:
    """
    clase aritmetica para realizar las operaciones
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA   = operandoA
        self.operandoB   = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5,3)
print(f"resta: {aritmetica1.restar()}")
print(f"sumar: {aritmetica1.sumar()}")
print(f"multiplicar: {aritmetica1.multiplicar()}")
print(f"dividir: {aritmetica1.dividir():.2f}")