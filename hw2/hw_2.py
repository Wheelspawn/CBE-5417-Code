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
latitude = 41.15

global s_0
s_0 = 1368.0

feb = 2452672.0
may = 2452761.0
aug = 2452853.0
nov = 2452945.0

#if Lt == 12:
    #for

def solarIrradiance(day, theta):
    global s_0
    sun_earth_ratio = 1.0 + 0.034 * np.cos(((day-3.0)/(365.0))*2*np.pi)
    declination_angle = -23.45*np.cos((day+ 10.)/365*2*np.pi)
    hour_angle = (2*np.pi/(24.*3600))*(Lt-12.*3600.)
    cos_theta = np.cos(latitude)*np.cos(declination_angle)*np.cos(hour_angle) + np.sin(declination_angle)*np.sin(latitude)
    f = s_0*sun_earth_ratio*cos_theta
    return f

febX = []
febY = []

mayX = []
mayY = []

augX = []
augY = []

novX = []
novY = []

const = 4000.0

for i in range(0,int(const)):
    febX.append(i/const)
    febY.append(solarIrradiance(feb,(i/const*np.pi)))
    
    mayX.append(i/const)
    mayY.append(solarIrradiance(may,(i/const*np.pi)))
    
    augX.append(i/const)
    augY.append(solarIrradiance(aug,(i/const*np.pi)))
    
    novX.append(i/const)
    novY.append(solarIrradiance(nov,(i/const*np.pi)))

pylab.plot(febX,febY,'b--',mayX,mayY,'y',augX,augY,'g--',novX,novY,'r')
pylab.legend(["Feb","may","Aug","Nov"])
pylab.xlim(-0.01,1.01)
pylab.ylim(-1500,1500)
pylab.show()

print('done')