#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés 
#separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras 
#y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no
#está en el diccionario debe dejarla sin traducir.

def main():
    dict = { "paciente": " pacient", "pactar": " agree ",
    "carro": " car", "avion": " plane",
    "bicicleta": " bicycle "}
    
    word = input("Ingrese la palabra: ")
    #valor = dict.get(word)
    value = dict.values() 
    
    print(dict[word, value])
    #print(dict[value])





if __name__ == '__main__':
    main()