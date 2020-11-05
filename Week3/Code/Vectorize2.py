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

rm(list=ls())

stochrick<-function(p0=runif(1000,.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{
  #initialize
  N<-matrix(NA,numyears,length(p0))
  N[1,]<-p0
  
  for (pop in 1:length(p0)){#loop through the populations: for every pop in row 1
    
    for (yr in 2:numyears){ #for each pop, loop through the years

      N[yr,pop] <- N[yr-1,pop] * exp(r * (1 - N[yr - 1,pop] / K) + rnorm(1,0,sigma))
    
    }
  
  }
 return(N)

}

print("Stochastic Ricker takes:")
print(system.time(res1<-stochrick()))

# Now write another function called stochrickvect that vectorizes the above 
# to the extent possible, with improved performance: 

def stochrickvect():
    p0,r=1.2,K=1,sigma=0.2,numyears=100 #runif() generates random deviates from a min of .5 to a max of 1.5
    for x in range(1000):
        p0 = random.uniform (0.5, 1.5)
'''
r =1.2
K= 1
sigma = 0.2
numyears =100 #check what type of variable is numyears!!

import random
p0 = [] #generates random deviates from a min of .5 to a max of 1.5
for i in range (0,1000):
    x = random.uniform(0.5,1.5)
    p0.append(x)
    print (p0)
return(p0)

import numpy as np
N=[] with rows being numyears and columns being p0

for i in N[0:]:#loop through the populations
    
    for y in N[:i]: #for each pop, loop through the years

        N[yr,pop]= N[yr-1,pop] * exp(r * (1 - N[yr - 1,pop] / K) + rnorm(1,0,sigma))
    
    }
  
  }
 return(N)

