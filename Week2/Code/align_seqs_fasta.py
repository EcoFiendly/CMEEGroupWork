#!/usr/bin/env python3

"""
Script that takes DNA sequences as input from a single external file and 
aligns two DNA sequences such that they are as similar as possible. The best 
alignment, along with its corresponding score is then saved in a text file to 
the /Results/ directory. 

This script is able to take user arguments from cli. However, if no arguments 
were provided, the script defaults to two fasta files in the /Data/ directory.

Script starts by positioning the beginning of the shorter sequence at all 
positions (bases) of the longer one (the start position), and count the number 
of bases matched. The alignment with the highest score wins. Ties are possible, 
in which case, an arbitrary alignment (e.g. first or last) with the highest 
score is taken.
"""

__appname__ = '[align_seqs_fasta.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = ""

## Imports ##
import sys # module to interface our program with the operating system

## Constants ##

# Read cli arguments using the sys module

if len(sys.argv) != 3:
    print("No arguments provided, defaulting to 2 fasta files in ../Data/")
    # opens the default files
    with open('../Data/407228326.fasta', 'r') as f1:
        seq1 = [line.strip() for line in f1]
    with open('../Data/407228412.fasta', 'r') as f2:
        seq2 = [line.strip() for line in f2]
else:
    # opens the files provided as arguments
    with open(sys.argv[1], 'r') as f1:
        seq1 = [line.strip() for line in f1]
    with open(sys.argv[2], 'r') as f2:
        seq2 = [line.strip() for line in f2]

# Populate s1 and s2 with sequences from file1 and file2 respectively
# also skips the line if it starts with > (skips lines which are not sequences)
s1 = []
for row in seq1:
    if row[0:1] != '>':
        row = row.strip() # removes '\n'
        s1.append(row)

s2 = []
for row in seq2:
    if row[0:1] != '>':
        row = row.strip() # removes '\n'
        s2.append(row)

# convert the lists to strings

s1 = "".join(s1)
s2 = "".join(s2)

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(s1)
l2 = len(s2)
if l1 <= l2:
    s1, s2 = s2, s1 # swap the two seqences
    l1, l2 = l2, l1 # swap the two lengths

# for finding the best match (highest score) for the two sequences

my_best_align = None
my_best_score = -1

## Functions ##

def calculate_score(s1, s2, l1, l2, startpoint):
    """
    Computes a score by returning the number of matches starting from an 
    arbitrary startpoint (chosen by user)

        Parameters:
            s1 (str): string containing the longer sequence
            s2 (str): string containing the shorter sequence
            l1 (int): length of s1
            l2 (int): length of s2
            startpoint: arbitrary startpoint chosen by user

        Returns:
            score (int): number of matches between the sequences
            matched (str): matched string with * as match and - as no match

    """
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output, commented out to speed up the code
    # print("." * startpoint + matched)           
    # print("." * startpoint + s2)
    # print(s1)
    # print(score) 
    # print(" ")

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 

print(my_best_align)
print(s1)
print("Best score:", my_best_score)

# Save output to a text file in /Results/ directory
sys.stdout = open('../Results/best_align.txt', 'w')
# Write to the file
print("Best align is:", str(my_best_align))
print("Best score is:", str(my_best_score))
sys.stdout.close() # Close output file