"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
funcione cuando el día o el mes se introduzcan con un solo carácter.
"""


def fechas_run():
    date = input("Ingresa la fecha de nacimiento con este formato dd/mm/aaaa: ")
    dia = date[:date.find("/")]
    meses = date[date.find("/")+1:]
    mes = meses[:meses.find("/")]
    año = meses[meses.find("/")+1:]
    print(" dia " + dia + " mes " + mes + " año " + año)


if __name__ == '__main__':
    fechas_run()


    