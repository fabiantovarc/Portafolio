# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:11:18 2021
Escribir una función que reciba un diccionario con las notas de los alumnos 
en curso en un examen y devuelva una serie con la nota mínima, la máxima, 
media y la desviación típica.
@author: fabian
"""
def librerias():
    import pandas as pd

def run():

#diccionario
    my_dict = {"luisa","carlos","stiven","lucia"}  
        
#contador
    cont = 0
    
#ingreso de las variables
    for i in range(my_dict):
        
        notas = float(input("¿cual fue tu nota del examen?"))
        cont += 1
        
        return cont



if __name__ == '__main__':
    run()
