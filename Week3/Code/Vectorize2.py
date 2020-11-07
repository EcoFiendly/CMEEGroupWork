#!/usr/bin/env python3

"""Vectorize1 script in python codes"""

__appname__ = 'oaks.py'
__author__ = 'Billy Lam (ykl17@ic.ac.uk)'
__version__ = '0.0.1'

import time
import numpy as np

def stochrickvect(p0 = np.random.uniform(0.5, 1.5, 1000), r = 1.2, K = 1, sigma = 0.2, numyears = 100):
    """ 
    """
    N = np.zeros((numyears, 1000))
    N[1, ] = p0
    for years in range(numyears):
        N[years, ] = N[years - 1, ] * np.exp(r * (1 - (N[years - 1, ] / K))) + \
            np.random.normal(0, sigma, size = len(p0))
    return N

start = time.time()
stochrickvect()
end = time.time()

print("The running time of stochrickvect is:")
print(end -start)