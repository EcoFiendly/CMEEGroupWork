#Language: R
#Auther: Cong Liu (cong.liu20@imperial.ac.uk)
#Script: PP_Regress_loc.R
#Work Path: CMEECourseWork/Week3
#Dependency: ggplot2, scales
#Input: Data/EcolArchives-E089-51-D1.csv
#Function: Regress prey mass and predator mass for each 
#          Feeding Type × Predator life Stage × Location combination and
#          save results in Results/PP_Regress_loc_Results.csv
#          For each combination, if it has only two pairs of data or 
#          there is no correlation (R-square = 0), it will not be saved
#Output: Results/PP_Regress_loc_Results.csv
#Usage: Rscript PP_Regress_loc.R
#Date: Oct, 2020

rm(list = ls())

#Import data
data = read.csv("Data/EcolArchives-E089-51-D1.csv")

FeedType = names(table(data$Type.of.feeding.interaction))
PredatorStage = names(table(data$Predator.lifestage))
Loc = names(table(data$Location))

RegTitle = c("slope", "intercept", "R^2","adjusted-R^2", 
             "F-statistic", "p-value")
library(broom)
#Summary of linear model
lmSum = function(a,b){
  c = rep(NA, 6)
  mol = lm(a~b)
  sum = unlist(summary(mol))
  c[1] = sum$coefficients2
  c[2] = sum$coefficients1
  c[3] = sum$r.squared
  c[4] = sum$adj.r.square
  c[5] = sum$fstatistic.value
  c[6] = unname(glance(mol)$p.value)
  return(c)
}

Reg_loc = data.frame(RegTitle)
n = names(Reg_loc)
k = 2
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
        a = lmSum(log(d$Prey.mass), log(d$Predator.mass))
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
write.csv(Reg_loc,"Results/PP_Regress_loc_Results.csv")
