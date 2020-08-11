import numpy as np 
import bias
import charge
#this file reads all the raw data analyze it 
#creating new files with the information

#define all the values needed for the functions and import all the two needed modules

points=1024
#points in each waveform
time_spacing=0.4
window_integration=220
#size of the integration window for the charge
resistance=1000
waveforms_5=100000
#number of waveforms

time=np.arange(0,(points*time_spacing),time_spacing)
#creating the time array with the points and time spacing specifications

#open all the files needed to save the information analyze

charges=open('charge_5_bi.csv','w')
#file for charges of the waveforms
charges_max=open('charge_max_5_bi.csv','w')
#file for max charge of each waveform
base_line=open('base_line_5_bi.csv','w')
#file for baseline of each waveform
voltage_base=open('volt_base_5_bi.csv','w')
#file for amplituesof the waveforms
volts_max=open('volts_max_ch_5_bi.csv','w')
#file for teh max amplitude of each waveform
time_ch=open('time_max_ch_5_bi.csv','w')
#file for the time when the max charge of each waveform occur
time_v=open('time_max_v_5_bi.csv','w')
#file for the time when the max amplitude of each waveform occur
max_all_time=open('max_ch_v_and_time.csv','w')
#file joining the baseline, the max amplitude, the time the max amplitude occur
#the max charge and the time when the max charge occur
charges_maxx=[]
base_linee=[]
volts_maxx=[]
time_chh=[]
time_vv=[]

for waveform in range (waveforms_5):
    print(waveform)
   
    start=waveform*points
    
    ini=np.loadtxt('trigger_-5.csv',skiprows=start, max_rows=points)
    #initial reading of the raw data file one waveform at a time

    volts=(ini*-1)*2
    #inverse polarity and correct for the impedance of the oscilloscope

    base=bias.bias(voltage=volts, slope=points)
    #find the baseline
    #input list of amplitudes and the number of points in a waveform. 
    base_line.write(str(base)+'\n')
    base_linee.append(base)
    #write baseline to file

    volts_base, voltage_max, time_max_v=bias.voltage_base_and_max(volts=volts,bias=base, time_spacing=time_spacing)
    #get an array of voltages without the baseline, get the maximum amplitude of that array and the time when that happens
    #input list of amplitudes, baseline calculated and the time spacing
    np.savetxt(voltage_base,volts_base)
    volts_max.write(str(voltage_max)+'\n')
    time_v.write(str(time_max_v)+'\n')
    volts_maxx.append(voltage_max)
    time_vv.append(time_max_v)
    #write everything to its respective file

    charge, charge_max, time_max_ch=charge.charge(window=window_integration, time=time, volts=volts_base, resistance=resistance, time_spacing=time_spacing, points=points)
    # get an array of charge, the maximum charge in that array and the time when that happens
    #input the size of the window of integration, a list of the corrected amplitudes, the list of time, the time spacing, the value of resistance and the number of points in a waveform
    np.savetxt(charges, charge)
    charges_max.write(str(charge_max)+'\n')
    time_ch.write(str(time_max_ch)+'\n')
    charges_maxx.append(charge_max)
    time_chh.append(time_max_ch)
    #write everything to its respective file

number_waveform=np.arange(0,1,1)
np.savetxt(max_all_time, np.column_stack((number_waveform,base_linee,volts_maxx,time_vv,charges_maxx,time_chh)),delimiter=',',header='Waveform, Baseline (mV), Maximum Amplitude (mV), Time of max amplitude (ns), Max Charge (pC), Time of max charge (ns)')
# save the max amplitude, the time when the max amplitude happens, the max charge and the time when it happens and the wavefomr of each data all in one file

charges.close()
charges_max.close()
base_line.close()
voltage_base.close()
volts_max.close()
time_ch.close()
time_v.close() 
max_all_time.close()

