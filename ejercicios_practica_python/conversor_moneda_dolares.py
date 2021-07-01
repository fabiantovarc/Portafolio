pesos = int(input("¿Cuantos pesos colombianos tienes? "))
pesos = float(pesos)
valor_dolar =  3629
dolares = pesos / valor_dolar 
dolares = round(dolares, 2)
dolares = str(dolares)
print("tienes $" + dolares + " dolares")
