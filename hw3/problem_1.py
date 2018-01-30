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
    
    return -1 if f < 0 else f
    
    # returns average solar irradiance on given day and latitude
def averagedSolarIrradiance(day, latitude):
    avg = 0.0
    for i in range(24): # hours
        avg += hourlySolarIrradiance(np.deg2rad(latitude),day,i)
    return avg/24.0

def solarDeclinationAngle(day): # calculate the solar declination angle
    return -23.45 * np.cos( np.deg2rad( (360.0/365.0) * (day + 10) ) )
    # the deg2rad inside the cos function turns the degrees to rads
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

x = np.linspace(-90, 90, 180) # x-axis.
# for some reason, matplotlib flips these so the x-axis is actually the y-axis. I don't know why
y = np.linspace(year_begin, year_end, 365) # y-axis

X, Y = np.meshgrid(x, y) # set up the contour
Z = np.zeros((np.size(x), np.size(y))) # calculate the z values
W = np.zeros((np.size(x), np.size(y))) # these will be the dark areas
P = np.zeros((np.size(x), np.size(y)))
D = np.zeros(np.size(y)) # declination angle

# calculating the Z and W values
for i in range(np.size(x)):
    for j in range(np.size(y)):
        a = averagedSolarIrradiance(y[j], x[i])
        if a <= 0.0:
            W[i,j] = 1 # matplotlib will plot this as part of the gray region
        else:
            W[i,j] = None # matplotlib won't plot these None values
        P[i,j] = a
        Z[i,j] = a

# calculate the declination angle
for k in range(np.size(D)):
    D[k] = solarDeclinationAngle(k)+90


pylab.close() # closes any plot you might have open

ax = plt.subplot(111) # this subplot will let us set custom tick labels

center = 170
# default setting for the labels. make the background white and keep the padding minimal (1.0)
label_bbox=dict(facecolor='white', edgecolor='none', pad=1.0)

# CF = pylab.plt.contour(Z, 0, colors='black')
pylab.plt.contourf(P, 30, cmap='plasma') # contourf will be filled
pylab.plt.contourf(W, 30, colors='gray') # contourf will be filled
CS = pylab.plt.contour( Z, 25, colors='black') # contour CS will have contour lines

# setting locations for some labels for insolation
manuallocations = [(center, 20),(center, 42),(center, 58),
                   (center, 75),(center, 95),(center, 160),
                   (15,55),(15,100),(15,115),(15,130),(15,145),
                   (350,60),(350,100),(350,115),(350,130),(350,145)]
pylab.plt.clabel(CS, inline_spacing=-3, fontsize=10, manual=manuallocations) # plot the labels

pylab.title("Daily average insolation [W m$^{-2}$]") # title

pylab.text(160-3,170,'24 hr light') # text for 24hr light/dark
pylab.text(160-3,10,'24 hr darkness')

pylab.text(10,170,'24 hr darkness')
pylab.text(310,170,'24 hr darkness')

pylab.text(10,10,'24 hr light')
pylab.text(310+10,10,'24 hr light')

# custom axis tick labels
new_x_axis = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
new_y_axis = ['SP', '60S', '30S', 'EQ', '30N', '60N', 'NP']

# where to place the labels
months=[0,30,58,89,119,150,180,211,242,272,303,333,364]
lats=[0,30,60,90,120,150,180]

# set the labels
ax.set_xticks(months)
ax.set_xticklabels(new_x_axis)

ax.set_yticks(lats)
ax.set_yticklabels(new_y_axis)

# finally, plot the solar declination angle along the x-y axis
pylab.plot(Y,D,'k--',linewidth=1.0,dashes=(5,5))
pylab.text(70,106,'Solar Declination',rotation=26)

# show the plot
pylab.show()
