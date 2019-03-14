# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:21:35 2018

@author: exabefa
"""
import numpy as np  
import matplotlib.pyplot as plt

def WGN(inputSignal,SNR_dB):
    SNR_lin = 10**(SNR_dB/10.0)
    AvSigPower = np.mean(inputSignal.real**2+inputSignal.imag**2)
    NoisePower = AvSigPower/SNR_lin
    if inputSignal.dtype == 'complex':
        return np.random.randn(len(inputSignal))*np.sqrt(NoisePower)+1j*np.random.randn(len(inputSignal))*np.sqrt(NoisePower)
    else:
        return np.random.randn(len(inputSignal))*np.sqrt(NoisePower)

if __name__ == '__main__' :
    sin = np.zeros(100)
    for n in range(0,len(sin)):
        sin[n] = np.sin(n/10*np.pi)
        
    snr = 3.5
    sin_addnoise = WGN(sin,snr)+sin
    plt.plot(sin,'ro-' )
    plt.plot(sin_addnoise,'bo-')
    plt.legend(('Sin Wave', 'Sin with %fdB SNR noise'%(snr)),loc='upper center')
    