import numpy as np
import matplotlib.pyplot as plt
from myCubicSpline import *

# Macro function
def makeParametric( X, Y ):
    N = len(X)
    rX = myCubicSpline( np.arange( N ), X )
    rY = myCubicSpline( np.arange( N ), Y )
    return rX, rY

def plotParametric( X, Y ):
    N = len(X.X)
    for i in range(1, N):
        newx = np.linspace(i-1, i, 50)
        plt.plot( X.spline( i, newx ), Y.spline( i, newx ), '-', color='black')
