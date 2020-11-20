#!/bin/env python3

# Author: Group4
#
# Script: LV3.py
#
# Description: this script plots the discrete time version of the Lotka-Volterra model in two graphs
#
# Arguments: 0
#
# Input: python3 LV3.py arg1 arg2 ... etc
#
# Output: one pdf file containing two plots in ../Results/ directory 
#
# Date: November 2020

""" Script that plots Lotka-Volterra model with input model parameters from command line"""
__author__ = 'Group4'
__appname__= 'LV3.py'
__version__ = '0.0.1'
__license__= 'None'

#packages needed
import sys
import numpy as np
import scipy.integrate as integrate
import matplotlib.pylab as p
from matplotlib.backends.backend_pdf import PdfPages

#assign parameter values
if len(sys.argv) <5:
    print("You have not inputed the model parameters... Using defaults values")
    r=1
    a=0.1
    z=1.5
    e=0.75
else:
    print("Applying the LV mode with the inputed parameters")
    r = float(sys.argv[1]) #1
    a = float(sys.argv[2]) #0.1
    z = float(sys.argv[3]) #1.5
    e = float(sys.argv[4]) #0.75

#Set the initial conditions for the two populations (10 resources and 5 consumers per unit area)
R0=10 
C0=5
K=30
t=np.linspace(0, 15, 1000) #time vector

pops = np.zeros((len(t),2))#two columns:one for R and one for C

for year in range(len(t)): #loop through the years

    Rt1 = R0 * (1 + r * (1- R0/K) - a * C0)
    Ct1 = C0 * (1 - z + e * a * R0)
    R0= Rt1
    C0=Ct1
    pops[year,:]= [Rt1,Ct1]


f1 = p.figure()

p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')
textstr= '\n'.join((
    r'$r=%.2f$'%(r,),
    r'$a=%.2f$'%(a,),
    r'$z=%.2f$'%(z,),
    r'$e=%.2f$'%(e,)))
props=dict(boxstyle='round', facecolor='lightgray', alpha=0.5)
p.text(25, 10, textstr, fontsize=10, bbox=props)

f2=p.figure()

p.plot(pops[:,1], pops[:,0], '-r') # Plot (-r -> solid line, red)
p.grid()
p.xlabel('Resource Density')
p.ylabel('Prey Density')
p.title('Consumer-Resource population dynamics')
textstr= '\n'.join((
    r'$r=%.2f$'%(r,),
    r'$a=%.2f$'%(a,),
    r'$z=%.2f$'%(z,),
    r'$e=%.2f$'%(e,)))
props=dict(boxstyle='round', facecolor='lightgray', alpha=0.5)
p.text(4.4, 14, textstr, fontsize=10, bbox=props)

pp = PdfPages('../Results/LV3_models.pdf')
pp.savefig(f1)
pp.savefig(f2)
pp.close()

print('The final population size of consumers is:', int(pops[(pops.shape[0]-1),1]), 'individuals') #for a matrix of shape(n,m) where n=rows and m=columns, shape[0] gives the rows
print('The final population size of resources is:', int(pops[(pops.shape[0]-1),0]), 'individuals')
