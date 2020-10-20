#!/usr/bin/env python3

"""Programme that takes the DNA sequences as an input from a single external file and saves
the best alignment along with its corresponding score in a single text file
!!!!!!But this includes partial overlap of strands at bth ends, not just latter!!!!!!"""

__author__ = 'Ben Nouhan (b.nouhan.20@imperial.ac.uk)'
__version__ = '0.0.1'

import ipdb
import sys


def get_seq(in_fpath):
    """Reads the file entered as argument, adds each row as a string to a list called seqs"""
    seq = ""
    with open(in_fpath, "r") as f:
        seq_lines = f.read().splitlines(True)
        for line in seq_lines[1:]:
            seq = seq + line.strip()
    return seq


def calculate_score(s1, s2, l1, l2, startpoint): #need to make implicit loop to try each startpoint, choose highest score, give corresponding seqeunce side by side
    """Computes score of the alignment given as parameters, 1 point per matching base pair"""
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):  
        if (i + startpoint) < (l1 + l2 - 1): 
            if l2 - i > startpoint + 1:
                matched = matched + "."  #dots before they start overlapping
            elif s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*" #matched bases
                score = score + 1 #adds one to score
            else:
                matched = matched + "-" #not matched bases
    shift, end_shift = startpoint * ".", (l2 + l1 - startpoint - 2) * "." #dots at end, but only up until end of dots tailing l1    #if startpoint is bigger than l1-2, end shift is less than l2 according to this formula. the below check stops it from getting less than l2. is that necessary??
    return score, matched, shift, end_shift


def main(argv):
    """Gets input from file, assigns longer seq to s1 & v.v., calculates scores, and saves highest-scoring alignment(s) in new file"""
    
    ### gets seqs from the two argued .fasta files, or if not provided gets seqs from the default files in data/
    if len(sys.argv) == 3 and sys.argv[1].endswith("fasta") == True and sys.argv[2].endswith("fasta") == True:
        print("Aligning input sequences... please wait.")
        seq1, seq2 = get_seq(sys.argv[1]), get_seq(sys.argv[2]) 
    else: #if not, inform them and use the default fasta files
        print("Two .fasta files not provided. Using default files from data/fasta/.")
        seq1, seq2 = get_seq("../data/fasta/407228326.fasta"), get_seq("../data/fasta/407228412.fasta")
    
    
    ### Assign the longer sequence to s1, and the shorter to s2
    l1, l2 = len(seq1), len(seq2)
    if l1 >= l2:
        s1, s2 = ((l2 - 1) * "." + seq1 + (l2 - 1) * "."), seq2 #puts l2-1 "."s either side of l1
    else:
        s1, s2 = ((l1 - 1) * "." + seq2 + (l1 - 1) * "."), seq1
        l1, l2 = l2, l1 

    ### writes alignment(s) with highest score into output file
    my_best_score = -1 #so 0 beats it
    for i in range(l1 + l2 -1):
        score, matched, shift, end_shift = calculate_score(s1, s2, l1, l2, i)
        #assigns returns from calc_score function to these variables
        statement = "This alignment occurs when the smaller strand (" + str(l2) + "nt in length) attaches from base " + str(i - l2 + 2) + " of the larger strand, with the highest score of " + str(score) + "." + "\n\n"
        best_comparison_highSP, best_comparison_lowSP, best_s2, best_s1 = (shift + matched + (l2 - 1) * "." + "\n"), (shift + matched + end_shift + "\n"), (shift + s2 + end_shift + "\n"), (s1 + "\n\n\n\n")
        if i < l1 - 1:
            best_alignment = (str(statement) + str(best_comparison_lowSP) + str(best_s2) + str(best_s1))
        else:
            best_alignment = (str(statement) + str(best_comparison_highSP) + str(best_s2) + str(best_s1))
        #uses returned variables to write a statement about the alignment giving its score and startpoint,
        # and assigns the 3 lines of alignment (s1, s2 and matching bases) to a variable each for later printing
        if score > my_best_score:
            my_best_score = score
            f = open('../results/fasta_align.txt', 'w')
            f.write(best_alignment)
            f.close()
        elif score == my_best_score:
            f = open('../results/fasta_align.txt', 'a')
            f.write(best_alignment)
            f.close()
        print("Done!")
                

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
