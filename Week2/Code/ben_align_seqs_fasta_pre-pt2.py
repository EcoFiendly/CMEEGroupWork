#!/usr/bin/env python3

"""Programme that takes the DNA sequences as an input from a single external file and saves
the best alignment along with its corresponding score in a single text file
!!!!!!But this includes partial overlap of strands at bth ends, not just latter!!!!!!"""

__author__ = 'Ben Nouhan (b.nouhan.20@imperial.ac.uk)'
__version__ = '0.0.1'

import ipdb
import sys



def get_seqs(in_fpath1, in_fpath2):
    """Reads the file entered as argument, adds each row as a string to a list called seqs"""
    seq1, seq2 = "", ""
    with open(in_fpath1, "r") as f: ####return back to in_fpath1 when done. need to remove \n but strip or rstrip arent working. then work out the input stuff
        seq_lines_1 = f.read().splitlines(True)
        for line in seq_lines_1[1:]:
            line = line.strip()
            seq1 = seq1 + line
    with open(in_fpath2, "r") as f:
        seq_lines_2 = f.read().splitlines(True)
        for line in seq_lines_2[1:]:
            line = line.strip()
            seq2 = seq2 + line
    return seq1, seq2


def calculate_score(s1, s2, l1, l2, startpoint): #need to make implicit loop to try each startpoint, choose highest score, give corresponding seqeunce side by side
    """Computes score of the alignment given as parameters, 1 point per matching base pair"""
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):  
        if (i + startpoint) < (l1 + l2 - 1):  #####################change 3################## shows matches all the way along
            if l2 - i > startpoint + 1:
                matched = matched + "."  #dots before they start overlapping
            elif s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*" #matched bases
                score = score + 1 #adds one to score
            else:
                matched = matched + "-" #not matched bases
    shift, end_shift = startpoint * ".", (l2 + l1 - startpoint - 2) * "." #dots at end, but only up until end of dots tailing l1
    return score, matched, startpoint, shift, end_shift


def main(argv):  # start with all assignments (except ones that must be assigned later) then everything else including calling functions defined above
    """Gets input from file, assigns longer seq to s1 & v.v., calculates scores, and saves highest-scoring in new file"""
    
    ### gets seqs from the two argued .fasta files, or if not provided gets seqs from the default files in data/
    if len(sys.argv) == 3: #if 2 arguments (plus the .py) called as planned, and both .fasta, use them
        if sys.argv[1].endswith("fasta") == True and sys.argv[2].endswith("fasta") == True:
            print("Aligning input sequences... please wait.")
            seq1, seq2 = get_seqs(sys.argv[1], sys.argv[2])
        else:
            print("Please enter only .fasta files to align.")
            sys.exit()
    else: #if not, inform them and use the default fasta files
        print("Two .fasta files not provided. Using default files from data/fasta/.")
        seq1, seq2 = get_seqs("../data/fasta/407228326.fasta", "../data/fasta/407228412.fasta") #the function can basically be replaced with output, just like print(x). hence unpack the output as shown here, where only ouput is return seq1, seq2
    
    
    ### Assign the longer sequence to s1, and the shorter to s2
    l1, l2 = len(seq1), len(seq2)
    if l1 >= l2:
        s1 = ((l2 - 1) * "." + seq1 + (l2 - 1) * ".")
        s2 = seq2
    else:
        s1 = ((l1 - 1) * "." + seq2 + (l1 - 1) * ".")
        s2 = seq1
        l1, l2 = l2, l1 

    ### finds alignment with highest score, save others with same score
    my_best_score = -1 #so 0 beats it
    for i in range(l1 + l2 -1):
        z, matched, startpoint, shift, end_shift = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score: #hash these lines for when I don't want to use pickle; use pickle to write lines instead of this, to pring multiples easily
            my_best_score, my_best_align, my_best_matched, my_best_startpoint, my_best_shift, my_best_end_shift = z, s2, matched, startpoint, shift, end_shift

        #     f = open('../sandbox/samescore_aligns.p', 'wb') # may make blank first line therefore [0] will give nothing, check]
        #     f.write("")
        # elif z = my_best_score: #requires pickle!!!!! ouput file should be .p (pickle?)
        #     f=open('../sandbox/samescore_aligns.p', 'wb') #read not write
        #     f.write("") #may make blank first line therefore [0] will give nothing, check] # writethese variables as tuple to read and output later
        
    ### writes output into a file, in alginment format plus an interpretation
    f = open('../results/fasta_align.txt', 'w')
    if my_best_startpoint > l1 - 2:
        f.write(my_best_shift + my_best_matched + (l2 - 1) * "." + "\n")
    else:
        f.write(my_best_shift + my_best_matched + my_best_end_shift + "\n")
        f.write(my_best_shift + my_best_align + my_best_end_shift + "\n")
        f.write(s1 + "\n")
        f.write("The best alignment occurs when the smaller strand (" + str(l2) + "nt in length) attaches from base " + str(my_best_startpoint - l2 + 2) + " of the larger strand, with a score of " + str(my_best_score) + "." + "\n")
        f.close()
    print("Done!")


if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)


#The current script/program runs through all possible starting points on the main sequence and then just takes the first of the alignments
# with the highest score. This should be apparent if you closely examine this part of the script:

# for i in range(l1):
#     z = calculate_score(s1, s2, l1, l2, i)
#     if z > my_best_score:
#         my_best_align = "." * i + s2
#         my_best_score = z


#This means when multiple alignments have the same score(highly likely in longer sequences), you lose all the equally good alignments,
# keeping only the last one.

#Modify the script so that all the equally best alignments are recorded and saved to the results directory in an appropriate
# file format(Hint: recall pickle). Call your new script align_seqs_better.py.

# allows the write function to use these
