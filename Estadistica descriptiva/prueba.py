def run():
    import csv
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import seaborn as sns
    
    arch = "2015.csv"
    with open(arch, newline="" ) as f:
        datos = csv.reader(f)
        
        paises = list(id)
        
    print("El tipo de datos de la lista paises es:", type(paises))
"""""
    df = pd.read_csv('2015.csv')
    sns.scatterplot(data = df, x = "Economy (GDP per Capita)", y = "Happyness Score")
    plt.show()"""
    
if __name__ == '__main__':
    run()