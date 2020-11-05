#!/bin/bash
# Author: Maddalena Cella mc2820@ic.ac.uk
# Script: run_get_TreeHeight.sh
# Description: shell script to run the get_TreeHeight.R and get_Treeheight.py scripts
# Arguments: None
# Date: October 2020

#run get_TreeHeight.R with trees.csv file
Rscript get_TreeHeight.R ../Data/trees.csv

#run get_TreeHeight.py with trees.csv file
python3 get_TreeHeight,py ../Data/trees.csv