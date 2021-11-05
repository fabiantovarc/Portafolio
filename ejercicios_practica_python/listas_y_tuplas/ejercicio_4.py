"""ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista 
y los muestre por pantalla ordenados de menor a mayor.
    for i in range(4):
        my_list.append(int(input("Introduce un número ganador: ")))
    
    my_list.sort()
    print(f"Los números ganadores son {my_list}")
    #my_list.append(i)
"""
import random
def my_list(list):
   
    for i in range(4):
        list[i] = random.randint(0, 10)
    return list 
        
#list.sort()
#print(list)


if __name__ == '__main__':
    my_list()