texto1 = ("Bienvenido")
texto2 = ("Convertidor de moneda de dolares a pesos Colombianos")
print (texto1)
print (texto2)
dolares = int(input("Ingrese los dolares: "))
dolares = float(dolares)
valor_pesos = 0.28
dolares = dolares / valor_pesos 
dolares = round(dolares, 2)
dolares = str(dolares)
print ("Tines $ " + dolares + " en pesos colombianos")