import numpy as np 
import scipy.integrate as integrate
import cmath
import math

#file contains the code for the window integration to get the charge of each waveform

def charge (window, time, volts,resistance, time_spacing, points):
    #this function returns the list of charge related to the voltage list, also the maximum charge and the time when it happens
    #the inputs of this function are the window size for the integration (in ns), 
    #the time array for the integration, the amplitude array for the integration,
    #the resistance to calculate the charge, the time spacing and the number of points in the waveform

    window_points=int(window/time_spacing)
    
    #calculation of the window size with respect to the number of points in the waveform

    points_charge=int(points-window_points)
  
    #the amount of points that are going to be in the charge array

    ch=[]
    for s in range (points_charge):
        I=integrate.simps(volts[s:s+window_points],time[s:s+window_points])
        #integration of the waveform 

        q=I/resistance
        #calculation of the charge

        ch.append(q)
        #append each individual charge to a list
    
    charges=np.array(ch)
    ch_max=charges.max()
    #get the max charge 
   
    time_max_ch=ch.index(ch_max)*time_spacing
    #time when the max charge occur

    return ch, ch_max, time_max_ch
