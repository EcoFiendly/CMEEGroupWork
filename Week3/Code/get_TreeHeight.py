#!/usr/bin/env python3

"""
This script is the translated version of get_TreeHeight.R
"""

__author__ = 'Group 4'
__versin__ = '0.0.1'

import sys
import numpy as np

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

def main(argv):
    """
    Applies TreeHeight function on data from an input file provided as a cli 
    argument
    """
    # initialize empty list
    TreeData = []
    # populates the list
    with open(sys.argv[1],'r') as f: 
        for line in f: 
            line = line.strip().split(",")
            TreeData.append(line)
    f.close()

    # Add output of TreeHeight for each tree to a new column in TreeData
    TreeData[0].append("\"Tree.Height.m\"")
    for j in range(1, len(TreeData)):
        height = TreeHeight(float(TreeData[j][1]), float(TreeData[j][2]))
        TreeData[j].append(height)

    # Write data to output file
    # splits the path and extension away from the file, and concatenate it into 
    # desired path and format
    output = "../Results/" + sys.argv[1].split("/")[2].split(".")[0] + "_treeheights.csv"
    with open(output, "w") as g:
        for k in TreeData:
            g.write(k[0] + "," + k[1] + "," + k[2] + "," + str(k[3]) + "\n")
    g.close()

    return(0)

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)

