#!/bin/bash
#Auther: Cong Liu (cong.liu20@imperial.ac.uk)
#Script: run_get_TreeHeight.sh
#Work Path: CMEECourseWork/Week3
#Input: Data/tree.csv
#Function: Test get_TreeHeight.R and get_TreeHeight.py
#Output:
#Usage: bash run_get_TreeHeight.sh [Input]
#Date: Oct 2020


Rscript Code/get_TreeHeight.R $1
python Code/get_TreeHeight.py $1