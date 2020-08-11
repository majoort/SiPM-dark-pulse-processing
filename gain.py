import numpy as np
from scipy.special import gamma, factorial
#the purpose of this library is to calculate factorials and gamma functions
import matplotlib.pyplot as plt
#the purpose of this library is to plot 
import math
from scipy.optimize import curve_fit
#the purpose of this library is to make the fitting
#import needed libraries

#The purpose of the code file is to make a fit on the histogram of total charge
# in order to obtain the gain 

def fit(x,k,theta,mean1,std1,mean2,std2,mean3,std3,mean4,std4,A,B,C,D,E):
    #this function is for creating all the functions for the fitting of the histogram
    #it contains one gamma distribution and 4 gaussian distributions, it returns all of this functions added 
    #Each function has its own amplitude

    gamma_s=(1/(gamma(k)*theta**k))*(np.power(x,(k-1)))*(np.exp(np.divide((-1*x),theta)))
    #the expression for the gamma distribution
    gauss_1=((1/std1*math.sqrt(2*math.pi))*np.exp((-1/2)*((x-mean1)/std1)**2))
    gauss_2=(((1/std2*math.sqrt(2*math.pi))*np.exp((-1/2)*((x-mean2)/std2)**2)))
    gauss_3=((1/std3*math.sqrt(2*math.pi))*np.exp((-1/2)*((x-mean3)/std3)**2))
    gauss_4=((1/std4*math.sqrt(2*math.pi))*np.exp((-1/2)*((x-mean4)/std4)**2))
    #the expresions for the four gaussian distributions

    return (A*gamma_s)+(B*gauss_1)+(C*gauss_2)+(D*gauss_3)+(E*gauss_4)


charge_max=np.loadtxt('charge_25.csv')
#read the file with the information of the maximum charge of all the waveforms. 

print('Number of waveforms'+ str(charge_max.size))
#print the number of waveforms that will be part of the histogram 

n,bins,patches=plt.hist(charge_max, bins=100, range=(0.5,2.5), edgecolor='black')
#get hte information for the histogram there are 100 bins in this histogram and 
#the range of the histogram goes from 0.5 to 2.5
#n is the size of the bins i.e. the counts
#bins contains the starting and end point of each bin ( the thickness)

middle=[]
for j in range(len(bins)-1):
    middle.append((bins[j]+bins[j+1])/2)
    #add the start plus the end of each bin and divide by two
middle_np=np.array(middle)
#this process gets the middle value of each bin which means the value of each bin

parameters, covariance=curve_fit(fit, middle_np,n, bounds=([0.4,0,0.60,0,0.80,0,1.07,0,1.28,0,0,0,0,0,0],[9,3,0.7,1,0.95,1,1.1,1,1.30,1,500,500,500,500,500]))
#this function is inherit from scipy.optimize it is where the function is fitted
#the first output is a list with the parameters of the fit, 
# the second output is a list of covarience of each of the parameters it is used to obtain the standar deviation of each of the parameters
#The first list of the boundaries variable contains the starting point where the parameters should be look for
#the second list represents the ending point
#The boundaries for the gamma distribution theta and k are choosen based on the posible parameters according to the wikipedia page on gamma distributions
#the boundaries for the mean of the gaussian distributions are choosen after generating the histogram and lokking around which values the peaks are positioned 
#the boundaries for the all the standard deviations are between 0 and 1 
#the order of the boundaries follows the order on how the parameter are accepted by pour fit function

errors= np.sqrt(np.diag(covariance))
#This commandis to transform the lists of covariences into a list of stadard deviations for each parameter

#Next are the steps to get the coefficient of determination to get the goodness of the fit

ss_res=np.sum((n - fit(middle_np,*parameters)) ** 2)
#sum of squares of residuals
ss_tot=np.sum((n - np.mean(n)) ** 2)
#total sum of squares

r2=1-(ss_res/ss_tot)
#calculation of the coefficient of determination

print('Parameters of gama function ')
print('Shape parameter (k) '+str(parameters[0])+'+/-' +str(errors[0]))
print('Scale parameter (theta) '+str(parameters[1])+'+/-'+str(errors[1]))
print('Amplitude '+str(parameters[10])+'+/-'+str(errors[10]))
print(' \n Parameters of first gamma function ')
print('mean '+str(parameters[2])+'+/-'+str(errors[2]))
print('standard deviation '+str(parameters[3])+'+/-'+str(errors[3]))
print('Amplitude '+str(parameters[11])+'+/-'+str(errors[11]))
print(' \n Parameters of second gamma function ')
print('mean '+str(parameters[4])+'+/-'+str(errors[4]))
print('standard deviation '+str(parameters[5])+'+/-'+str(errors[5]))
print('Amplitude '+str(parameters[12])+'+/-'+str(errors[12]))
print(' \n Parameters of third gamma function ')
print('mean '+str(parameters[6])+'+/-'+str(errors[6]))
print('standard deviation '+str(parameters[7])+'+/-'+str(errors[7]))
print('Amplitude '+str(parameters[13])+'+/-'+str(errors[13]))
print(' \n Parameters of fourth gamma function ')
print('mean '+str(parameters[8])+'+/-'+str(errors[8]))
print('standard deviation '+str(parameters[9])+'+/-'+str(errors[9]))
print('Amplitude '+str(parameters[14])+'+/-'+str(errors[14]))
#All of this is to display the parameters in the terminal later they will be saved to a file 

print('\n'+' Coefficient of determination '+str(r2))
#display the coeficient of determination


rows=['Shape parameter (k)','Scale parameter (theta)','mean 1', 'standard deviation 1', 'mean 2','standard 2','mean 3','standard 3','mean 4','standard 4', 'amplitude gamma', 'amplitude 1','amplitude 2', 'amplitude 3','amplitude 4']
t=np.column_stack((rows,parameters, errors))
np.savetxt('gain_fit_parameters.csv', t,delimiter=',',header=' , parameters, +/- error',fmt='%s')
#save all the parameters with their error to one file 
# the name of the file is gain_fit_parameters.csv

coefficient=open('gain_fit_parameters.csv','a')
coefficient.write('\n'+'R^2= '+str(r2)+'\n')
coefficient.close()
#save the coefficient of determination to the same file as the parameters

plt.xlabel('Charge (pC)')
plt.ylabel('Counts')
plt.grid()
plt.title('Histogram of total charge')
plt.plot(middle,fit(middle_np,*parameters),'r-')
#plot the fitting on the histogram 
plt.savefig('histogram_gain.png')
#save histogram
plt.show()
#display the plot of the histogram with the fit in red









