#!/usr/bin/env python3

"""Vectorize1 script in python codes"""

__appname__ = 'oaks.py'
__author__ = 'Billy Lam (ykl17@ic.ac.uk)'
__version__ = '0.0.1'

import time
import numpy as np

#M <- matrix(runif(1000000),1000,1000)
M = np.random.rand(1000, 1000)

start = time.time()

summm = np.sum(M)

print(suummm)

end = time.time()

print("The time taken to sum all is:")
print(end - start)
