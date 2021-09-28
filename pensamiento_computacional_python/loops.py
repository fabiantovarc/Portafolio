# def run():
#     contador = 0
#     while contador < 10:
#         print("Imprimir", contador)
#         contador += 1
#     return contador
# if __name__ == '__main__':
#     run()

# for x in range(0, 31, 5):
#   print(x)
def run():

  objetivo = int(input("Escoge un numero: "))
  epsilon = 0.01
  paso = epsilon**2
  respuesta = 0.01

  while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
#  para simplificar los decimales se coloca round y dentro de la respuesta a imprimir se coloca (coma) y el numero a simplificar
    print(round(respuesta,4))
    print(abs(respuesta**2 - objetivo), respuesta)
  if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
  else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

if __name__ == '__main__':
  run()