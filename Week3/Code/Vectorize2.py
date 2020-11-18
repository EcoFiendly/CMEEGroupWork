# This script contains two functions (one vectorised and one not) and aims to compare their runtime. 
# Both functions give the expected number (or density) Nt+1 of individuals in generation 
# t+1 as a function of the number of individuals in the previous generation t when stochasticity is added
#
# ARGUMENTS
# None
#
# INPUT
# None
#
# OUTPUT
# time it takes for the non-vectorised and vectorised functions stochrick and stockrickvect to run

#packages needed
import numpy as np
import time #to calculate runtime

def stochrick(p0= np.random.uniform(0.5,1.5,1000), r=1.2, K=1, sigma=0.2, numyears=100): 
    """function that applies the stochastic Ricker equation to some populations

        parameters:
          p0= initial population density (allows gaussian fluctuations)
          r= intrisic growth rate
          K= carrying capacity of the population
          sigma= environmental process noise 
          numyears= number of generations over which the equation is run

        output:
        N= density of population after numyears """

    N= np.zeros((numyears, len(p0)))
    N[1,] = p0
    for pop in range(0,len(p0)):
        for year in range(1,numyears): #for all populations, loop through the years
            N[year,pop]= N[year-1,pop] * np.exp(r * (1 - N[year - 1,pop] / K) + np.random.normal(0,sigma,1)) #rnorm[number of,mean,var] vs np.random.normal(mean,SD, size)
    return N

def stochrickvect(p0= np.random.uniform(0.5,1.5,1000), r=1.2, K=1, sigma=0.2, numyears=100):
    """function that applies the stochastic Ricker equation to some populations

        parameters:
          p0= initial population density (allows gaussian fluctuations)
          r= intrisic growth rate
          K= carrying capacity of the population
          sigma= environmental process noise 
          numyears= number of generations over which the equation is run

        output:
        N= density of population after numyears """

    N= np.zeros((numyears, len(p0)))
    N[1,] = p0
    for year in range(numyears): #for all populations, loop through the years
        N[year,]= N[year-1,] * np.exp(r * (1 - N[year - 1,] / K) + np.random.normal(0,sigma,1)) #rnorm[number of,mean,var] vs np.random.normal(mean,SD, size)

    return N

#compare runtime of non-vectorised and vectorised function
start= time.time()
stochrick()
end=time.time()
print("Time taken for the non-vectorised function to run:")
print(end-start)

startv=time.time()
stochrickvect()
endv=time.time()
print("Time taken for the vectorised function to run:")
print(endv-startv)


