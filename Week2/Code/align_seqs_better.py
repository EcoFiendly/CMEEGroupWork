#!/usr/bin/env python3

# Author: Maddalena Cella mc2820@ic.ac.uk and Group 4
# Script: align_seqs_better.py
# Description: improved alignment program that records equally best alignments
# Input: seqs_copy.csv
# Output: better_align_b.p to ../results/ directory
# Date: October 2020

""" This Program takes DNA sequences from two external FASTA files
    and saves the best alignment and score in a new text file """
__appname__="align_seqs_fasta.py"
__author__ = "Maddalena Cella (mc2820@ic.ac.uk) and Group 4"
__version__ = "0.0.1"
__license__="None"


import sys
import pickle

#input

if len(sys.argv) == 1:
    with open('../Data/407228326.fasta', 'r') as f1:
        seq1 = [line.strip() for line in f1] #need to strip
    with open('../Data/407228412.fasta', 'r') as f2:
        seq2 = [line.strip() for line in f2]

else:
    with open(sys.argv[1], 'r') as f1:
        seq1 = [line.strip() for line in f1]
    with open (sys.argv[2], 'r') as f2:
        seq2 = [line.strip() for line in f2]

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
        line = line.strip() #removes '\n'
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
#it does it for every possible alignment
def calculate_score(s1, s2, l1, l2, startpoint):
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2): #for each nucleotide 'i' in the sequence 2
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*" #if matched, *
                score = score + 1 #increases the score, the more nucleotide matches there are
            else:
                matched = matched + "-" #if unmatched, -

    # some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# now try to find the best match (highest score) for the two sequences
best_aligns = None
best_scores = -1

#output is here!!!
r=open('../results/better_align_b.txt','wb') #what is .p--> needs to be binary
r_l= []

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i) #the function defined before
    
    if z == best_scores: #added the == because it can be the same score
        best_aligns = "." * i + s2 
        best_scores = z 
        r_l.append(best_scores)
        r_l.append(best_aligns)
        r_l.append(s1)
        print(best_aligns) 
        print(s1)
        print("Best score:", best_scores) 

    elif z > best_scores:
        best_aligns = "." * i + s2 
        best_scores = z

        r_l= [] #otherwise it keeps the alignments that are equally good!!!--> needs to be emptied
        r_l.append(best_scores)
        r_l.append(best_aligns)
        r_l.append(s1)

pickle.dump(r_l,r)

sys.stdout = open('../Results/best_align.txt', 'w')

print("Best score:", r_l[0])
print("Best alignmnent(s):", r_l[1:2])

r.close()
sys.stdout.close()


