"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
    como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""
def run():
    comprobar = True

    while comprobar == True:

        num= int(input("Ingrese un numero entero positivo: "))

        if num > 0:

            for i in range(num):
                comprobar = True
                
                #print(i)
                print("*"*(i+1))#lo que sucede aqui es que la "i" inicializa en 0, entonces le suma 1 y se multiplica las veces
                                #que se repite el string

        else:

            print("El numero ingresado no es correcto. Intentalo nuevamente. ")



if __name__ == '__main__':
    run()