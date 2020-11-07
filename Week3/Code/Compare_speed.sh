#!/bin/bash

# Author: Billy
# Script: Compare_Speed.sh
# Desc: Script runs Vectorize 1 and 2 in both R and python for speed comparison
# Date: Nov 2020


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