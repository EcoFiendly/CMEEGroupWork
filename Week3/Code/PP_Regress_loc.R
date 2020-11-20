#!/bin/env Rscript

# Author: Maddalena Cella mc2820@ic.ac.uk
# Script: PP_Regress.R
# Description: script that draws and saves a multi-panel figure as pdf, containing subplots of regressions of predator mass on prey mass for the different types of feeding interaction.
# it additionally saves a csv file with the results of the regression analyses
# Input: Rscript PP_Regress.R
# Output: 1 plot (PP_Regress.pdf) in Results directory and a csv file (PP_Regress_Results.csv) in Results directory
# Arguments:0
# Date: October 2020

rm(list = ls())

#Import data
data = read.csv("../Data/EcolArchives-E089-51-D1.csv")

FeedType = names(table(data$Type.of.feeding.interaction))
PredatorStage = names(table(data$Predator.lifestage))
Loc = names(table(data$Location))

RegTitle = c("slope", "intercept", "adjusted-R^2", 
             "F-statistic", "p-value")
library(broom)
#Summary of linear model
lmSum = function(a,b){
  c = rep(NA, 5)
  mol = lm(a~b)
  sum = unlist(summary(mol))
  c[1] = sum$coefficients2
  c[2] = sum$coefficients1
  c[3] = sum$adj.r.square
  c[4] = sum$fstatistic.value
  c[5] = unname(glance(mol)$p.value)
  return(c)
}

Reg_loc = data.frame(RegTitle)
n = names(Reg_loc)
k = 2 #because the first item is RegTitle
for (i in FeedType){
  for (j in PredatorStage){
    for (l in Loc){
      d = subset(data,
                 data$Type.of.feeding.interaction == i &
                  data$Predator.lifestage == j &
                   data$Location == l)
      if (nrow(d) >2){
        n[k] = paste(i,j,l,sep = "_")
        k = k + 1
        mod= unlist(summary(lm(log(Predator.mass) ~ log(Prey.mass), data)
        a = c(summary(mod)$coeff[2], summary(mod)$coeff[1],
         summary(mod)$adj.r.squared, summary(mod)$fstatistic[1],
         summary(mod)$coeff[8])
        Reg_loc = cbind(Reg_loc, a)
      names(Reg_loc) = n
      }
    }
  }
}
Reg_loc
#For combination "piscivorous", "juvenile" and "Off the Bay of Biscay",
#R-square is 0, indicating no correlation. That is why the loops output
#an error: since R-square is 0, F-test was not conducted, and 
#no F statistic available. This combination is not in Reg_loc
write.csv(t(Reg_loc),"../Results/PP_Regress_loc_Results.csv")
  