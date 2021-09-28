def conversor(valor,nacionalidad):
    pesos = input("¿Cuantos pesos " + nacionalidad + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")    

opcion = input("""

## CONVERSOR DE MONEDAS ##

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

""")
if opcion == '1':
    conversor(3600,'colombianos')
elif opcion == '2':
    conversor(85,'argentinos')
elif opcion == '3':
    conversor(24,'mexicanos')
else:
    print('Ingrese una opción valida')