#!/usr/bin/env python3

"""Practical on findiing oaks in a csv dataframe"""

__appname__ = 'oaks_debugme.py'
__author__ = 'Billy Lam (ykl17@ic.ac.uk)'
__version__ = '0.0.1'

# Import packages
import csv
import sys
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' 
    
    >>> is_an_oak('Quercus robur')
    True
        
    >>> is_an_oak('Fagus sylvatica')
    False

    >>> is_an_oak('Querrcus robur')
    False

    """
    return name.lower().startswith('quercus')

def main(argv): 
    """
    Reads TestOaksData.csv and writes JustOaksData.csv.
    We will find oak species in TestOaksData and save them in JustOaksData.csv
    """
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()
    for row in taxa:
        if row[0] != "Genus":
            print(row)
            print ("The genus is: ") 
            print(row[0] + '\n')
            if is_an_oak(row[0]):
                print('FOUND AN OAK!\n')
                csvwrite.writerow([row[0], row[1]])    
    g.close()

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod() 