"""
Created on Tue Oct  5 16:18:54 2021

@author: fabian
"""
"""librerias"""
#from openpyxl import Workbook
#from openpyxl import load_workbook

"""creacion de archivo"""
#wb = Workbook()
#wb.save("excel_prueba.xlsx")

#wb2 = load_workbook("excel_prueba.xlsx")

"""creacion de hojas"""
#ws1 = wb2.create_sheet("hoja2")
#ws2 = wb2.create_sheet("hoja3")

""" cambio de nombre de las hojas"""
#ws = wb2["Sheet"]
#ws.title = "hoja1"


#wb2.save("excel_prueba.xlsx")

def run():
    
   miarchivo = open('C:\\Users\\rexcu\\Desktop\\Portafolio\\Estadistica_descriptiva\\dataset_practicing\\prueba_1.csv', 'r')
   lectura = miarchivo.readline()

   
   
   print(lectura)


if __name__ == '__main__':
   run()