# Author: Group 4
# Script: PP_Regress_loc.R
# Created: Nov 2020
#
# Script draws and saves a pdf of regression analysis using data subsetted by
# the Predator.lifestage field and writes the accompanying regression results to
# a formatted table in csv in the results directory

# clear out workspace
rm(list = ls())

require(tidyverse)

# load data
df <- read.csv("../data/EcolArchives-E089-51-D1.csv")

# convert masses in mg to g
for (i in 1:nrow(df)) {
  if (df$Prey.mass.unit[i] == "mg") {
    df$Prey.mass.unit[i] <- "g"
    df$Prey.mass[i] <- df$Prey.mass[i] / 1000
  }
}

linregc <- df %>%
    #reduce dataset, group by desired factors
    dplyr::select(Predator.mass, Prey.mass, Predator.lifestage, Type.of.feeding.interaction, Location) %>%
    group_by(Type.of.feeding.interaction, Predator.lifestage, Location) %>%
    #filter out too small datasets and those with identical predator masses
    filter(length(unique(Predator.mass)) > 1 & n() > 2) %>%
    # lm calculation and store calculations to a dataframe
    do(mod = lm(log(Predator.mass) ~ log(Prey.mass), data = .)) %>%
    mutate(Regression.slope = summary(mod)$coeff[2],
           Regression.intercept = summary(mod)$coeff[1],
           R.squared = summary(mod)$adj.r.squared,
           F.statistic = summary(mod)$fstatistic[1],
           p.value = summary(mod)$coeff[8]) %>%
# remove mod column
dplyr::select(-mod)
# write to csv
write.csv(linregc, "../results/PP_Regress_Results2.csv")