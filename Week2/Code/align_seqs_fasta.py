#!/usr/bin/env python3

# Author: Maddalena Cella mc2820@ic.ac.uk and Group 4
# Script: align_seqs_fasta.py
# Description: program that takes DNA sequences from two FASTA files and aligns them
# Input: python3 align_seqs_fasta <*.fasta> <*.fasta>; where *.fasta and *.fasta from ../data/ directory
# Output: align.txt to ../results/ directory
# Date: October 2020

""" This Program takes DNA sequences from two external FASTA files
    and saves the best alignment and score in a new text file """
__appname__="align_seqs_fasta.py"
__author__ = "Maddalena Cella (mc2820@ic.ac.uk) and Group 4"
__version__ = "0.0.1"
__license__="None"

import sys 

#input: I merged my solution to Yewshen's because they were very similar-->##differences
if len(sys.argv) == 1: ##
    print("No arguments provided, defaulting to two fasta files in ../Data/")

    with open('../Data/407228326.fasta', 'r') as f1:
        seq1 = [line.strip() for line in f1] #need to strip
    with open('../Data/407228412.fasta', 'r') as f2:
        seq2 = [line.strip() for line in f2]

else:
    with open(sys.argv[1], 'r') as f1:
        seq1 = [line.strip() for line in f1]
    with open (sys.argv[2], 'r') as f2:
        seq2 = [line.strip() for line in f2]
##
s1= []
s2= []
for line in seq1: 
    #skips lines that start with '>'
    if not line.startswith('>'):
        line = line.strip() #removes '\n'
        s1.append(line)
for line in seq2: 
    #skips lines that start with '>'
    if not line.startswith('>'):
        line = line.strip() #removes '\n')
        s2.append(line)

#converts the lists into string
s1 = "".join(s1)
s2 = "".join(s2)

l1= len(s1)
l2= len(s2)
if l1 >= l2:
    s1, s2 = s2, s1

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)

def calculate_score(s1, s2, l1, l2, startpoint):
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"
## remove the following '#' if interested in seeing all the alignmnets
    #some formatted output
    #print("." * startpoint + matched)           
    #print("." * startpoint + s2)
    #print(s1)
    #print(score) 
    #print(" ")

    return score

# now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 
        my_best_score = z 
print(my_best_align) 
print(s1)
print("Best score:", my_best_score)

#outupt
sys.stdout = open('../results/align.txt','w')

print('Best alignmnet is:', str(my_best_align))
print('Best score is:', str(my_best_score))
sys.stdout.close()

