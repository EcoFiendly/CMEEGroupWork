#!/usr/bin/env python3

"""
This script runs the discrete-time version of the Lotka-Volterra model and plots
the results in two graphs saved to ../Results.
"""

__author__ = 'Group 4'
__version__ = '0.0.1'

# imports
import numpy as np
import scipy.integrate as integrate
import matplotlib.pylab as p
import sys

# define time vector, integrate from time point 0 to 15, using 1000
# sub-divisions of time
# note that units of time are arbitrary here
t = np.linspace(0, 15, 1000)

# set initial conditions for two populations (10 resources and 5 consumers per 
# unit area), and convert the two into an array (because our dCR_dt function
# takes an array as input)
R0 = 10
C0 = 5

# set K, which is the carrying capacity
K = 33

def main(r = 1.0, a = 0.1, z = 1.5, e = 0.75):
    """
    Calculates the population density at each time step using the discrete-time
    version of the Lotka-Volterra model
    Plots the results in two graphs saved to ../Results/. 
    First, a change in resource and consumer density over time, and second, the 
    change in population density of consumer with respect to the change in 
    population density of resource
    
    Parameters:
        r (float): intrinsic (per-capita) growth rate of the resource 
                   population (time ^ -1)
        a (float): per-capita "search rate" for the resource
                   (area x time ^ -1) multiplied by its attack success
                   probability, which determines the encounter and 
                   consumption rate of the consumer on the resource
        z (float): mortality rate (time ^ -1)
        e (float): consumer's efficiency (a fraction) in converting 
                   resource to consumer biomass
    """
    RC = np.zeros([len(t),2]) # preallocate list
    RC[0, :] = np.array([R0, C0]) # fill the first row with starting conditions

    # discrete time version of LV model
    for i in range(0, len(t) - 1):
        # fill first column with R population at each time step
        RC[i + 1, 0] = RC[i, 0] * (1 + r * (1 - RC[i, 0] / K) - a * RC[i, 1])
        # fill second column with C population at each time step
        RC[i + 1, 1] = RC[i, 1] * (1 - z + e * a * RC[i, 0])
    
    # visualize with matplotlib
    f1 = p.figure()
    p.plot(t, RC[:,0], 'g-', label = "Resource density") # plot
    p.plot(t, RC[:,1], 'b-', label = "Consumer density")
    p.grid()
    p.legend(loc = "best")
    p.xlabel("Time")
    p.ylabel("Population density")
    p.suptitle("Consumer-Resource population dynamics")
    p.title("r = %.2f, a = %.2f, z = %.2f, e = %.2f" %(r, a, z, e),
        fontsize = 8)
    # p.show()
    f1.savefig("../Results/LV_model3.pdf") # save figure

    # plot of Consumer density against Resource density
    f2 = p.figure()
    p.plot(RC[:,0], RC[:,1], 'r-')
    p.grid()
    p.xlabel("Resource density")
    p.ylabel("Consumer density")
    p.suptitle("Consumer-Resource population dynamics")
    p.title("r = %.2f, a = %.2f, z = %.2f, e = %.2f" %(r, a, z, e),
        fontsize = 8)
    # p.show()
    f2.savefig("../Results/LV_model3-1.pdf")

if __name__ == "__main__":
    main()
    sys.exit()