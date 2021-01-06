# Author: Group 4
#
# Script: get_TreeHeight.R
#
# Desc: Reads argued .csv file(s) for data frame, adds blank 4th column, uses
#       columns 2 & 3 to calculate tree heights to populate 4th column, then
#       writes new dataframe into a new .csv file
#
# Arguments:
# .csv file(s) with second header "Distance.m" and third header "Angle.degrees", 
# or none to use default.
#
# Output:
# ../results/[argument basename]_treeheights.csv
#
# Date: 27 Oct 2020

### This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
#
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
#
# RETURN
#
# height:    The heights of the tree, same units as "distance"
#
TreeHeight <- function(degrees, distance){
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    return (height)
}

### This function gets the datagrame from the argued .csv file, creates a 4th
# column, uses TreeHeight() to populate this column with treeheights using
# columns 2 & 3, then writes the expanded dataframe into a custom-named .csv
# file in ../results/
#
# ARGUMENTS
#
# filename.csv: .csv file(s) with second header "Distance.m" and third header
#               "Angle.degrees"
#
# RETURN
#
# NULL

getCSV_addTreeHeight <- function(filename.csv){
    MyData <- read.csv(filename.csv, header = TRUE)
    MyData["Tree.Height.m"] <- NA
    MyData[,4] <- TreeHeight(MyData[,3], MyData[,2])
    basename <- tools::file_path_sans_ext(basename(filename.csv))
    #tool removes extension, basename() removes filepath
    new_fpath <- paste("../Results/",basename,"_treeheights.csv", sep = "")
    write.csv(MyData, new_fpath)
    return (NULL)
}

# creates list of command arguments
term_args <- commandArgs(trailingOnly = TRUE); csv_count <- 0

### Performs a series of checks on the input
for (i in term_args){
    if (endsWith(i, ".csv") & file.exists(i)){ # Checks i exists and is a .csv
        # Checks the table in i is compatible with getCSV_addTreeHeight()
        header_check <- read.csv(i, header = FALSE)
        if (toString(header_check[1,2]) == "Distance.m" &
            toString(header_check[1,3]) == "Angle.degrees"){
                csv_count <- csv_count + 1
                getCSV_addTreeHeight(i); cat("Finished converting", i, "\n")
        # Checks the columns contain the right data type
        } else {
            (cat(paste(i, "is incompatible. The second header must be",
            "'Distance.m' and the third header 'Angle.degrees'\n")))
        } #check file exists and has csv extension
    } else {
        (cat(i, "is not an existing .csv file; please enter a .csv file", "\n"))
    }
}

# no file entered or no compatible csvs entered, uses default
if (length(term_args) == 0 || csv_count == 0) { # If no file converted or argued
    cat("No appropriate .csv file entered, using default: ../Data/trees.csv\n")
    getCSV_addTreeHeight("../Data/trees.csv")
    cat("Finished converting ../Data/trees.csv\n")
}