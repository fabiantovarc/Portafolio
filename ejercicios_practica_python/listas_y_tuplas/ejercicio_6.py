#Escribir un programa que pida al usuario una palabra 
#y muestre por pantalla el número de veces que contiene cada vocal.

def contador_vocales(palabra):
    vocales = {"a","e","i","o","u"}
    contador = 0
    for i in palabra: #recorro la palabra
        if i in vocales: #si el caracter es una vocal
            contador += 1 #sumo 1 al contador
    return contador #retorno el contador
    

#Programa Principal

def main():
    
    pala = str(input("Ingrese una plabra: "))
    palabra = pala.lower()
    contador = contador_vocales(palabra)
    #print(contador) por si quiero ver el contador en pantalla
    print(f"""
    La palabra: {palabra}  
    a = {palabra.count("a")}    
    e = {palabra.count("e")}
    i = {palabra.count("i")}
    o = {palabra.count("o")}
    u = {palabra.count("u")}
    tiene {contador} vocales
    """)

if __name__ == "__main__":
    main()