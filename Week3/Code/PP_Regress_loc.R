#!/bin/env Rscript

# Author: Maddalena Cella mc2820@ic.ac.uk
# Script: PP_Regress.R
# Description: script that draws and saves a multi-panel figure as pdf, containing subplots of regressions of predator mass on prey mass for the different types of feeding interaction.
# it additionally saves a csv file with the results of the regression analyses
# Input: Rscript PP_Regress.R
# Output: 1 plot (PP_Regress.pdf) in Results directory and a csv file (PP_Regress_Results.csv) in Results directory
# Arguments:0
# Date: October 2020

rm(list=ls())

library(dplyr)
library(ggplot2)

Data <- read.csv("../Data/EcolArchives-E089-51-D1.csv", header=T)
head(Data)

#create subsets of the data by feeding types
Data_loc <- Data %>% group_by(Location)%>%
summarise(
    intercept <- summary(lm(log(Predator.mass)~log(Prey.mass)))$coefficients[1,1],
    slope <- summary(lm(log(Predator.mass)~log(Prey.mass)))$coefficients[2,1],
    rsquared <- summary(lm(log(Predator.mass)~log(Prey.mass)))$r.squared,
    fstatistic <- summary(lm(log(Predator.mass)~log(Prey.mass)))$fstatistic[1],
    pvalue <- summary(lm(log(Predator.mass)~log(Prey.mass)))$coefficients[2,4],
    .groups='drop'
)
  
#write csv with Summary in it
write.csv(Data_loc, "../Results/PP_Regress_loc_res.csv")

##MyDF.I
counter <- 0
for ( i in unique(MyDF.I$Predator.lifestage) ){
  #create a subset data 
  data_sub <- subset(MyDF.I, Predator.lifestage == i)
  
  counter <- counter + 1
  #create the linear model. If it is the first loop,
  #then the model name will be lm_ins1
  j <- assign(paste("lm_I",counter,sep = ""), lm(Prey.mass ~ Predator.mass, data_sub))

  #show many lms created
  assign(paste("lm_I", counter, sep = ""), res_linear(j))
}
##MyDF.P
counter <- 0
for ( i in unique(MyDF.P$Predator.lifestage) ){
  #create a subset data 
  data_sub <- subset(MyDF.P, Predator.lifestage == i)
  
  counter <- counter + 1
  #create the linear model. If it is the first loop,
  #then the model name will be lm_ins1
  j <- assign(paste("lm_P",counter,sep = ""), lm(Prey.mass ~ Predator.mass, data_sub))

  #show many lms created
  assign(paste("lm_P", counter, sep = ""), fun1(j))
}
##MyDF.PL
counter <- 0
for ( i in unique(MyDF.PL$Predator.lifestage) ){
  #create a subset data 
  data_sub <- subset(MyDF.PL, Predator.lifestage == i)
  
  counter <- counter + 1
  #create the linear model. If it is the first loop,
  #then the model name will be lm_ins1
  j <- assign(paste("lm_PL",counter,sep = ""), lm(Prey.mass ~ Predator.mass, data_sub))

  #show many lms created
  assign(paste("lm_PL", counter, sep = ""), fun1(j))
}
##MyDF.PR
counter <- 0
for ( i in unique(MyDF.PR$Predator.lifestage) ){
  #create a subset data 
  data_sub <- subset(MyDF.PR, Predator.lifestage == i)
  
  counter <- counter + 1
  #create the linear model. If it is the first loop,
  #then the model name will be lm_ins1
  j <- assign(paste("lm_PR",counter,sep = ""), lm(Prey.mass ~ Predator.mass, data_sub))

  #show many lms created
  assign(paste("lm_PR", counter, sep = ""), fun1(j))
}
##MyDF.PP
counter <- 0
for ( i in unique(MyDF.PP$Predator.lifestage) ){
  #create a subset data 
  data_sub <- subset(MyDF.PP, Predator.lifestage == i)
  
  counter <- counter + 1
  #create the linear model. If it is the first loop,
  #then the model name will be lm_ins1
  j <- assign(paste("lm_PP",counter,sep = ""), lm(Prey.mass ~ Predator.mass, data_sub))

  #show many lms created
  
  assign(paste("lm_PP", counter, sep = ""), fun1(j))
}

# bind by columns
resh <- cbind(lm_I1, lm_P1, lm_P2, lm_P3, lm_P4, lm_P5, lm_PL1, lm_PL2, lm_PL4,
             lm_PL5, lm_PR1, lm_PR2, lm_PR3, lm_PR4, lm_PR5, lm_PR6, lm_PP1)
# name the columns
colnames(resh)<- c("lm_I1", "lm_P1", "lm_P2", "lm_P3", "lm_P4", "lm_P5", "lm_PL1", "lm_PL2", "lm_PL4",
             "lm_PL5", "lm_PR1", "lm_PR2", "lm_PR3", "lm_PR4", "lm_PR5", "lm_PR6", "lm_PP1")
final <- data.frame(t(resh))[,-c(5:6)] #transpose the results so that the regression outputs are the columns and the models are the rows, remove df and variance column

#write csv with Summary in it
write.csv(final, "../Results/PP_Regress_Results.csv")