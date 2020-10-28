"""Language: Python3
   Auther: Cong Liu (cong.liu20@imperial.ac.uk)
   Script: get_TreeHeight.py
   Work Path: CMEECourseWork/Week3
   Dependencies: sys, math
   Input: Data/trees.csv
   Function: Calculate heights of trees given distance of each tree 
             from its base and angle to its top, using  the trigonometric formula 
   Output: Results/trees_treeheights.csv
   Usage: python get_TreeHeight.py [Input]
   Date: Oct, 2020"""

import sys
import math

inpu = sys.argv[1]
file = open(inpu, "r")

data = []
for line in file:
    line = line.strip().split(",")
    data.append(line)
file.close()

def TreeHeight(distance, degree):
    """Calculate heights of trees.
       
       Input:
       distance: the distance from tree base
       degree: angle to its top
       
       Output: Height of tree"""
    pi = math.pi
    deg = degree*pi/180
    tanv = math.tan(deg)
    height = distance * tanv
    return height

res = []
data[0].append("Tree.Height.m")
for i in range(1,len(data)):
    height = TreeHeight(float(data[i][1]), float(data[i][2]))
    data[i].append(height)

result_name = "Results/" + inpu.split("/")[1].split(".")[0] + "_treeheights.csv"
result = open(result_name, "w")
for i in data:
    result.write(i[0]+","+i[1]+","+i[2]+","+str(i[3]))
    result.write("\n")

result.close() 
