#no funciona

# def run():
#     i = 0
#     operacion = 2**2+i
#     print(operacion)
#     for i in range(0,1000):
#         if operacion == 1000:
#             print(operacion+ " operacion finalizada")
#         else:
#             print(operacion)
# if __name__=='__main__':
#     run()


def run():
    LIMITE = 1000000
    contador = 1
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a "+ str(potencia_2))
        contador = contador + 1 
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()