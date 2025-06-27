import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import scipy as sp

x = np.linspace(0, 10, 100)
y = 3 * x + 2 + np.random.normal(0, 1, 100)


def lineare(x,a,b):

    return x*a+b

def fit_line(x,y):

    fit,_=sp.optimize.curve_fit(lineare,x,y)
    pred=lineare(x,*fit)

    a,b=fit

    stringa=f'y={a}. * x + {b}'
    return a,b,stringa

a,b,stringa= fit_line(x,y)
print(stringa)

y_pred=lineare(x,a,b)

plt.scatter(x,y)
plt.plot(x,y_pred,'r-')
plt.show()