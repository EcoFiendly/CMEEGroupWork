## Groupwork

##
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")

## Data inspection
unique(MyDF$Type.of.feeding.interaction) #5
unique(MyDF$Predator.lifestage) #6
unique(MyDF$Location) #25


## Function to extract regression results
fun1<-function(x){
  res<-c(x$coefficients[1],
         x$coefficients[2],
         summary(x)$r.squared,
         summary(x)$fstatistic)
         #pf(summary(x)$fstatistic[1],summary(x)$fstatistic[2],
            #summary(x)$fstatistic[3],lower.tail=FALSE))
  names(res)<-c("intercept","slope","r.squared")
              
  return(res)}   


## Nested for loop
trial <- list()
trial2 <- list()
for(y in unique(MyDF$Type.of.feeding.interaction)){
  feed <- subset(MyDF, Type.of.feeding.interaction == y)

  for(l in unique(feed$Predator.lifestage)){
    predator <- subset(feed, Predator.lifestage == l)
    
    for(x in unique(predator$Location)){
      locatt <- subset(predator, Location == x)
      
      j <- assign(paste("lm",y, l, x, sep = " "), lm(Prey.mass ~ Predator.mass, locatt))
      trial2[[x]] <- assign(paste("aov",y, l, x, sep = " "), anova(lm(Prey.mass ~ Predator.mass, locatt))$"Pr(>F)"[1])
      
      #show many lms created
      #print(paste("Created lm", sep = "")) 
      
      trial[[x]] <- assign(paste("result",y, l, x, sep = " "), fun1(j))
      
      #assign(paste(y, l, x, sep = " ")) <- cbind(c, a)
    }
  }
}

### Data wrangling
trial <- as.data.frame(trial)
trial <- t(trial)
trial2 <- as.data.frame(trial2)
trial2 <- t(trial2)

trial3 <- cbind(trial, trial2)
trial3 <- as.data.frame(trial3)

# Renaming and removing columns
trial3 <- trial3[, -c(5,6)]

names(trial3)[names(trial3) == "V1"] <- "Intercept"
names(trial3)[names(trial3) == "V2"] <- "Slope"
names(trial3)[names(trial3) == "V3"] <- "R.squared"
names(trial3)[names(trial3) == "V4"] <- "F-statistics"
names(trial3)[names(trial3) == "V7"] <- "P-value"

# Export
write.csv(trial3,"../Results/PP_Regress_loc_Results.csv")