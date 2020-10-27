#!/usr/bin/env python3

"""
Debug practice, where the bug prevents oaks from being found
Debug by writing doctests
"""

__appname__ = '[oaks_debugme.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = ""

## Imports ##

import csv
import sys
import doctest

## Functions ##

#Define function
def is_an_oak(name):
    """ 
    Returns True if name starts with 'quercus' 
    
    >>> is_an_oak('Fagus sylvatica')
    False

    >>> is_an_oak('Querrcus robur')
    False

    >>> is_an_oak('Quercus robur')
    True
    
    """
    return name.lower().startswith('quercus')
    # only accepts quercus, filters out typos

def main(argv):
    """
    Opens and reads TestOaksData.csv, opens JustOaksData.csv for writing
    Checks if species in TestOaksData.csv are from the genus quercus, and writes
    them to JustOaksData.csv if they are.
    """
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    # oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        print(is_an_oak(row[0]))
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])
    f.close()
    g.close()

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)
    # sys.exit(status)

doctest.testmod() # To run with embedded tests