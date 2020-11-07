#!/bin/env Rscript

# Author: Maddalena Cella (mc2820@ic.ac.uk)
#
# Script: get_TreeHeight.R
#
# Description: this script calculates the tree height for all trees in the trees.csv data set using the trigonometric formula:
# height = distance * tan(radians) and stores the results in a .csv output file
#
# Arguments: 1-> input file fom command line (trees.csv). trees.csv downloaded from https://raw.githubusercontent.com/mhasoba/TheMulQuaBio/master/content/data/trees.csv
# and stored in the ../data/ directory
#
# Input: Rscript get_TreeHeight.R trees.csv
#
# Output: trees_treeheights.csv stored in ../Results/ directory 
#
# Date: October 2020

#read input
args<- commandArgs(trailingOnly=TRUE)
Trees <- read.csv(args, header = TRUE)

## function that calculates heights of trees given distance of each tree from its base and angle to its top

## ARGUMENTS
## degrees: angle of elevation of tree (degrees)
## distance: distance from base of tree (meters)

## OUTPUT
## Height of the tree (meters)

TreeHeight <- function(degrees, distance){
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    return (height)
}

Trees$Tree.Height.m <- TreeHeight(Trees$Angle.degrees, Trees$Distance.m)

#output
strip_csv <- tools::file_path_sans_ext(basename(args[1]))
write.csv(Trees, paste("../results/", strip_csv, "_treeheights.csv", sep="")) 