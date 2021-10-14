def run():
    print("""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

        Renta	                Tipo impositivo
    Menos de 10000€	                5%
    Entre 10000€ y 20000€	        15%
    Entre 20000€ y 35000€	        20%
    Entre 35000€ y 60000€	        30%
    Más de 60000€	                45%

Escribir un programa que pregunte al usuario su renta anual
y muestre por pantalla el tipo impositivo que le corresponde.
    """)
    renta = float(input("Ingrese cual es su ingreso mensual en euros: "))

    if renta < 10000:
        print(renta * 5 /100)
    elif renta >= 10000 and renta <= 20000:
        print(renta * 15 /100)
    elif renta >= 20000 and renta <= 35000:
        print(renta * 20 /100)
    elif renta >= 35000 and renta <= 60000:
        print(renta * 30 /100)
    elif renta > 60000:
        print(renta * 45 /100)


if __name__ == '__main__':
    run()