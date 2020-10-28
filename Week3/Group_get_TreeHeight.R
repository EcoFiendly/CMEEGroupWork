#Language: R
#Auther: Cong Liu (cong.liu20@imperial.ac.uk)
#Script: get_TreeHeight.R
#Work Path: CMEECourseWork/Week3
#Input: Data/trees.csv
#Function: Calculate heights of trees given distance of each tree 
#          from its base and angle to its top, using  the trigonometric formula 
#Output: Results/trees_treeheights.csv
#Usage: Rscript get_TreeHeight.R [Input]
#Date: Oct, 2020

args = commandArgs(trailingOnly = T)

data = read.csv(args, header = T)
a = nrow(data)

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  return (height)
}

Tree.Height.m = c()
for ( i in 1:a ){
  distance = as.numeric(data$Distance.m[i])
  degree = as.numeric(data$Angle.degrees[i])
  height = TreeHeight(degree, distance)
  Tree.Height.m[i] = height 
}

data_more = data.frame(data, Tree.Height.m)

inputfile = unlist(strsplit(args, split = "/"))[2]

inputfilename = unlist(strsplit(inputfile, split = ".csv"))[1]


e = paste("Results/", inputfilename, sep = "")
e = paste(e, "_treeheights.csv", sep = "")
write.csv(data_more, e, row.names = F)