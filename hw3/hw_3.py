# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pylab

import sys  

sys.setdefaultencoding('utf8')

#find the current hour
from datetime import datetime
now = datetime.now()
Lt = now.hour

global s_0
s_0 = 1368.0

year_begin = 0 # january 1, 2012
year_end = 	364 # december 31, 2012
    
def hourlySolarIrradiance(latitude, day, hour): # returns solar irradiance on given day, latitude and hour
    global s_0
    sun_earth_ratio = 1.0 + 0.034 * np.cos(((day-3.0)/(365.0))*2*np.pi)
    declination_angle = np.deg2rad(-23.45)*np.cos((day+ 10.)/365*2*np.pi)
    hour_angle = (2*np.pi/(24*3600))*(hour*3600.-12*3600.)
    cos_theta = np.cos(latitude)*np.cos(declination_angle)*np.cos(hour_angle) + np.sin(declination_angle)*np.sin(latitude)
    f = s_0*sun_earth_ratio*cos_theta
    
    return 0 if f < 0 else f
    
def averagedSolarIrradiance(day, latitude): # returns average solar irradiance on given day and latitude
    avg = 0.0
    for i in range(24): # hours
        avg += hourlySolarIrradiance(np.deg2rad(latitude),day,i)
    return avg/24.0
    
def planckFunction(wave, temp): # wavelength and temp (Kelvins)
    print wave 
    k_b = np.float64(1.3806485279*10**-23) # boltzmann constant (joules/second)
    c = np.float64(2.997924580*10**8)      # speed of light (micrometers/second)
    h = np.float64(6.62607004081*10**-34)  # planck constant (joules/second)
    
    return np.float64( (2*h*c**2)/((wave**5)*(np.e**( (h*c)/(k_b*wave*temp) )-1)) )
    
def wienDisplacement(temp):
    wave_max = (2.897772917*10**-3)/temp
    return wave_max
    
'''
x = np.linspace(year_begin, year_end, 365) # x-axis from january 1, 2012 to december 31, 2012--day
y = np.linspace(-90, 90, 180) # y-axis from -90 degrees to 90 degrees--latitude

X, Y = np.meshgrid(x, y) # set up the contour
Z = np.zeros((np.size(x), np.size(y))) # calculate the z values

for i in range(np.size(x)):
    for j in range(np.size(y)):
        Z[i,j] = averagedSolarIrradiance(x[i], y[j])

CS = pylab.plt.contour( Z, 20, colors='black') # plot contour
'''

# m = Basemap()
# cs = m.contour()
# clabels = ax.clabel(CS)

# milli = 10^-3
# micro = 10^-6
# nano = 10^-9

def run():
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
    pylab.xlabel('Wavelength (m)')
    pylab.ylabel('Spectral radiance (W m$^{−2}$ µm$^{−1}$ sr$^{−1}$)')
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.show()
