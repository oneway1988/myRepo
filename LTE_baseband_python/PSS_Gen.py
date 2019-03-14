# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:46:36 2018

@author: exabefa
"""

import numpy as np
import matplotlib.pyplot as plt
import WhiteGaussianNoise as wg

def pss_gen(NID):
    u = {0:25,1:29,2:34}
    pss = np.zeros([62],dtype=complex)
    if NID not in [0,1,2]:
        print("error:NID2 is out of range[0,1,2]")
    for n in range(0,31):
        pss[n] = np.exp(-1j*np.pi*u[NID]*n*(n+1)/63)
    for n in range(31,62):
        pss[n] = np.exp(-1j*np.pi*u[NID]*(n+1)*(n+2)/63)
    return pss

if __name__ == '__main__' :
        
    NID0_PSS = pss_gen(0)
    plt.figure(1)
    plt.plot(np.real(NID0_PSS),np.imag(NID0_PSS),'ro')
    
# =============================================================================
# Correlation between a PSS and its PhaseShifted Version, estimate phase shift
# =============================================================================
    
    # no phase shift
    xcorr = np.correlate(NID0_PSS,NID0_PSS,'full')
    abs_xcorr = np.abs(xcorr)
    angle_xcorr = np.angle(xcorr)
    plt.figure(2)
    plt.subplot(2,1,1)
    plt.plot(abs_xcorr,'o-')
    plt.title("No Phase Shift")
    plt.ylabel('Abs corr')
    plt.subplot(2,1,2)
    plt.plot(angle_xcorr,'ro')
    plt.xlabel('Samples')
    plt.ylabel('Angle corr')
    
    # phase shift
    phase_shift = np.pi/3
    NID0_PSS_phshift = NID0_PSS*np.exp(-1j*phase_shift)

    xcorr_phshift = np.correlate(NID0_PSS,NID0_PSS_phshift,'full')
    abs_xcorrph = np.abs(xcorr_phshift)
    angle_xcorrph = np.angle(xcorr_phshift)
    
    # retuen index where maximum abs of correlation is
    index_max = np.argmax(abs_xcorrph)
    esti_phshift = angle_xcorrph[index_max]
    
    plt.figure(3)
    plt.subplot(2,1,1)
    plt.plot(abs_xcorrph,'o-')
    plt.title("Phase Shift %f"%(phase_shift))
    plt.ylabel('Abs corr')
    plt.subplot(2,1,2)
    plt.plot(angle_xcorrph,'ro')    
    plt.xlabel('Samples')
    plt.ylabel('Angle corr')
    
# =============================================================================
# Correlation between a PSS and its Noised Version
# =============================================================================
    snr = 3
    WGNoise = wg.WGN(NID0_PSS,snr)
    NID0_PSS_WGN = NID0_PSS + WGNoise
    plt.figure(4)
    plt.plot(NID0_PSS.real,NID0_PSS.imag,'ro')
    plt.plot(NID0_PSS_WGN.real,NID0_PSS_WGN.imag,'bo')
    plt.legend(('PSS no SNR', 'PSS %ddB SNR '%(snr)),loc='upper center')
    plt.title("NID=0 Origenal PSS and Noised PSS")
    
    xcorr_noise = np.correlate(NID0_PSS,NID0_PSS_WGN,'full')
    abs_xcorr_noise = np.abs(xcorr_noise)
    angle_xcorr_noise = np.angle(xcorr_noise)
    plt.figure(5)
    plt.subplot(2,1,1)
    plt.plot(abs_xcorr_noise,'o-')
    plt.title("PSS with Noise")
    plt.ylabel('Abs corr')
    plt.subplot(2,1,2)
    plt.plot(angle_xcorr_noise,'ro')
    plt.xlabel('Samples')
    plt.ylabel('Angle corr')