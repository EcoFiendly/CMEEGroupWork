
# Author: Ben Nouhan, bjn20@ucl.ac.uk
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
#
# ARGUMENTS
#
# filename.csv: .csv file(s) with second header "Distance.m" and third header
#               "Angle.degrees"
#
#
# RETURN
#
# NULL
#
getCSV_addTreeHeight <- function(filename.csv){
    MyData <- read.csv(filename.csv, header = TRUE)
    MyData["Tree.Height.m"] <- NA
    for (i in 1:nrow(MyData)){
        MyData[i,4] <- TreeHeight(MyData[i,3], MyData[i,2])
    }
    basename <- tools::file_path_sans_ext(basename(filename.csv))
    #tool removes extension, basename() removes filepath
    new_fpath <- paste("../results/",basename,"_treeheights.csv", sep = "")
    write.csv(MyData, new_fpath)
    return (NULL)
}



term_args <- commandArgs(trailingOnly = TRUE); csv_count <- 0

for (i in term_args){
    if (endsWith(i, ".csv") & file.exists(i)){ # Checks i exists and is a .csv
        # Checks the table in i is compatible with getCSV_addTreeHeight()
        header_check <- read.csv(i, header = FALSE)
        if (toString(header_check[1,2]) == "Distance.m" &
            toString(header_check[1,3]) == "Angle.degrees"){
                csv_count <- csv_count + 1
                getCSV_addTreeHeight(i); cat("Finished converting", i, "\n")

        } else {
            (cat(paste(i, "is incompatible. The second header must be",
            "'Distance.m' and the third header 'Angle.degrees'\n")))
        }
    } else {
        (cat(i, "is not an existing .csv file; please enter a .csv file", "\n"))
    }

}

if (length(term_args) == 0 || csv_count == 0) { # If no file converted or argued
    cat("No appropriate .csv file entered, using default: ../data/trees.csv\n")
    getCSV_addTreeHeight("../data/trees.csv")
    cat("Finished converting ../data/trees.csv\n")
}





#     Write a Unix shell script called run_get_TreeHeight.sh that tests 
#     get_TreeHeight.R. Include trees.csv as your example file. Note that source will
#      not work in this case as it does not allow scripts with arguments to be run; 
#      you will have to use Rscript instead.

#NOTE FROM BEN    showcase the checks you've made in the shell script?
