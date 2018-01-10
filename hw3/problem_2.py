# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:16:29 2018

@author: Nathaniel
"""

import numpy as np
import pylab

def planckFunction(wave, temp): # wavelength and temp (Kelvins)
    k_b = np.float64(1.3806485279*10**-23) # boltzmann constant (joules/second)
    c = np.float64(2.997924580*10**8)      # speed of light (micrometers/second)
    h = np.float64(6.62607004081*10**-34)  # planck constant (joules/second)
    
    return np.float64( (2*h*c**2)/((wave**5)*(np.e**( (h*c)/(k_b*wave*temp) )-1)) )
    
def wienDisplacement(temp):
    wave_max = (2.897772917*10**-3)/temp
    return wave_max

x = []
sun = []
earth = []
sunWienDisp = []

for i in range(0, 10):
    x.append(i)
    sun.append(planckFunction(np.float64(i), 6500.0)) # earth frequency (0 micrometer to 500 micrometer) and temp
    earth.append(planckFunction(np.float64(i),300.0))
    
pylab.plot(x,sun,linewidth='2.5')
pylab.plot(x,earth,linewidth='2.5')
pylab.xlabel('Wavelength (µm)')
pylab.ylabel('Spectral radiance (W m$^{−2}$ µm$^{−1}$ sr$^{−1}$)')
pylab.xscale('log')
pylab.yscale('log')
pylab.show()