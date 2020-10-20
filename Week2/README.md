# Week 2

*Author: Group 4*

*Created: Week2*

This directory contains the scripts, data and results from week 2 for the group practical

Languages used in this week:
1. Python

Requirements:
1. Python

## Scripts

### 1. align_seqs_fasta.py

Script takes DNA sequences as input from a single external file and aligns two DNA sequences such that they are as similar as possible. The best alignment, along with it s corresponding score is then saved in a text file to the /Results/ directory.

This script is able to take user arguments from cli. However, if no arguments were provided, the script defaults to two fasta files in the /Data/ directory.

Script starts by positioning the beginning of the shorter sequence at all positions (bases) of the longer one (the start position), and count the number of bases matched. othe alignment with the highest score wins. Ties are possible, in which case, an arbitrary alignment (e.g. first or last) with the hightest score it taken.

### 2. align_seqs_better.py

Script works the same as align_seqs_fasta.py with the addition of saving equally good alignments when they share the same score as the best alignment.
