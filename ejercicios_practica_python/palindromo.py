def palindromo(palabra):
    #estamos remplazando los espacios para que no tenga espacio
    #por ejemplo en este palindromo  LUZ AZUL el computador 
    # no lee ese espacio, por lo mismo necesitamos quitar ese espacio con
    #palabra.replace
    palabra = palabra.replace(" ", "")
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()