"""Language: Python3
   Author: Cong Liu (cong.liu20@imperial.ac.uk)
   Script: LV3.py
   Work Path: CMEECourseWork/Week7/Code
   Dependencies: sys, numpy, scipy.integrate, matplotlib.pylab
   Input: 
   Function: Simulate discrete-time Lotka-Volterra model with prey density dependence and random fluctuation  
             and visualize results in two ways.
             Input parameters are:
             r = 1
             a = 0.19
             z = 0.4
             e = 0.75
             K =  10
   Output: Results/LV3_1.pdf
           Results/LV3_2.pdf
   Usage: python LV3.py 1 0.19 0.4 0.75 10
   Date: Nov, 2020"""

import sys
import numpy as np
import matplotlib.pylab as p

try:
   r = float(sys.argv[1])
   a = float(sys.argv[2])
   z = float(sys.argv[3])
   e = float(sys.argv[4])
   K = float(sys.argv[5])
except IndexError:
   r = 1
   a = 0.19
   z = 0.4
   e = 0.75
   K = 10

def RC_n(pops):
    """Calculate R(t+1) and C(t+1) from R(t) and C(t)"""
    R = pops[0]
    C = pops[1]
    Rn = R * (1 + r * (1 - R/K) - a * C)
    Cn = C * (1 - z + e * a * R)
    RnCn = [Rn,Cn]
    return RnCn

R0 = 10
C0 = 5
R0C0 = [R0,C0]

res = np.zeros((1000,2))
res[0,:] = R0C0

t = list(range(0,999))

for i in t:
    res[i + 1,:] = RC_n(res[i,:])
print(res[-1,:])

t = list(range(0,1000))
f1 = p.figure()
p.plot(t, res[:,0], 'g-', label='Resource density') # Plot
p.plot(t, res[:,1]  , 'b-', label='Consumer density')
p.legend(loc='best')
p.text(650,8.5,"r = " + str(r))
p.text(650,8,"a = " + str(a))
p.text(650,7.5,"z = " + str(z))
p.text(650,7,"e = " + str(e))
p.text(650,6.5,"K = " + str(int(K)))
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')
#p.show()# To display the figure
f1.savefig('../Results/LV3_1.pdf') #Save figure

f2 = p.figure()
p.plot(res[:,0], res[:,1], "r-")
p.text(9,10,"r = " + str(r))
p.text(9,9.5,"a = " + str(a))
p.text(9,9,"z = " + str(z))
p.text(9,8.5,"e = " + str(e))
p.text(9,8,"K = " + str(int(K)))
p.xlabel("Resource density")
p.ylabel("Consumer density")
p.title("Consumer-Resource population dynamics")
f2.savefig("../Results/LV3_2.pdf")
