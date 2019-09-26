#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:08:33 2018
Potentiometer plot only displacement for the in-class demontrations

What it does:
    -- Shows real time data from the potentiometer
    -- Save a .txt output file for later usage

-- to do --
- calculate velocity of the slider
@author: marcoscuderi
"""

import serial       # you have to install this package
import numpy as np
import matplotlib.pyplot as plt
import drawnow      # you have to install this package


# create a function to create a figure to plot real time data
def makeFig():
    plt.title('Block displacement: %.2f [cm] rec rate = %s[Hz]'%(disp,int(recRate)))
    plt.plot(timeData,dispData,'ko--')
    plt.ylabel('Block displacement, cm',fontsize=14)
    plt.xlabel('Time, s',fontsize=14)
    plt.ylim([0,16])

####### create a file to write the data ###########
fileName='exp1'
write_to_file_path = "/your path directory/%s.txt"%fileName
output_file = open(write_to_file_path, "w+")

#####################################################################


print 'PROGRAM STARTS'
##### set-up serial comunication #####
arduinoPort ='/dev/cu.usbmodem1451' # make sure this is the same serial port as the arduino is using
baudRate    = 115200
arduinoStream = serial.Serial(arduinoPort,baudRate)

##### set up variable to use in the loop #####
# this correspond to the data array for plotting #
timeData=[]
recNumData=[]
voltData=[] # do not really need
dispData=[]
##### initialize points to read in plot ####
xWindow = 200
count = 0
#### potentiometer calibration ####
potCal = 0.33 #[V/cm]
##### inizialize figure ####
plt.ion()
fig=plt.figure(2,figsize=(12,12))

while True:
    if (arduinoStream.inWaiting==0): # wait data from Arduino
        pass
    arduinoData = arduinoStream.readline() # read data from aeduino
    data = arduinoData.strip('\r\n') # take off the final characters
    data = arduinoData.split(',')    # divide by delimiter

    recRate = float(data[3])

    recNum = int(data[0])
    time = recNum / recRate #[s]

    #time_in = float(data[1])
    #time_in = time_in*0.001 #ms to s
    volt = float(data[2])
    disp = volt/0.33


    #velocity = (disp*1000)/time do better 
    timeData.append(time) # put real time values in array
    #recNumData.append(recNum)
    dispData.append(disp)
    #velData.append(velocity)

    drawnow.drawnow(makeFig,stop_on_close=True)
    plt.pause(0.000001)

    if count>xWindow:
        #timeData.pop(0)
        dispData.pop(0)
        timeData.pop(0)
        #velData.pop(0)
    # save data to .txt file
    output_file.write(arduinoData)
    output_file.flush()
    count+=1
