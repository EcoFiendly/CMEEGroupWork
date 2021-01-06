# Author: Group 4
# Script: PP_Regress.R
# Created: Nov 2020
#
# Script draws and saves a pdf of regression analysis using data subsetted by
# the Predator.lifestage field and writes the accompanying regression results to
# a formatted table in csv in the results directory

# clear out workspace
rm(list = ls())

require(tidyverse)
require(broom)

# load data
df <- read.csv("../Data/EcolArchives-E089-51-D1.csv")
dplyr::glimpse(df)

# convert masses in mg to g
for (i in 1:nrow(df)){
  if (df$Prey.mass.unit[i] == "mg"){
    df$Prey.mass.unit[i] <- "g"
    df$Prey.mass[i] <- df$Prey.mass[i] / 1000
  }
}

# calculate the regression
linreg <- df %>%
          group_by(Type.of.feeding.interaction, Predator.lifestage, Location) %>%
          do(tidy(lm(log(Predator.mass) ~ log(Prey.mass), .)))

# linreg returns:
# piscivorous postlarva/juvenile Antarctic Peninsula log(Prey.mass) NA NA NA NA
# planktivorous juvenile Gulf of Alaska log(Prey.mass) 1.689114e-01 NaN NaN NaN

# change Type of feeding interaction and Predator lifestage into factors
df$Type.of.feeding.interaction <- as.factor(df$Type.of.feeding.interaction)
df$Predator.lifestage <- as.factor(df$Predator.lifestage)
df$Location <- as.factor(df$Location)
# subset the corresponding factors which produced NA and NaN results
ss1 <- df[which(df$Type.of.feeding.interaction == "piscivorous" &
                df$Predator.lifestage == "postlarva/juvenile" &
                df$Location == "Antarctic Peninsula"), ]
ss2 <- df[which(df$Type.of.feeding.interaction == "planktivorous" &
                df$Predator.lifestage == "juvenile" &
                df$Location == "Gulf of Alaska"), ]
ss3 <- df[which(df$Type.of.feeding.interaction == "predacious" &
                 df$Predator.lifestage == "adult" &
                 df$Location == "Gulf of Maine, New England"), ]
ss4 <- df[which(df$Type.of.feeding.interaction == "piscivorous" &
               df$Predator.lifestage == "juvenile" &
               df$Location == "Off the Bay of Biscay"), ]

linregb <- df %>%
  # filtering entries found in the above subsets
  filter(!Record.number %in% c(30914, 30929, 277, 321)) %>%
  # select columns required and group by feeding type, predator lifestage and
  # location
  dplyr::select(Predator.mass, Prey.mass, Predator.lifestage,
                Type.of.feeding.interaction, Location) %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage, Location) %>%
  # lm calculation and store calculations to a dataframe
  do(mod = lm(log(Predator.mass) ~ log(Prey.mass), data = .)) %>%
  mutate(Regression.slope = summary(mod)$coeff[2],
         Regression.intercept = summary(mod)$coeff[1],
         R.squared = summary(mod)$adj.r.squared,
         F.statistic = summary(mod)$fstatistic[1],
         p.value = summary(mod)$coeff[8]) %>%
  # remove mod column
  dplyr::select(-mod)

# linreg b row 34 error: essentially perfect fit: summary may be unreliable
# subset the corresponding factors which produced the error
ss3<- df[which(df$Type.of.feeding.interaction == "predacious" &
                 df$Predator.lifestage == "adult" &
                 df$Location == "Gulf of Maine, New England"), ]

linregc <- df %>%
  # filtering entries found in the above subsets
  # filter(!Record.number %in% c(30914, 30929, 277, 321, 2204, 2221, 2222, 2223,
  #                             2224)) %>%
  # select columns required and group by feeding type, predator lifestage and
  # location
  dplyr::select(Predator.mass, Prey.mass, Predator.lifestage,
                Type.of.feeding.interaction, Location) %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage, Location) %>%
  filter(n() > 2) %>%
  # lm calculation and store calculations to a dataframe
  do(mod = lm(log(Predator.mass) ~ log(Prey.mass), data = .)) %>%
  mutate(Regression.slope = summary(mod)$coeff[2],
         Regression.intercept = summary(mod)$coeff[1],
         R.squared = summary(mod)$adj.r.squared,
         F.statistic = summary(mod)$fstatistic[1],
         p.value = summary(mod)$coeff[8]) %>%
  # filter(summary(mod)$adj.r.squared == 1) %>%
  # remove mod column
  dplyr::select(-mod)

write.csv(linregc, "../Results/PP_Regress_Results.csv")