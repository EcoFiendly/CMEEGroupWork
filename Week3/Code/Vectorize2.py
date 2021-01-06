#!/usr/bin/env python3

"""
This script is the translated version of Vectorize2.R
"""

__author__ = 'Group 4'
__version__ = '0.0.1'

import numpy as np
import time

def stochrick(p0 = np.random.uniform(.5, 1.5, 1000), r = 1.2, K = 1, sigma = 0.2, numyears = 100):
    """
    Runs the stochastic Ricker equation with gaussian fluctuations

    Parameters:
        p0 (array): initial population density
        r (float): intrinsic growth rate
        K (float): carrying capacity of the environment
        sigma (float): environmental process noise s.d.
        numyears (integer): number of years to loop over

    Returns:
        N (array): density of population after a number of generations
    """
    # initialize
    N = np.zeros((numyears, len(p0)))
    N[0, ] = p0

    # loop  through the populations
    for pop in range(0, len(p0)):
        # for each pop, loop through the years
        for yr in range(1, numyears):
            N[yr, pop] = N[yr - 1, pop] * np.exp(r * 1 - N[yr -1, pop] / K) + np.random.normal(0, sigma, 1)
    return N

# Now write another function called stochrickvect that vectorizes the above
# to the extent possible, with improved performance:
def stochrickvect(p0 = np.random.uniform(.5, 1.5, 1000), r = 1.2, K = 1, sigma = 0.2, numyears = 100):
    """
    Runs the stochastic Ricker equation with gaussian fluctuations

    Parameters:
        p0 (array): initial population density
        r (float): intrinsic growth rate
        K (float): carrying capacity of the environment
        sigma (float): environmental process noise s.d.
        numyears (integer): number of years to loop over

    Returns:
        N (array): density of population after a number of generations
    """
    # initialize
    N = np.zeros((numyears, len(p0)))
    N[0, ] = p0

    # loop through all populations together by year
    for yr in range(1, numyears):
        N[yr, ] = N[yr - 1, ] * np.exp(r * (1 - (N[yr - 1, ] / K))) + np.random.normal(0, sigma, size = 1)

    return N

# time stochrick
start = time.time()
stochrick()
end = time.time()
print("Non-vectorized Stochastic Ricker takes:")
print(end - start)

# time stochrickvect
start = time.time()
stochrickvect()
end = time.time()
print("Vectorized Stochastic Ricker takes:")
print(end - start)