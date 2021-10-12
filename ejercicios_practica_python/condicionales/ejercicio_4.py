"""
Escribir un programa que pida al usuario dos números y muestre por 
pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""

def run():

    print("Se realizara una division, ingrese los dos siguientes cifras. ")



    num_1 = int(input("Ingrese el primer numero: "))
    #primera condicional
    if num_1 == 0:
        print("Ocurrio un error, no se puede dividir por 0")
    else:
        num_2 = int(input("Ingrese el segundo numero: "))
        #segunda condicional
        if num_2 == 0:
            print("Ocurrio un error, no se puede dividir por 0")
        else: 
            print(num_1/num_2)
    



if __name__ == '__main__':
    run()