#!/bin/bash

# Author: Group 4
# Script: compare_Speed.sh
# Desc: Script runs Vectorize 1 and 2 in both R and python for speed comparison
# Date: Nov 2020

echo "Speed for Vectorize 1 and 2 in R:"
echo "Time taken for Vectorize1.R:"
Rscript Vectorize1.R
echo ""
echo "Time taken for Vectorize2.R:"
Rscript Vectorize2.R
echo ""
echo "Speed for Vectorize 1 and 2 in python:"
echo "Time taken for Vectorize1.py:"
python3 Vectorize1.py
echo ""
echo "Time taken for Vectorize2.py:"
python3 Vectorize2.py