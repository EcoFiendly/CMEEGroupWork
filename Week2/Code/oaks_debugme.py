"""Language: Python3
   Auther: Cong Liu (cong.liu20@imperial.ac.uk)
   Script: oaks_debugme.py
   Work Path: CMEECourseWork/Week2
   Input file:
   Function: Practical of python programming
   Output:
   Usage: python oaks_debugme.py
   Date: Oct, 2020"""

import csv
import sys
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' 
    >>> is_an_oak("Quercus, robur")
    True
    
    >>> is_an_oak("quercuss, sylvestris")
    False

    >>> is_an_oak("Fraxinus, excelsior")
    False
    """
    name = name.lower().split(",")
    if name[0] == "quercus":
        return True
    return False

def main(argv): 
    """Find oaks in Data.TestOaksData.csv and save results in Results/JustOaksData.csv"""
    f = open('./Data/TestOaksData.csv','r')
    g = open('./Results/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    csvwrite.writerow(["Genus", "species"])
    for row in taxa:
        if row[0] != "Genus":
            print(row)
            print ("The genus is: ") 
            print(row[0] + '\n')
            if is_an_oak(row[0]):
                print('FOUND AN OAK!\n')
                csvwrite.writerow([row[0], row[1]])    

    return 0
    
if (__name__ == "__main__"):
   status = main(sys.argv)

doctest.testmod() 