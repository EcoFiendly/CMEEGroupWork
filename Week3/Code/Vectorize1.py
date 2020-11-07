#!/usr/bin/env python3

"""
This script is the translated version of Vectorize1.R
"""

__author__ = 'Group 4'
__version__ = '0.0.1'

import numpy as np
import time

M = np.random.normal(size = (1000, 1000))

def SumAllElements(M):
    """
    Sums all of the elements in a given matrix

    Parameters:
        M (matrix): any matrix

    Returns:
        Sum (float): sum of all elements in M
    """
    Sum = 0
    for i in range(0, len(M[0])):
        for j in range(0, len(M[1])):
            Sum = Sum + M[i,j]
    return Sum

# time SumAllElements
start = time.time()
SumAllElements(M)
end = time.time()
print("Using loops, time taken is:")
print(end - start)

# time sum function in numpy
start = time.time()
np.sum(M)
end = time.time()
print("Using the in-built vectorized function, the time taken is:")
print(end - start)
