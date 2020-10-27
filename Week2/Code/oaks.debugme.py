#!/usr/bin/env python3

"""Script that fixes a bug and allows oak species to be recognised from a list of trees"""

__author__ = 'Maddalena Cella mc2820@ic.ac.uk'
__version__ = '0.0.1'

import csv
import sys

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' """
    if all([len(name.split()[0]) == 7 and name.lower().startswith('quercus')]): #counts the number of characters in the first letter of 'name'
    #split() splits string into list
        return True
    else:
        return False

#doctests:
#is_an_oak('Quercuss robur')
#is_an_oak('Quercus robur')
#is_an_oak('sucrueq robur')

def main(argv): 
    f = open('../data/TestOaksData.csv','r') #dowload these into data directory when home
    g = open('../data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()
    for row in taxa:
        if row[0] == 'Genus':
            csvwrite.writerow([row[0], row[1]])  #this returns the header names in the output file: genus and species 
        if row[0] != 'Genus': #this excludes the headers in the species evaluation 
            print('The Genus is: ' + row[0])
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])  

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)
