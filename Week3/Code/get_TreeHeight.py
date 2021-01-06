#!/usr/bin/env python3

"""
This script is the translated version of get_TreeHeight.R
"""

__author__ = 'Group 4'
__versin__ = '0.0.1'

import sys
import numpy as np

# translate sys.argv to open file
inpu = sys.argv[1]
file = open(inpu, "r")

# initialize empty list
data = []
# append lines from file to list
for line in file:
    line = line.strip().split(",")
    data.append(line)
file.close()

def TreeHeight(degrees, distance):
    """
    This function calculates heights of trees given distance of each tree from
    its base and angle to its top, using the trogonometric formula

        Parameters:
            degrees (int): the angle of elevation of tree
            distance (int): the distance from base of tree (e.g. meters)

        Returns:
            height (int): height of trees, same units as "distance"
    """
    radians = degrees * np.pi / 180
    height = distance * np.tan(radians)

    return(height)

# add tree heights column to list
data[0].append("Tree.Height.m")
# loop through data to calculate heights and add to column
for i in range(1,len(data)):
    height = TreeHeight(float(data[i][1]), float(data[i][2]))
    data[i].append(height)

# set name of output file
result_name = "../Results/" + inpu.split("/")[1].split(".")[0] + "_treeheights.csv"
result = open(result_name, "w")
# write to results
for i in data:
    result.write(i[0]+","+i[1]+","+i[2]+","+str(i[3]))
    result.write("\n")

result.close()