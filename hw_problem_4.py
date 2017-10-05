# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pylab

global s_0
s_0 = 1368.0

feb = 2452672.0
may = 2452761.0
aug = 2452853.0
nov = 2452945.0

def solarIrradiance(day, theta):
    global s_0
    sun_earth_ratio = 1.0 + 0.034 * np.cos((day-3.0)/(365.0)*np.pi)
    f = s_0 * sun_earth_ratio*np.cos(theta)
    return f

febX = []
febY = []

mayX = []
mayY = []

augX = []
augY = []

novX = []
novY = []

for i in range(0,100):
    febX.append(i/100.0)
    febY.append(solarIrradiance(feb,(i/100.0*2*np.pi)))
    
    mayX.append(i/100.0)
    mayY.append(solarIrradiance(may,(i/100.0*2*np.pi)))
    
    augX.append(i/100.0)
    augY.append(solarIrradiance(aug,(i/100.0*2*np.pi)))
    
    novX.append(i/100.0)
    novY.append(solarIrradiance(nov,(i/100.0*2*np.pi)))

pylab.plot(febX,febY,mayX,mayY,augX,augY,novX,novY,'r')
pylab.legend(["Feb","may","Aug","Nov"])
pylab.xlim(-0.01,1)
pylab.ylim(-2000,2000)
pylab.show()

print('done')