# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:37:09 2018

@author: Nathaniel
"""

from problem_2 import planckFunction
import pylab
import numpy as np

def run():
    x = []
    y = []
    
    for i in range(1, 1001):
        x.append(i/100.0)
        y.append((planckFunction(i*10**-8, 2850.0)))
    
    pylab.ticklabel_format(axis='y', style='sci', scilimits=(-3,4)) # label in scientific notation
    pylab.plot(x,y,linewidth='2.5', label='2850 K')
    pylab.xlabel('Wavelength (µm)')
    pylab.ylabel('Spectral radiance (W m$^{−2}$ µm$^{−1}$ sr$^{−1}$)')
    pylab.legend()
    pylab.show()

def area(a, b, temp, steps=8192.0): # use Simpson's rule to estimate area under curve
    area = 0
    h = (b-a)/steps # calculate step size
    segs = np.arange(a,b,(b-a)/steps) # get the x-value of each step
    for i in range(len(segs)-1): # sum the area under the cubic polynomials
        area += (h/6)*(planckFunction(segs[i], temp) +
                 4*planckFunction((segs[i+1]+segs[i])/2.0, temp) +
                 planckFunction(segs[i+1], temp))
    return area*10**6

# print(area(4.0*10**-6,7.0*10**-6,2850))
print(area(4.0*10**-6,7.0*10**-6,2850,8192))
run()