"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas.
"""
def run():
    #Se implementa con la variable comprobar un ciclo bucle para que inicie correctamente el programa
    comprobar = True

    while comprobar == True:

        

        num = int(input("Ingrese un numero entero positivo: "))

        if num > 0:
            comprobar = False

            for i in range(num): #tambien se puede implementar con range(num, -1, -1)

                print(num-i, end=", ")

        else:

            print("El numero ingresado no es correcto. Intentalo nuevamente. ")

if __name__ == '__main__':
    run()