# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:16:29 2018

@author: Nathaniel
"""

import numpy as np
import pylab

def planckFunction(wave, temp): # wavelength and temp (Kelvins)
    if wave == 0.0:
        return 0.0
    k_b = np.float64(1.3806485279*10**-23) # boltzmann constant (joules/second)
    c = np.float64(2.997924580*10**8)      # speed of light (meters/second)
    h = np.float64(6.62607004081*10**-34)  # planck constant (joules/second)
    
    spectral_density = np.float64( (2*h*c**2) / ((wave**5)*(np.e**( (h*c)/(k_b*wave*temp) )-1)) )*(10**-6)
    return spectral_density 
    # return ( (2*h)/(c**3) ) * ( (freq**3)/(np.e**( (h*freq)/(k_b*temp) ) -1 ) )
    # return 2*h*(c**2)/((wave**5)*(np.exp(h*c/(k_b*wave*temp))-1))/1000.0/1000.0
    
def wienDisplacement(temp):
    wave_max = (2897.0)/temp
    return wave_max

def run():
    x = []
    sun = []
    earth = []
    mars = []
    wienDisp = []
    
    step = np.float(1)
    for i in range(1, 100):
        x.append(i*step)
        sun.append((planckFunction(i*10**-6, 6000.0)))
        earth.append((planckFunction(i*10**-6, 300.0)))
        mars.append((planckFunction(i*10**-6, 250.0)))
        wienDisp.append(wienDisplacement(i*60))
    
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.plot(x,sun,linewidth='2.5', label='6000 K')
    pylab.plot(x,earth,linewidth='2.5', label='300 K')
    pylab.plot(x,mars,linewidth='2.5',label='250 K')
    pylab.plot(x,wienDisp,linewidth='2.5',label='Wien Displacement')
    pylab.xlabel('Wavelength (µm)')
    pylab.ylabel('Spectral radiance (W m$^{−2}$ µm$^{−1}$ sr$^{−1}$)')
    pylab.legend()
    pylab.show()