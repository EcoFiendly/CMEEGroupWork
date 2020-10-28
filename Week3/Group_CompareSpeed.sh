#!/bin/bash
#Auther: Cong Liu (cong.liu20@imperial.ac.uk)
#Script: CompareSpeed.sh
#Work Path: CMEECourseWork/Week3
#Input: None
#Function: Compare speeds of the following script pairs: Vectorize1.R & Vectorize1.py;
#                                                        Vectorize2.R & Vectorize2.py;
#Output:
#Usage: bash CompareSpeed.sh
#Date: Oct 2020

cd Code
echo "Running time of Vectorize1.R"
Rscript Vectorize1.R
echo ""
echo "Running time of Vectorize1.py"
python Vectorize1.py
echo ""
echo ""
echo "Running time of Vectorize2.R"
Rscript Vectorize2.R
echo ""
echo "Running time of Vectorize2.py"
python Vectorize2.py