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

x = np.linspace(year_begin, year_end, 365) # x-axis from january 1, 2012 to december 31, 2012--day
y = np.linspace(-90, 90, 180) # y-axis from -90 degrees to 90 degrees--latitude

X, Y = np.meshgrid(x, y) # set up the contour
Z = np.zeros((np.size(x), np.size(y))) # calculate the z values

for i in range(np.size(x)):
    for j in range(np.size(y)):
        Z[i,j] = averagedSolarIrradiance(x[i], y[j])

CS = pylab.plt.contour( Z, 20, colors='black') # plot contour
manuallocations = [(20, 182),(40, 182),(60, 182),(80, 182),
                   (100, 182),(120, 182),(140, 182),(160,182)]
pylab.plt.clabel(CS, inline=1, fontsize=10, manual=manuallocations)
pylab.xlabel('Latitude')
pylab.ylabel('Days (of the year)')

# m = Basemap()
# cs = m.contour()
# clabels = ax.clabel(CS)
