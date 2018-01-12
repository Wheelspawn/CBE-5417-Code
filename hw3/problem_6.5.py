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
    wicky_woo = []
    
    for i in range(1, 1001):
        x.append(i/100.0)
        wicky_woo.append((planckFunction(i*10**-8, 2850.0)))
    
    # pylab.ticklabel_format(axis='y', style='sci', scilimits=(-3,4))
    pylab.plot(x,wicky_woo,linewidth='2.5', label='2850 K')
    pylab.xlabel('Wavelength (µm)')
    pylab.ylabel('Spectral radiance (W m$^{−2}$ µm$^{−1}$ sr$^{−1}$)')
    pylab.legend()
    pylab.show()

def area(a, b, temp, steps=2048.0): # use Simpson's rule to estimate area under curve
    area = 0
    h = (b-a)/steps
    segs = np.arange(a,b,(b-a)/steps)
    for i in range(len(segs)-1):
        area += (h/6)*(planckFunction(segs[i], temp) + 4*planckFunction((segs[i+1]+segs[i])/2.0, temp) + planckFunction(segs[i+1], temp))
    return area*10**6

# print(area(4.0*10**-6,7.0*10**-6,2850))
print(area(4.0*10**-6,7.0*10**-6,2850))
run()