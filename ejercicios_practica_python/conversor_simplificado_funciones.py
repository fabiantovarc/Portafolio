def conversor(tipo_pesos, valor_dolar):
    print ("Pesos Colombianos")
    pesos = int(input("¿Cuantos pesos "+ tipo_pesos + " tienes? "))
    pesos = float(pesos)
    valor_dolar =  valor_dolar
    dolares = pesos / valor_dolar 
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")



menu = """ 
Bienvenido al conversor de moneda de pesos a dolares


1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Pesos Argentinos

Ingresa el numero del indice que deseas usar
"""
opcion = int(input(menu))
#condicional, estamos 
if opcion == 1:
    conversor(" colombianos", 3800)
elif opcion == 2:
    conversor(" mexicanos",19.90)
elif opcion == 3:
    conversor("argentinos", 92.94 )
else:
    print("Ingresaste un valor incorrecto")


#condicionales la primera version que aprendimos, la mas larga.

# if opcion == 1:
#     print ("Pesos Colombianos")
#     pesos = int(input("¿Cuantos pesos Colombianos tienes? "))
#     pesos = float(pesos)
#     valor_dolar =  3629
#     dolares = pesos / valor_dolar 
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("tienes $" + dolares + " dolares")
# elif opcion == 2:
#     print ("Pesos Mexicanos")
#     pesos = int(input("¿Cuantos pesos Mexicanos tienes? "))
#     pesos = float(pesos)
#     valor_dolar =  19.90
#     dolares = pesos / valor_dolar 
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("tienes $" + dolares + " dolares")
# elif opcion == 3:
#     print ("Pesos Argentinos")
#     pesos = int(input("¿Cuantos pesos Mexicanos tienes? "))
#     pesos = float(pesos)
#     valor_dolar =  93.03
#     dolares = pesos / valor_dolar 
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("tienes $" + dolares + " dolares")
# else:
#     print("Ingresaste un valor incorrecto") 