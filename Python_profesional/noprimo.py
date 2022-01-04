def es_primo(num: int):
    result = [x for x in range(2,num) if num % x == 0]
    result_final = len(result) == 0
    if result_final == True:
        print(f"El numero {num} es primo")
    else:
        print(f"El numero {num} no es primo. Es divisible por {result}")

def run():
    variable = int(input("Ingrese un numero: "))
    if variable >= 0:
        es_primo(variable)

if __name__ == "__main__":
    run()