def run():
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    from mpl_toolkits.mplot3d import Axes3D

    df = pd.read_csv('C:\\Users\\rexcu\\Desktop\\Portafolio\\Estadistica_descriptiva\\dataset_world_happiness\\2016.csv')
"""
    sns.scatterplot(data = df, x = "Economy (GDP per Capita)", y = "Happiness Score")

    plt.show()
    """
    
    
if __name__ == '__main__':
    run()