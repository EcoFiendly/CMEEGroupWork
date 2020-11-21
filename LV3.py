#!/usr/bin/env python3

"""The discrete time version of the Lotka-Volterra model for a predator-prey system in 2D space"""

__appname__ = 'LV3.py'
__author__ = 'Billy Lam (ykl17@ic.ac.uk)'
__version__ = '0.0.1'

# imports
import sys
import numpy as np
import scipy.integrate as integrate
import matplotlib.pylab as p

# check whether there are input arguments, if not use default parameters
if len(sys.argv) <5:
    print("There are no input for model parameters, we will use defaults values")
    r=1
    a=0.1
    z=1.5
    e=0.75
else:
    print("Using the input parameters for the LV model")
    r = float(sys.argv[1]) 
    a = float(sys.argv[2]) 
    z = float(sys.argv[3]) 
    e = float(sys.argv[4]) 

# Time vector
t = np.linspace(0, 15, 1000)

# Initial conditions
R0 = 10
C0 = 5
K = 32

# Preallocate, two columns
popu = np.zeros((len(t),2))

# For loop
for yr in range(len(t)): 

    Rn = R0 * (1 + r * (1- R0/K) - a * C0)
    Cn = C0 * (1 - z + e * a * R0)
    R0 = Rn
    C0 = Cn
    popu[yr,:]= [Rn,Cn]

# #
f1 = p.figure()
p.plot(t, popu[:,0], 'g-', label = "Resource density") 
p.plot(t, popu[:,1], 'b-', label = "Consumer density")
p.grid()
p.legend(loc = "best")
p.xlabel("Time")
p.ylabel("Population density")
p.title("r = %.2f, a = %.2f, z = %.2f, e = %.2f" %(r, a, z, e))
p.suptitle("Consumer resource population dynamics")

#p.show()

f1.savefig("../results/LV_model3a.pdf") # save figure

# #
f2 = p.figure()
p.plot(popu[:,0], popu[:,1], 'r-', color = 'blue')
p.grid()
p.xlabel("Resource density")
p.ylabel("Consumer density")
p.title("r = %.2f, a = %.2f, z = %.2f, e = %.2f" %(r, a, z, e))
p.suptitle("Consumer-Resource population dynamics")

#p.show()

f2.savefig("../results/LV_model3b.pdf"