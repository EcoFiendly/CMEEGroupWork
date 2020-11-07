#!/usr/bin/env python3

"""Searches input csv file for species of oak tree (not allowing for typos)
and writes them into a new csv document"""


#docstrings are considered part of the running code (normal comments are
#stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ben Nouhan (b.nouhan.20@imperial.ac.uk)'
__version__ = '0.0.1'


import csv
import sys
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if name (made lowercase) == 'quercus'
    
    Parameters:
    
    name - genus of tree species - tollerates nothing but input of genus
           (with any extent of capitalisation) spelt correctly
    
    
    Returns:
    
    True OR False - depending on whether the genus is "Quercus"
    
    

    >>> is_an_oak("quercus")
    True

    >>> is_an_oak("Quercus")
    True

    in case of wrong genus:
    >>> is_an_oak("Pinus")
    False

    in case of typo:
    (could tollerate this using: return "quercus" in name.lower() and writing
    "Quercus" into file by default as below, but haven't been asked to)
    >>> is_an_oak("Quercuss")
    False

    
    in case of genus + species in same cell:
    >>> is_an_oak("Quercus whateverus")
    False

    """
    return name.lower() == 'quercus'

def main(argv):
    """Opens file, reads taxa, selects those of the "Quercus" genus, and writes
    them into a new file"""
    f = open('../data/TestOaksData.csv','r')
    g = open('../results/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()
    csvwrite.writerow(["Genus", " species"])
    for row in taxa:
        if row[0] == "Genus":
            continue
        #ignores column names row
        else:
            print(row)
            print ("The genus is: ") 
            print(row[0] + '\n')
            if is_an_oak(row[0]):
                print('FOUND AN OAK!\n')
                csvwrite.writerow(["Quercus", row[1]])   
                #in case row[0] == "quercus" chars, writes capitalised version

    return None
    
doctest.testmod() 
    
if (__name__ == "__main__"):
    status = main(sys.argv)
