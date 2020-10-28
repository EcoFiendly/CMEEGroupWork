"""Language: Python3
   Auther: Cong Liu (cong.liu20@imperial.ac.uk)
   Script: Vectoriza2.py
   Work Directory: CMEECourseWork/Week3
   Dependencies: time, numpy
   Input:
   Function: Compare te efficiency of Pyton and R
   Output:
   Usage: python Vectorize2.py
   Date: Oct, 2020"""
import time
start = time.time()

import numpy as np

# Run the stochastic Ricker equation with gaussian fluctuations
def function(p0, r, k, sigma, numyears):
    """Description: Stochastic Ricker model with gaussian fluctuations
       
       Input variables:
       p0: a list composed of densities or sizes of initial populations
       r: a float represents instrinct growth rate
       k: a float represents capasity
       sigma: a float represents standard error of fluctuations
       numyears: a integer represents number of generations
       
       Output: An array. The columns represents the growth process of a population,
               and the rows represent the densities or sizes of populations in certain generation."""
    M = np.empty(shape = [numyears, len(p0)])
    M[0] = p0
    for i in range(0, len(p0)):
        for j in range(0, numyears - 1):
            fluc = float(np.random.normal(0, sigma, 1))
            b = r*(1-float(M[j,i])/k)
            a = np.exp(b)
            M[j + 1, i] = float(M[j, i])*a + fluc
    return M

p0 = np.random.uniform(low = 0.5, high = 1.5, size = 1000)
r = 1,2
k = 1
sigma = 0.2
numyears = 100
Result = function(p0,1.2,1,0.2,100)
print(Result)

end = time.time()

print("Running time of Vectorize2.py: " + str(end - start))