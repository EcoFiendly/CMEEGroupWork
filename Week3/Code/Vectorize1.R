# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: Vectorize1.R
# Created: Oct 2020
#
# This script demonstrates vectorization, where it is an apporach which directly
# applies compiled, optimized code to run an operation on a vector, matrix or a
# higher-dimensional data structure (like an R array), instead of performing the
# operation element-wise on the data structure
#
# ARGUMENTS:
# a vector, matrix or higher-dimensional data structure
#
# OUTPUT
# time taken to sum with a written loop and sum with inbuilt sum()

M <- matrix(runif(1000000), 1000, 1000)

SumAllElements <- function(M) {
    Dimensions <- dim(M)
    Tot <- 0
    for (i in 1:Dimensions[1]) {
        for (j in 1:Dimensions[2]) {
            Tot <- Tot + M[i, j]
        }
    }
    return(Tot)
}

print("Using loops, the time taken is:")
print(system.time(SumAllElements(M)))

print("Using the in-built vectorized function, the time taken is:")
print(system.time(sum(M)))