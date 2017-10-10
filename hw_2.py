# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pylab

#find the current hour
from datetime import datetime
now = datetime.now()
Lt = now.hour

#use the latitude for Omaha,NE as given
latitude = np.deg2rad(41.15)

global s_0
s_0 = 1368.0

year = 2457755.0
year2 = 2458119.0

def solarIrradiance(day):
    global s_0
    sun_earth_ratio = 1.0 + 0.034 * np.cos(((day-3.0)/(365.0))*2*np.pi)
    declination_angle = np.deg2rad(-23.45)*np.cos((day+ 10.)/365*2*np.pi)
    hour_angle = (2*np.pi/(24*3600))*(Lt-12*3600.)
    cos_theta = np.cos(latitude)*np.cos(declination_angle)*np.cos(hour_angle) + np.sin(declination_angle)*np.sin(latitude)
    f = s_0*sun_earth_ratio*cos_theta
    return f


yearX = []
yearY = []

const = 4000.0

for i in range(0,365):
    yearX.append(i)
    yearY.append(solarIrradiance(year+i))
    
pylab.plot(yearX,yearY)
pylab.legend(["days"])
pylab.xlim(0,365)
pylab.ylim(-2000,0)
pylab.show()

print('done')