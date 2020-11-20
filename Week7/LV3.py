#!/usr/bin/env python3

""" Script to itteritively calculate resource and consumer data using a discrete-time prey density dependent Lotka-Volterra model, and plot the result

"""

__author__ = 'Ben Nouhan'
__version__ = '0.0.1'

import sys
import scipy as sc
import matplotlib.pylab as p


def CRtplus1(pops, t):
    """
    Itteritively calculates, using every past generation (t) and each additional value of R and C, the consumer and resource population of each subsequent generaion.

    Parameters:

    pops - a scipy array with R0 and C0 values in a row
    t - a sequence of timesteps, specified in the main function

    Returns:

    N - a scipy array with calculated R and C values of a generation in each row, with len(t) number of rows. 

    """

    ### Set parameters here
    K = 32 #goes crazy over 33; true value must be ~33.1
    if len(sys.argv) == 5:
        r, a = float(sys.argv[1]), float(sys.argv[2])
        z, e = float(sys.argv[3]), float(sys.argv[4])
    else:
        r, a, z, e = 1., 0.1, 1.5, 0.75
    
    ### Initialize Array
    N = sc.zeros((len(t), 2))
    N[0, ] = pops

    ### Loop year to year, populating array
    for yr in range(1, len(t)):
        N[yr,0] = N[yr-1,0] * (1 + r*(1 - N[yr-1,0]/K) - a*N[yr-1,1])
        N[yr,1] = N[yr-1,1]*(1-z+e*a*N[yr-1,0])
    return N


def main(argv):
    """
    Generates random data using specified parameters, effectively integrates from first principles and saves plots as PDFs
    """

    
    ### Integration (from first principles)
    t = sc.linspace(0, 50, 500)
    R0 = 10
    C0 = 5 #drops immediately and never recovers, unlike LV2
    RC0 = sc.array([R0, C0])
    pops = CRtplus1(RC0, t)
    
    ### Plotting pop density over time
    f1 = p.figure()
    p.plot(t, pops[:,0], 'g-', label='Resource density')
    p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
    p.grid()
    p.legend(loc='best')
    p.xlabel('Time')
    p.ylabel('Population density')
    p.title('Consumer-Resource population dynamics')
    if len(sys.argv) == 5:
        p.text(5/9*len(t), 6/7*max(pops[:,0:1]), "r="+sys.argv[1]+", a="+sys.argv[2]+", z="+sys.argv[3]+", e="+sys.argv[4])
    else:
        p.text(5/9*len(t), 6/7*max(pops[:,0:1]), "r=1.0, a=0.1, z=1.5, e=0.75")
    f1.savefig('../results/LV3a.pdf')
    print("Final predator and prey populations are", round(pops[len(t)-1,1],2), "and", round(pops[len(t)-1,0],2), "respectively.")
    
    ### plotting Comsumer density by resource density
    f2 = p.figure()
    p.plot(pops[:, 0], pops[:, 1], 'r-', label='Resource density')  # Plot
    p.grid()
    p.xlabel('Resource density')
    p.ylabel('Consumer density')
    p.title('Consumer-Resource population dynamics')
    #p.show()# To display the figure
    f2.savefig('../results/LV3b.pdf'); p.close('all')
    
    return None
        
if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
