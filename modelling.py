import numpy as np
def gaus(x,A,B,C):
    """
    This is a 3-param gaussian
    """
    return A * np.exp( -(x-B)**2 / (2*C**2))
