# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:40:25 2018

@author: exabefa
"""

import os
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

os.system('cls')
#%% 
'''
modulation function
input:(modulation method),support "QPSK","16QAM" and "64QAM"
output:(constellation mapping integer,constellation mapping arrary)
'''
def mod_Para(mod_method):
    if mod_method == "QPSK":
        mod_src = 4
        norm = np.sqrt(1/2)
        const_re = np.array([1, 1, -1, -1])
        const_im = np.array([1, -1, 1, -1])
        mod_set = norm * (const_re + 1j*const_im)
    elif mod_method == "16QAM":
        mod_src=16
        norm = np.sqrt(1/10)
        const_re = np.array([1, 1, 3, 3, 1, 1, 3, 3, -1, -1, -3, -3, -1, -1, -3, -3])
        const_im = np.array([1, 3, 1, 3, -1, -3, -1, -3, 1, 3, 1, 3, -1, -3 ,-1, -3])
        mod_set = norm * (const_re + 1j*const_im)
    elif mod_method == "64QAM":
        mod_src=64
        norm = np.sqrt(1/42)
        const_re = np.array([3,3,1,1,3,3,1,1,5,5,7,7,5,5,7,7,3,3,1,1,3,3,1,1,5,5,7,7,5,5,7,7,-3,-3,-1,-1,-3,-3,-1,-1,-5,-5,-7,-7,-5,-5,-7,-7,-3,-3,-1,-1,-3,-3,-1,-1,-5,-5,-7,-7,-5,-5,-7,-7])
        const_im = np.array([3,1,3,1,5,7,5,7,3,1,3,1,5,7,5,7,-3,-1,-3,-1,-5,-7,-5,-7,-3,-1,-3,-1,-5,-7,-5,-7,3,1,3,1,5,7,5,7,3,1,3,1,5,7,5,7,-3,-1,-3,-1,-5,-7,-5,-7,-3,-1,-3,-1,-5,-7,-5,-7])
        mod_set = norm * (const_re + 1j*const_im)
    else:
        print("error: unknown modulation type")
        return 0,0
    return mod_src,mod_set
#%% 
'''
Baseband IQ generation function
input:(modulation method, bandwidth, number of frames)
output:(Baseband IQ stream, sample rate)
'''
def baseband_Gen(mod_method,BW,numofframe):
#    print("Run baseband_Gen")
    numofSC = BW * 60     # sub-carrir number in one OFDM symbol
    CP1 = BW * 8    # CP length in first OFDM symbol
    CP2 = int(BW * 7.2)  # CP length in other OFDM symbols
    fftSize = int(BW / 10 * 1024)    # FFT size
    numofsubf_frame = 10
    numofsymb_subframe = 14
    totalsymb = numofframe * numofsubf_frame * numofsymb_subframe
    
    (mod_src,mod_set) = mod_Para(mod_method)    # Generate constellation map
    SC_data = np.random.randint(0,mod_src,[numofSC,totalsymb])  # Generate data sub-carrier for all frame
    FDinput = mod_set[SC_data]  # Generate frequence domain data by Mapping data with constellation map
    # Generate data for ifft input, fill 0 to none data sub-carriers
    IFFTinput = np.vstack((np.zeros([1,totalsymb]),FDinput[int(numofSC/2):,:],np.zeros([(fftSize-numofSC-1),totalsymb]),FDinput[0:int(numofSC/2),:])) 
    # Generate time domain data by IFFT process
    TDinput = np.fft.ifftn(IFFTinput)
    
    
    
    bbIQ = np.zeros([1,1])  # initial baseband IQ data stream
    for symbIdx in range(0,totalsymb):
        if symbIdx % 7 == 0:
            cp = np.reshape(TDinput[(fftSize-CP1):,symbIdx],[CP1,1])    # CP for first symbol in a slot
        else:
            cp = np.reshape(TDinput[(fftSize-CP2):,symbIdx],[CP2,1])    # CP for other symbols
        data = np.reshape(TDinput[:,symbIdx],[fftSize,1])   # Extract data for one symbol
        bbIQ = np.vstack((bbIQ,cp,data))    # Combine CP and data
    bbIQ = bbIQ[1:,0]
    sampleRate = 1000 * bbIQ.shape[0] / (numofframe*10)
    return bbIQ,sampleRate
#%% 
'''
spectrum display function
Input:(data with numpy array size(N,) , sample rate unit Hz)
Output:None
'''
def PSD_Disp(data,sr):
#    FDdata = np.fft.fftn(data)
#    FDdata_abs = np.fft.fftshift(abs(FDdata))
#    axis = np.linspace((-sr/2)/1000000,(sr/2-1)/1000000,num=FDdata_abs.shape[0])
#    plt.title('Frequency Spectrum')
#    plt.xlabel('MHz')
#    plt.plot(axis,FDdata_abs)
    
    plt.psd(data,NFFT=2048,Fs=sr,window=mlab.window_none,scale_by_freq=True)
    
#    f, Pper_spec = signal.periodogram(data, sr, 'flattop',return_onesided=False)
#    plt.semilogy(f, Pper_spec)
#    plt.xlabel('frequency [Hz]')
#    plt.ylabel('PSD')
#    plt.show()
#%%
if __name__ == '__main__' :
    (bbIQ,sr) = baseband_Gen("16QAM",20,1)
    PSD_Disp(bbIQ,sr)

    