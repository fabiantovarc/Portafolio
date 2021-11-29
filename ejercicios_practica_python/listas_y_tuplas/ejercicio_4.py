# ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista 
#y los muestre por pantalla ordenados de menor a mayor.
import random

def ejercicio_4():
    #ejercicio 4
    my_list = []

    for i in range(4):
        my_list.append(int(input("Introduce un número ganador: ")))
    
    my_list.sort()
    print(f"Los números ganadores son {my_list}")
    return my_list

def my_list():
    #ejercicio planteado
    #generar de manera aleatoria los numeros ganadores y ingresarlo a una listasYTuplas
    list = [] 
    
    for i in range(10): # "N" numeros ganadores
        list.append(random.randint(0, 9999)) #generar numeros aleatorios rango de 0 a 9999
    print(f"Los números ganadores son {list}")# Imprime el mensaje con los numeros ganadores
    list.sort() #Organizar los numeros de menor a mayor
    
    return list


#generar un indice que contenga los dos ejercicios
#ejecutar el indice
menu ="""
###INDICE###

1) Ejercicio 4
2) Ejercicio planteado
salir (Escribir salir)

"""
    
while True:
    print(menu)
    opcion = input("Elige una opción: ")
    if opcion == "1":
        ejercicio_4()
    elif opcion == "2":
        my_list()
        
    elif opcion == "salir":
        print("Adios")
        break
    else:
        print("Opcion no valida")
        continue
    

if __name__ == '__main__':
    my_list()