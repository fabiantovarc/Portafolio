def run():
    print("""
    1) Contraseña y validacion de la misma
    2) Identificador de edad
    3) Indice corporal de grasa 
    4) Division (muestra en pantalla el resultado cosiente y residuo)
    5) Contador de impuesto
    """)
    contador = 1
    menu = int(input("Ingresa el indice que deseas ingresar: "))
    while menu ==1:
        
        while contador <=3:
            password = str(input("Ingrese la contraseña: "))
            validacion = str(input("Ingrese nuevamente la contraseña: "))
        if password == validacion:
            print("las dos contraseñas coinciden")
            print("Proceso completado")
            contador = 4
        else:
            print("Las contraseñas no coinciden")
            print("Ingrese nuevamente las contraseñas")
            contador += 1
            return


    if menu == 2:
        edad = int(input("Ingresa la edad: "))
        if edad < 18:
            print ("Eres menor de edad")
        else:
            print("Eres mayor de edad")


            
    if menu == 3:
        print("Bienvenido a los ejercicios interactivos de Fabian")
        peso_inicial = float(input("Ingresa el perso en KG: "))
        estatura_inicial = float(input("Ingresa la estatura en metros: "))
        grasa = round(peso_inicial/(estatura_inicial/100),2)
        print("Tu indice corporal de grasa es: " + str(grasa))
        """
        Utilizamos round para poder dar formato al float 
        y disminuir los decimales que salen en la respuesta.
        """  



    if menu == 4:
        n = input("Introduce el dividendo (entero): ")
        m = input("Introduce el divisor (entero): ")
        print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))



    if menu == 5:
        inversion = float(input("Ingresa la cantidad a invertir: "))
        años = int(input("Ingresa el numero de años: "))
        interes = float(input("Ingresa el interes anual: "))
        print(round(inversion * (interes /100+1) ** años, 2))



    else:
        print("Numero demaciado alto")
        print("Ingresa nuevamente el indice")
        return




if __name__ == '__main__':
    run()
# def run():
#     squares = []
    
#     # squares = [i **2 for i in range (1, 101) if i%3 == 0]
    
#     # print(squares)
#     for i in range(1, 101):
#         if i % 3 != 0:
#         squares.append[i**2]

#     print(squares)

# if __name__ == '__main__':
#     run()