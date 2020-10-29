# Author: Yewshen Lim (y.lim20@imperial.ac.uk)
# Script: TreeHeight.R
# Created: Oct 2020
#
# This function calculates heights of trees given distance of each tree from its
# base and angle to its top, using the trigonometric formula
#
# height = distance * tan(radians)
#
# ARGUMENTS
# args: cli argument as input file
# degrees: The angle of elevation of tree
# distance: The distance from base of tree (e.ge, meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

# Take cli arguments
args <- commandArgs(trailingOnly = TRUE)

# Read trees.csv file
TreeData <- read.csv(args, header = TRUE)

TreeHeight <- function(degrees, distance) {
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    # print(paste("Tree height is:", height))

    return(height)
}

# Add output of TreeHeight for each tree to new column in TreeData
TreeData$Tree.Height.m <- TreeHeight(TreeData$Angle.degrees,
     TreeData$Distance.m)

# strip path and extension from input file
inputname <- tools::file_path_sans_ext(basename(args[1]))
# Write to output file in Results
write.csv(TreeData, paste0("../Results/", inputname, "_treeheights.csv"))