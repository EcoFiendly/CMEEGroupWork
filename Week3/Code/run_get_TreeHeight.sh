#!/bin/bash
# Author: Group 4
# Script: run_get_TreeHeight.sh
# Desc: shell script to run R and python versions of get_TreeHeight
# Arguments: none
# Date: Oct 2020

# run get_TreeHeight.R with trees.csv
Rscript get_TreeHeight.R ../Data/trees.csv

# run get_TreeHeight.py with trees.csv
python3 get_TreeHeight.py ../Data/trees.csv