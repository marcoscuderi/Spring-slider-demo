#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:59:31 2018

@author: marcoscuderi
"""

import numpy as np
import matplotlib.pyplot as plt
import fit as f

data = np.loadtxt('Calibration.txt', unpack=True)
slope = f.fit(data[0],data[1],1)


fig=plt.figure()
plt.title('potentiometer calibration')
plt.plot(data[0],data[1],'ro-')
plt.ylabel('Volt, V')
plt.xlabel(r'Displacement ($\delta$), cm')
plt.text(2,2,'The slope of this line is') 
plt.text(2,1.5,r'$\frac{\Delta V}{\Delta \delta}$ = %s [v/cm]'%(slope[2][1]))
         


