#!/usr/bin/env python3

"""
Programme that takes the DNA sequences from two (argued or default) FASTA files
and saves the best alignment(s) along with corresponding score(s) in a single
text file - includes alignments with partial overlap of strands at both ends.
"""

__author__ = 'Group 4'
__version__ = '0.0.1'

import sys

def get_seq(in_fpath):
    """
    Reads the file entered as argument, creates a string (seq) of all data
    contained in the file after the first line.
    
    Parameters:
    
    in_fpath - file path to fasta file used for data extraction
    
    
    Returns:
    
    seq - fasta data extracted from input fasta file
    """
    seq = ""
    with open(in_fpath, "r") as f:
        seq_lines = f.read().splitlines(True)
        for line in seq_lines[1:]:
            seq = seq + line.strip()
    return seq


def calculate_score(s1, s2, l1, l2, startpoint): 
    """
    Computes score of the alignment given as parameters, 1 point per matching
     base pair
     
    Parameters:
    
    s1 - longer input sequence, with (l2-1)*"."s appended to either end 
    s2 - shorter input sequence
    l1 - length of s1 prior to "."s appendage to either end
    l2 - length of s2
    startpoint - point along s1 at which alignment calc_score with s2 is occurrs
    
    
    Returns:
    
    score - number of matched bases between s1 and s2
    matched - sequence of "."s, "-"s and "*"s to annotate alignment
    shift - "."s before s2 to indicate there are no matches between sequences
    end_shift - "."s after s2 to indicate there are no matches between sequences
    """
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
    shift, end_shift = startpoint * ".", (l2 + l1 - startpoint - 2) * "."
    # dots at end, but only up until end of dots tailing l1
    # if startpoint is bigger than l1-2, end shift is less than l2 according to
    # this formula. the below check stops it from getting less than l2.
    return score, matched, shift, end_shift


def main(argv):
    """
    Gets input from files, assigns longer seq to s1 & vv, calculates scores,
    and saves highest-scoring alignment(s) in new file with explanation
    """
    
    # gets seqs from the two argued .fasta files,
    # or if not provided gets seqs from the default files in data/
    if len(sys.argv) == 3 and sys.argv[1].endswith("fasta") == True \
    and sys.argv[2].endswith("fasta") == True:
        print("Aligning input sequences... please wait.")
        seq1, seq2 = get_seq(sys.argv[1]), get_seq(sys.argv[2]) 
    else: #if not, inform them and use the default fasta files
        print("Two .fasta files not provided. Using defaults from data/")
        seq1 = get_seq("../data/407228326.fasta")
        seq2 = get_seq("../data/407228412.fasta")
    
    
    # Assign the longer sequence to s1, and the shorter to s2
    l1, l2 = len(seq1), len(seq2)
    if l1 >= l2:
        s1, s2 = ((l2 - 1) * "." + seq1 + (l2 - 1) * "."), seq2
        #puts l2-1 "."s both sides of l1, allows alignment of all overlap combos
    else:
        s1, s2 = ((l1 - 1) * "." + seq2 + (l1 - 1) * "."), seq1
        l1, l2 = l2, l1 

    # writes alignment(s) with highest score into output file
    my_best_score, best_alignments = -1, [] #so 0 beats best score
    for i in range(l1 + l2 -1):
        score, matched, shift, end_shift = calculate_score(s1, s2, l1, l2, i)
        #assigns returns from calc_score function to these variables
        if score >= my_best_score:
            statement = "This alignment occurs when the smaller strand (" + \
            str(l2) + "nt in length) attaches from base " + str(i - l2 + 2) + \
            " of the larger strand, with the highest score of " + str(score) + \
            ":\n"
            #statement explaining the alignment in detail
            best_comparison_highSP =  (shift + matched + (l2 - 1) * "." + "\n")
            best_comparison_lowSP = (shift + matched + end_shift + "\n")
            best_s2, best_s1 = (shift + s2 + end_shift + "\n"), (s1 + "\n\n\n")
            #formats the matching, s1 and s2 lines to line-up neatly
            if i < l1 - 1:
                best_alignment = (str(statement) + str(best_comparison_lowSP) \
                + str(best_s2) + str(best_s1))
            else:
                best_alignment = (str(statement) + str(best_comparison_highSP) \
                + str(best_s2) + str(best_s1))
            # uses returned variables to write a statement about the alignment 
            # giving its score and startpoint, and assigns 3 lines of alignment 
            # (s1, s2 and matching bases) to a variable each for later printing
            if score > my_best_score:
                my_best_score = score
                best_alignments = [best_alignment]
            elif score == my_best_score:
                best_alignments.append(best_alignment)
    f = open('../results/fasta_better_align.txt', 'w')
    for string in best_alignments:
        f.write(string)
    f.close()
    print("Done!")
    return None
        
if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
