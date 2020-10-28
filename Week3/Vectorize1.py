"""Language: Python3
   Auther: Cong Liu (cong.liu20@imperial.ac.uk)
   Script: Vectoriza1.py
   Work Directory: CMEECourseWork/Week3
   Dependencies: time, numpy
   Input:
   Function: Compare te efficiency of Pyton and R
   Output:
   Usage: python Vectorize1.py
   Date: Oct, 2020"""
import time
start = time.time()

import numpy as np

#Create a 1000*1000 zero-array
M = np.empty(shape=[1000, 1000])

#Each value in M is from a uniform distribution of [0,1).
for i in range(0, 1000):
    row = np.random.uniform(0,1, size = 1000)
    M[i] = row

#Sum all elements in M
su = np.sum(M)

print(su)

end = time.time()

print("Running time of Vectorize1.py: " + str(end - start))
