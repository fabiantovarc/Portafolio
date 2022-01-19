from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))


empleado1 = Empleado("Daniel", 3000)
imprimir_detalles(empleado1)


gerente1 = Gerente("karla",5000 , "Software")
imprimir_detalles(gerente1)



