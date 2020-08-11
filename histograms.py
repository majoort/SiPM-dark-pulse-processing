import numpy as np
import matplotlib.pyplot as plt
#import the libraries needed to display the graphs

#The purpose of this code is to display and save the histograms for max charge and max amplitude

charge_max=np.loadtxt('charge_max_5_bi.csv')
voltage_base_max=np.loadtxt('volts_max_ch_5_bi.csv')
baseline_max=np.loadtxt('base_line_5_bi.csv')
#read the necesary files for the graphs, max charges, max amplitudes and baseline

array_voltage_base=voltage_base_max.tolist()
plt.hist(voltage_base_max, edgecolor='black', bins=100, range=(11,35))
#make a histogram with the max amplitudes, the number of bins in this histogram is 100
#by having a previous look at the histogram it was determine that the main information was in the range of 
#11 to 35 this range is set for 35,000 waceforms
plt.xlabel('Voltage (mV)')
plt.ylabel('Counts')
plt.title('Histogram of Amplitudes')
plt.grid()
print('\n Histogram size data '+str(voltage_base_max.size))
#print the number of waveforms to construct this graph 
print('Max Amplitude '+str(voltage_base_max.max()))
#display the max amplitude among all the waveforms
print('Waveform of max amplitude '+str(array_voltage_base.index(voltage_base_max.max())))
#display the number of the waveform when the max amplitude occur
print('Baseline of max amplitude '+str(baseline_max[array_voltage_base.index(voltage_base_max.max())]))
#display the baseline of the waveform when the max amplitude occur
plt.savefig('max_voltage_base_histogram_5.png')
#save histogram
plt.show()
#display histogram

array_charge=charge_max.tolist()
plt.hist(charge_max, bins=100,range=(0.5,2.5), edgecolor='black')
# make the histogram with the max charges, the number of bins in this histogram is 100
#by having a previous look at the histogram it was determine that the main information was in the range of 
#0.5 to 2.5 this range is set for 35,000 waceforms
plt.xlabel('Charge (pC)')
plt.ylabel('Counts')
plt.title('Histogram Charge')
plt.grid()
print('\n Histogram size data '+str(charge_max.size))
#print the number of waveforms to construct this graph 
print('Total charge '+str(charge_max.max()))
#display the max xharge among all the waveforms
print('Waveform of total charge '+str(array_charge.index(charge_max.max())))
#display the number of waveform when the max charge occur
print('Baseline of total charge '+str(baseline_max[array_charge.index(charge_max.max())]))
#display the baseline of the waveform when the max charge occur
plt.savefig('max_charge_histogram_5.png')
#save the histogram
plt.show()
#display the histogram
