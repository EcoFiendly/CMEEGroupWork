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

#input
## if no files are inputed with command line...
if len(sys.argv) == 1: 
    print('No files have been inputed in the command line... Using fasta files in Data directory')

    seq1, seq2= "", ""    
    with open('../Data/407228326.fasta', 'r') as fasta1:
        seq_lines = fasta1.read().splitlines()
        for line in seq_lines[1:]: #i do not want the first line (> etc...)
            line = line.strip()#remove \n from end of each line
            seq1 = seq1 + line #join together all the lines
        
    with open('../Data/407228412.fasta', 'r') as fasta2:
        seq_lines_2 = fasta2.read().splitlines()
        for line in seq_lines_2[1:]:
            line = line.strip() #remove \n from end of each line
            seq2 = seq2 + line
    
# if two files have been inputed
else:
    if sys.argv[1].endswith('.fasta') == True and sys.argv[2].endswith('.fasta') == True: 
        print('The sequences you want to align are being evaluated...')

        seq1, seq2= "", ""
        with open(sys.argv[1], 'r') as fasta1:
            seq_lines = fasta1.read().splitlines()
            for line in seq_lines[1:]:
                line = line.strip()
                seq1 = seq1 + line
        
        with open(sys.argv[2], 'r') as fasta2:
            seq_lines_2 = fasta2.read().splitlines()
            for line in seq_lines_2[1:]:
                line = line.strip()
                seq2 = seq2 + line  
    else:
        print('The files are not in the correct format, please enter FASTA files only')


#count the sequence length of both sequences
l1= len(seq1)
l2= len(seq2)

if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths if seq2 is longer than seq1

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

#output
sys.stdout = open('../results/align_2.txt','w')

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 
print(my_best_align) 
print(s1)
print("Best score:", my_best_score, file=sys.stdout)
#print("Best score:", my_best_score)
