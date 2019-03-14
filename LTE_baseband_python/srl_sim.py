# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:52:06 2018

@author: exabefa
"""
import duc
import baseband as bb
import filterbranch as fb
import numpy as np
from scipy.stats import cumfreq
import matplotlib.pyplot as plt


def calc_SkewR(datain):
    datatep = datain[1::2]-datain[0::2]
    dataout = np.append(abs(datatep.real),abs(datatep.imag))
    return dataout

def disp_SkewRCDF(datain):
    
    N = 200  # number of samples 
    
    maxi = 0
    for idx in range(len(datain)):
        if np.max(datain[idx]) > maxi :
            maxi = np.max(datain[idx])
        else:
            pass
    plt.figure(1)
    plt.title('CDF')
    plt.grid(True)
    plt.ylabel('Probability')
    plt.xlabel('Skew Rate')
    for data in datain:
        cdf = cumfreq(data,N,defaultreallimits=(0,maxi))   
        plt.plot(np.linspace(0,maxi,N),cdf.cumcount/(len(data)))
    plt.show()
    
#    cdf0 = cumfreq(data0,N,defaultreallimits=(0,maxi))
#    cdf1 = cumfreq(data1,N,defaultreallimits=(0,maxi))
#    
#    plt.figure(1)
#    plt.title('CDF')
#    plt.grid(True)
#    plt.ylabel('Probability')
#    plt.xlabel('Skew Rate')
#    plt.plot(np.linspace(0,maxi,N),cdf0.cumcount/(len(data0)))
#    plt.plot(np.linspace(0,maxi,N),cdf1.cumcount/(len(data1)))
#    plt.show()
#        
    
bbIQ0,sr0 = bb.baseband_Gen("64QAM",10,1)
bbIQ1,sr1 = bb.baseband_Gen("64QAM",20,1)

bbIQ_122_10M,sr0 = fb.firbranch_DL(bbIQ0,sr0)
bbIQ_122_20M,sr1 = fb.firbranch_DL(bbIQ1,sr1)
bbIQ_245_20M,sr2 = fb.upsampling_2x(bbIQ_122_20M,sr1)

bbIQ_122_2x10M_5,sr3 = duc.duc([bbIQ_122_10M,bbIQ_122_10M],[-5000000,5000000],sr0)
bbIQ_122_2x10M_25,sr4 = duc.duc([bbIQ_122_10M,bbIQ_122_10M],[-25000000,25000000],sr0)
bbIQ_122_2x20M_20,sr5 = duc.duc([bbIQ_122_20M,bbIQ_122_20M],[-20000000,20000000],sr0)

plt.figure(0)
bb.PSD_Disp(bbIQ_122_10M,sr0)
bb.PSD_Disp(bbIQ_122_20M,sr1)
bb.PSD_Disp(bbIQ_122_2x10M_5,sr3)
bb.PSD_Disp(bbIQ_122_2x10M_25,sr4)
bb.PSD_Disp(bbIQ_122_2x20M_20,sr5)

skewR_122_10M = calc_SkewR(bbIQ_122_10M)
skewR_122_20M = calc_SkewR(bbIQ_122_20M)
skewR_245_20M = calc_SkewR(bbIQ_245_20M)
skewR_122_2x10M_5 = calc_SkewR(bbIQ_122_2x10M_5)
skewR_122_2x10M_25 = calc_SkewR(bbIQ_122_2x10M_25)
skewR_122_2x20M_20 = calc_SkewR(bbIQ_122_2x20M_20)

disp_SkewRCDF([skewR_122_10M,skewR_122_20M,skewR_122_2x10M_5,skewR_122_2x10M_25,skewR_122_2x20M_20])



#bbduc0,sr0 = duc.duc([bbIQ_122_10M],[0],sr0)
#bbduc1,sr1 = duc.duc([bbIQ_122_20M],[0],sr1)
#
#plt.figure(0)
#bb.PSD_Disp(bbduc0,sr0)
#bb.PSD_Disp(bbduc1,sr1)
#
#data0 = bbduc0[1::2]-bbduc0[0::2]
#data1 = bbduc1[1::2]-bbduc1[0::2]
#
#data0float = np.append(abs(data0.real),abs(data0.imag))
#data1float = np.append(abs(data1.real),abs(data1.imag))
#maxi0 = np.max(data0float)
#maxi1 = np.max(data1float)
#maxi = max(maxi0,maxi1)
#
#cdf0 = cumfreq(data0float,20,defaultreallimits=(0,maxi))
#cdf1 = cumfreq(data1float,20,defaultreallimits=(0,maxi))
#
#plt.figure(1)
#plt.title('CDF')
#plt.grid(True)
#plt.ylabel('Probability')
#plt.xlabel('Skew Rate')
#plt.plot(np.linspace(0,maxi,20),cdf0.cumcount/(len(data0float)))
#plt.plot(np.linspace(0,maxi,20),cdf1.cumcount/(len(data0float)))
#plt.show()





