
import numpy as np
import scipy as sp
import matplotlib.pyplot as ptl

x = np.linspace(0, 10, 100)
y = 3 * x + 2 + np.random.normal(0, 1, 100)

def lineare(x,a,b):

    return a*x+b

def fit_line(x,y):

   fit,_=sp.optimize.curve_fit(lineare,x,y)

   a,b=fit

   pred=lineare(x,*fit)
   
   stringa= f'La stringa è: {float(a)} * x + {float(b)}'
   return float(a),float(b),stringa

a,b,stringa=fit_line(x,y)

pred=a*x+b
ptl.plot(x,y,'r-')
ptl.plot(x,pred,'b-')
ptl.show()