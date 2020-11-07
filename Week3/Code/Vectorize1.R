#__author__ = 'Billy Lam (ykl17@ic.ac.uk)'
#__version__ = '3.6.3'

## Vectorization example

# Sums all elements of a matrix
M <- matrix(runif(1000000),1000,1000)

SumAllElements <- function(M){
  Dimensions <- dim(M)
  Tot <- 0
  for (i in 1:Dimensions[1]){
    for (j in 1:Dimensions[2]){
      Tot <- Tot + M[i,j]
    }
  }
  return (Tot)
}


# Shows sum() is much faster than sumallelements() because it uses vectorization
print("Using loops, the time taken is:")
print(system.time(SumAllElements(M))) #system.time calculates code efficiency

print("Using the in-built vectorized function, the time taken is:")
print(system.time(sum(M)))
