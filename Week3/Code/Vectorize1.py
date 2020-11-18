#!/usr/bin/env python3

"""Python script to calculate the sum of all the cells in a matrix"""
__author__ = 'Maddalena Cella (mc2820@ic.ac.uk)'
__version__ = '0.0.1'

import time
import numpy as np
#M <- matrix(runif(1000000),1000,1000)
M= np.arange(1,1000001).reshape(1000,1000) #creates a matrix of 1000x1000 of numbers from 1 to 1 million

start=time.time()
def SumAllElements(M):
    """function that calculates the sum of all the cells in a matrix"""
    sum=0
    for col in range(0,len(M[0])): #from 0 to 1000
        for row in range(0,len(M)):
            sum= sum + M[row,col]
    return sum
SumAllElements(M)
end=time.time()
print("The non vectorised function takes:")
print(end-start)

start=time.time()
np.sum(M) #adds up all the cells in the matrix
end=time.time()
print("The vectorised function takes:")
print(end-start)

