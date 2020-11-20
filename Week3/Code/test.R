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

rm(list=ls())

library(broom)

#Import data
data = read.csv("../data/EcolArchives-E089-51-D1.csv")

#Convert mg to g
for (row in 1:nrow(data)) {
  if (data[row, 14] == "mg") {
    data[row, 14] <- "g"
    data[row, 13] <- data[row, 13] / 1000 }
}

FeedType = names(table(data$Type.of.feeding.interaction))
PredatorStage = names(table(data$Predator.lifestage))
Loc = names(table(data$Location))
RegTitle = c("Slope", "Intercept", "Adjusted-R^2",
             "F-statistic", "p-value")
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
            if (nrow(d) > 2){
                n[k] = paste(i, j, l, sep="_")
                k = k + 1
                mod = unlist(summary(lm(log(d$Prey.mass)~log(d$Predator.mass))))
                a = c(mod$coeff[2], mod$coeff[1], mod$adj.r.squared, mod$fstatistic[1], mod$coeff[8])
                Reg_loc = cbind(Reg_loc, a)
                names(Reg_loc) = n } } } 
}

write.table(t(Reg_loc), col.names=FALSE, "../results/PP_Regress_loc_Results.csv")

#For combination "piscivorous", "juvenile" and "Off the Bay of Biscay",
#R-square is 0, indicating no correlation. That is why the loops output
#an error: since R-square is 0, F-test was not conducted, and
#no F statistic available. This combination is not in Reg_loc