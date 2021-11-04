def run():
#Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

    
    password_user = input("Ingrese la contraseña: ")
    password = "contraseña"
    while password_user != password:
        password_user = input("Ingrese nuevamente la contraseña: ")    

if __name__ == '__main__':
    run()