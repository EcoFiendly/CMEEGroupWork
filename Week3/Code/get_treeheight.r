#!/bin/env Rscript


#read input
args<- commandArgs(trailingOnly=TRUE)
Trees <- read.csv(args, header = TRUE)


TreeHeight <- function(degrees, distance){
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    return (height)
}

Trees$Tree.Height.m <- TreeHeight(Trees$Angle.degrees, Trees$Distance.m)

#output
strip_csv <- tools::file_path_sans_ext(basename(args[1]))
write.csv(Trees, paste("../results/", strip_csv, "_treeheights.csv", sep="")) 