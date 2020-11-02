# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: Vectorize2.R
# Created: Oct 2020
#
# Runs the stochastic Ricker equation with gaussian fluctuations
#
# ARGUMENTS
# p0 = initial population density
# r = intrinsic growth rate
# K = carrying capacity of the environment
# sigma = environmental process noise s.d.
# numyears = number of years to loop over
#
# OUTPUT
# density of population after a number of generations

# clears workspace
rm(list = ls())

stochrick <- function(p0=runif(1000, .5, 1.5), r = 1.2, K = 1, sigma = 0.2,
                      numyears = 100) {

    #initialize
    N <- matrix(NA, numyears, length(p0))
    N[1, ] <- p0

    # loop through the populations
    for (pop in 1:length(p0)) {

        # for each pop, loop through the years
        for (yr in 2:numyears) {
            N[yr, pop] <- N[yr - 1, pop] * exp(r * (1 - N[yr - 1, pop] / K) +
            rnorm(1, 0, sigma))
        }
    }
    return(N)
}

# Now write another function called stochrickvect that vectorizes the above
# to the extent possible, with improved performance:
stochrickvect <- function(p0=runif(1000, .5, 1.5), r = 1.2, K = 1, sigma = 0.2,
                          numyears = 100) {

    # initialize N, 100 years x 1000 populations
    N <- matrix(NA, numyears, length(p0))
    # p0 is the starting number across all populations
    N[1, ] <- p0
    # how to vectorize
    # can vectorize across all populations, but not within the populations
    # this is because all populations are independent
    # but within populations, there is dependency, N(t + 1) comes from N(t)
    for (yr in 2:numyears) {
        # by leaving N[, pop] blank, it lets the function work across all pop
        # at once
            N[yr, ] <- N[yr - 1, ] * exp(r * (1 - N[yr - 1, ] / K) +
            rnorm(1, 0, sigma))
        }
    # can skip looping through populations one by one, figure out how to apply
    # the equation across all populations at once
    return(N)
}

print("Non-vectorized Stochastic Ricker takes:")
print(system.time(res1 <- stochrick()))
print("Vectorized Stochastic Ricker takes:")
print(system.time(res2 <- stochrickvect()))