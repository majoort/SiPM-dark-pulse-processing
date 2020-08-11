import numpy as np
import matplotlib.pyplot as plt
import array as arr
import scipy.integrate as integrate
import pandas as pd

charges=np.loadtxt('charge_30_1.csv', delimiter=',',usecols=1, skiprows=1)
volts_base=np.loadtxt('volt_base_30_1.csv', delimiter=',',usecols=1, skiprows=1)
vol=np.loadtxt('voltage_30_1.csv', delimiter=',',usecols=1, skiprows=1)
base=np.loadtxt('base_line_30_1.csv',delimiter=',',usecols=1, skiprows=1)
tim=[]
for k in range(0, 1024):
   tim.append(k*0.4)  

time=np.array(tim)
points=1024
waveform=int(input('Enter number of waveform '))
first=waveform*points
last=(waveform+1)*points
first_c=waveform*724
last_c=(waveform+1)*724
voltage=vol[first:last]
volts_bases=volts_base[first:last]
charge=charges[first_c:last_c]

array_charge=charge.tolist()
y=array_charge.index(charge.max())
tii=time[0:724]
plt.plot(time[0:724],charge)
plt.xlabel("Time (ns)")
plt.ylabel("Charge (pC)")
plt.title("Integration "+ str(waveform))
plt.grid()
print(str(waveform )+ " total charge "+ str(charge.max()))
print(str(waveform )+ " time of total charge "+ str(y*0.4))
print(str(waveform )+ " min charge "+str(charge.min()))
print(str(waveform )+" charge mean "+ str(charge.mean()))
print(str(waveform )+" time mean "+ str(tii.mean()))
print(str(waveform )+" charge standard deviation "+ str(charge.std()))
print(str(waveform )+" time standard deviation "+ str(tii.std()))
print(str(waveform )+ " size "+ str(charge.size))
plt.savefig('charge_waveform-30.png')
plt.show()

array_volt=voltage.tolist()
h=array_volt.index(voltage.max())
print(base[waveform])
print(str(waveform )+ " max amplitude "+ str(voltage.max()))
print(str(waveform )+ " time of max amplitude "+ str(h*0.4))
print(str(waveform )+ " min amplitude "+str(voltage.min()))
print(str(waveform )+" voltage mean "+ str(voltage.mean()))
print(str(waveform )+" time mean "+ str(time.mean()))
print(str(waveform )+" voltage standard deviation "+ str(voltage.std()))
print(str(waveform )+" time standard deviation "+ str(time.std()))
print(str(waveform )+ " size "+ str(voltage.size))
plt.plot(time, voltage, drawstyle='steps')
# def exponential (x, a, b, c):
#     return a*np.exp(-b*x)+c
#popt, pcov=curve_fit(exponential,time, vol)
#plt.plot(time,exponential(time, *popt), 'r--')
plt.grid()
plt.xlabel("Time (ns)")
plt.ylabel("Voltage (mV)")
plt.title("Waveform "+ str(waveform))
plt.savefig('voltage_waveform_-30.png')
plt.show()

array_volt_base=volts_bases.tolist()
h=array_volt_base.index(volts_bases.max())
print(str(waveform )+ " max amplitude "+ str(volts_bases.max()))
#print(str(waveform )+ " time of max voltage"+ str(h*0.4))
print(str(waveform )+ " min amplitude "+str(volts_bases.min()))
print(str(waveform )+" voltage mean "+ str(volts_bases.mean()))
print(str(waveform )+" time mean "+ str(time.mean()))
print(str(waveform )+" voltage standard deviation "+ str(volts_bases.std()))
print(str(waveform )+" time standard deviation "+ str(time.std()))
print(str(waveform )+ " size "+ str(volts_bases.size))
plt.plot(time, volts_bases, drawstyle='steps')
plt.xlabel("Time (ns)")
plt.ylabel("Voltage (mV)")
plt.title("Waveform base line "+ str(waveform))
plt.grid()
plt.savefig('voltage_baseline-30.png')
plt.show()

