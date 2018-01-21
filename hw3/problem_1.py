# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
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

    # returns solar irradiance on given day, latitude and hour
def hourlySolarIrradiance(latitude, day, hour):
    global s_0
    sun_earth_ratio = 1.0 + 0.034 * np.cos(((day-3.0)/(365.0))*2*np.pi)
    declination_angle = np.deg2rad(-23.45)*np.cos((day+ 10.)/365*2*np.pi)
    hour_angle = (2*np.pi/(24*3600))*(hour*3600.-12*3600.)
    cos_theta = ( np.cos(latitude)*np.cos(declination_angle)*np.cos(hour_angle)
                + np.sin(declination_angle)*np.sin(latitude) )
    f = s_0*sun_earth_ratio*cos_theta
    
    return 0 if f < 0 else f
    
    # returns average solar irradiance on given day and latitude
def averagedSolarIrradiance(day, latitude):
    avg = 0.0
    for i in range(12): # hours
        avg += hourlySolarIrradiance(np.deg2rad(latitude),day,i*2)
    return avg/12.0

'''
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
'''

x = np.linspace(-90, 90, 180)
y = np.linspace(year_begin, year_end, 365)

X, Y = np.meshgrid(x, y) # set up the contour
Z = np.zeros((np.size(x), np.size(y))) # calculate the z values
W = np.zeros((np.size(x), np.size(y)))

for i in range(np.size(x)):
    for j in range(np.size(y)):
        a = averagedSolarIrradiance(y[j], x[i])
        if a == 0.0:
            W[i,j] = 1
        else:
            W[i,j] = None
        Z[i,j] = a

pylab.close()

ax = plt.subplot(111)

center = 173.5
label_bbox=dict(facecolor='white', edgecolor='none', pad=1.0)

# CF = pylab.plt.contour(Z, 0, colors='black')
pylab.plt.contourf(W, 10, colors='gray')
CS = pylab.plt.contour( Z, 20, colors='black') # plot contour
manuallocations = [(center, 20),(center, 40),(center, 60),(center, 80),
                   (center, 100)]
pylab.plt.clabel(CS, inline=0, fontsize=10, manual=manuallocations)

pylab.title("Daily average insolation [W m$^{-2}$]")

pylab.text(160,170,'24 hr light',backgroundcolor='white',bbox=label_bbox)
pylab.text(160,10,'24 hr darkness')

pylab.text(10,170,'24 hr darkness')
pylab.text(310,170,'24 hr darkness')

pylab.text(10,10,'24 hr light',backgroundcolor='white',bbox=label_bbox)
pylab.text(310,10,'24 hr light',backgroundcolor='white',bbox=label_bbox)

new_x_axis = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
new_y_axis = ['SP', '60S', '30S', 'EQ', '30N', '60N', 'NP']

months=[0,30,58,89,119,150,180,211,242,272,303,333,364]
lats=[0,30,60,90,120,150,180]

ax.set_xticks(months)
ax.set_xticklabels(new_x_axis)

ax.set_yticks(lats)
ax.set_yticklabels(new_y_axis)

pylab.show()
