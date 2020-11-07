# Runs the stochastic Ricker equation with gaussian fluctuations


#__author__ = 'Billy Lam (ykl17@ic.ac.uk)'
#__version__ = '3.6.3'

#Clear
rm(list=ls())

#Original function
stochrick<-function(p0=runif(1000,.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{
  #initialize
  N<-matrix(NA,numyears,length(p0))
  N[1,]<-p0
  
  for (pop in 1:length(p0)){#loop through the populations
    
    for (yr in 2:numyears){ #for each pop, loop through the years

      N[yr,pop] <- N[yr-1,pop] * exp(r * (1 - N[yr - 1,pop] / K) + rnorm(1,0,sigma))
    
    }
  
  }
 return(N)

}
print(system.time(stochrick()))



# Now write another function called stochrickvect that vectorizes the above 
# to the extent possible, with improved performance: 

stochrickvect <- function(p0=runif(1000,.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{
  #initialize
  N<-matrix(NA,numyears,length(p0))
  N[1,]<-p0
  
  for (x in 1:length(p0)){#loop through the populations
    
    c(head(x, -1)) * exp(r * (1 - c(head(x, -1)) / K) + rnorm(1,0,sigma))
    
    
  }
  return(N)
  
}
# An alternative attempt with sapply, didn't work
  #try1 <- sapply(N, function(x) c(head(x, -1)) * exp(r * (1 - c(head(x, -1)) / K) + rnorm(1,0,sigma)))
  #return(try1)


print("Vectorized Stochastic Ricker takes:")
print(system.time(res2<-stochrickvect()))
