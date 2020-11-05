#!/bin/env python3

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

""" Script that calculates height of trees from csv file"""
__author__ = 'Maddalena Cella mc2820@ic.ac.uk'
__appname__= 'get_Treeheight.py'
__version__ = '0.0.1'
__license__= 'None'
#input
import sys
import csv
import math

Trees = [] #initiate an empty list
with open(sys.argv[1], 'r') as f:
    for line in f:
        row= line.strip().split(",") #strip() removes white spaces at the beginning or end of a string; split() separates with delimiter ","
        Trees.append(row)
f.close()

""" function that calculates heights of trees given distance of each tree from its base and angle to its top"""
def TreeHeight(degrees, distance):
    radians = math.radians(degrees)
    height = distance * math.tan(radians)
    return (height)


#add a new column to the list where the tree height is stored
Trees[0].append("\"Tree.Height.m\"") #add column header
for i in range(1, len(Trees)): #for every item in Trees (1 to the end)
    height= TreeHeight(float(Trees[i][2]), float(Trees[i][1]))
    Trees[i].append(height)

#output
#open an empty file called as ../Results/trees_treeheights.csv and fill it up with the Trees list converted into csv

with open(str("../Results/" + sys.argv[1].split("/")[2].split(".")[0] + "_treeheights.csv"), "w") as f2:
    for ele in Trees:
        f2.write(ele[0] + ',' + ele[1] + ',' + ele[2] + ',' + str(ele[3]) + '\n') #need to convert it int string because write concatenate just strings!!!
f2.close() 

