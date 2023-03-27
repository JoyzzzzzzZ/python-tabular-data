#! /usr/bin/env python3

"This is a module to perform linear regression for petal length and setal length of different iris species."

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def iris_lr(species):
    '''
    Draw a linear regression plot for sepal length vs petal length of a given iris species.

    Parameters
    ----------
    species : str
        A string representing the iris species name.

    Returns
    -------
    None
    '''
    df=pd.read_csv("iris.csv")
    df_sub=df[df.species==species]
    x=df_sub.petal_length_cm
    y=df_sub.sepal_length_cm
    regression=stats.linregress(x,y)
    slope=regression.slope
    intercept=regression.intercept
    plt.scatter(x, y, label='Data')
    plt.plot(x, slope * x + intercept, color="orange", label='Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("sepal_v_petal_length_regress_" + species + ".png")

def main():
    iris_lr('Iris_setosa')
    iris_lr('Iris_virginica')
    iris_lr('Iris_versicolor')

if __name__ == '__main__':
    main()
