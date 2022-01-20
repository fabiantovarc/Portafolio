from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from Computadora import Computadora
from Orden import Orden


pantalla1 = Monitor("samsung",30,6000, "HDMI")
raton1 = Raton("Tipo C", "DELUX", 150000)
teclado1 = Teclado("Tipo C", "Genius", 200000)
computador1 = Computadora("Gigabyte", pantalla1, raton1, teclado1)

pantalla2 = Monitor("LG", 30 , 15000000, "HDMI")
raton2 = Raton("USB", "Logitect", 5000000)
teclado2 = Teclado("Tipo c", "Force", 500000)
computador2 = Computadora("Thermaltek", pantalla2, raton2, teclado2)

monitor3 = Monitor("Gamer", "Bluetooth", 1500000, "HDMI")
raton3 = Raton("USB", "Gamer", 5000000)
teclado3 = Teclado("Tipo c", "Gamer", 500000)
computador3= Computadora("Gamer", pantalla2, raton2, teclado2)

computadoras1 = [computador1, computador2, computador3]
orden1 = Orden(computadoras1)
print(orden1)