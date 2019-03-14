# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:26:00 2018

@author: exabefa
"""
import baseband
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#%%
'''
Filter amplitudue response 
Input: filter coefficient
'''
def fir_ampresp(coef):
    w1, h1 = signal.freqz(coef)
    plt.title('Digital filter frequency response')
    plt.plot(w1, 20*np.log10(np.abs(h1)), 'b')
    plt.ylabel('Amplitude Response (dB)')
    plt.xlabel('Frequency (rad/sample)')
    plt.grid()
    plt.show()
#%%
'''
Channel filter  
Input: data before filtering with type numpy array size(N,)
Output: data after filtering
'''
def channelfir(datain):
    chanfir = np.loadtxt("chanfir20m.txt")
    #chanfir = signal.firwin2(95, [0.0, 20*0.9/30.72, 1.008*20/30.72, 1.0], [1.0, 1.0, 0.0, 0.0])
    #fir_ampresp(chanfir)
    dataout = signal.convolve(chanfir,datain)
    dataout = dataout[len(chanfir)-1:]
    return dataout
#%%
'''
2 times up sampling
Input: (data before up sampling, sample rate) 
Output: (data after up sampling,sample rate)
'''   
def upsampling_2x(datain,sr):
    hbcoef = np.loadtxt("hb2.txt")
    data_interp = np.zeros([len(datain)*2],dtype=complex)
    data_interp[0::2] = datain
    dataout = signal.convolve(hbcoef,data_interp)
    dataout = dataout[len(hbcoef)-1:]
    return dataout,sr*2
#%%
'''
Downlink filter branch
Input: data IQ
Output: 122.88Msps data IQ    
'''
def firbranch_DL(datain,sr):
    bbIQ = channelfir(datain)
    while int(122880000/sr) != 1:
        bbIQ,sr = upsampling_2x(bbIQ,sr)
    return bbIQ,int(sr)

#%%
if __name__ == '__main__' :
    (bbIQ,sr) = baseband.baseband_Gen("16QAM",10,1)
#    bbIQf = channelfir(bbIQ)
#    bbIQ2x,sr = upsampling_2x(bbIQf,sr)
#    bbIQ122,sr = upsampling_2x(bbIQ2x,sr)
    bbIQ122,sr = firbranch_DL(bbIQ,sr)
    baseband.PSD_Disp(bbIQ122,sr)
    