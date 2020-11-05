#!/usr/bin/env python3

"""Python script to calculate the sum of all the cells in a matrix"""
__author__ = 'Maddalena Cella (mc2820@ic.ac.uk)'
__version__ = '0.0.1'

import numpy as np
#M <- matrix(runif(1000000),1000,1000)
M= np.arange(1,1000001).reshape(1000,1000) #creates a matrix of 1000x1000 of numbers from 1 to 1 million

result = np.sum (a=M) #adds up all the cells in the matrix
print (result)
