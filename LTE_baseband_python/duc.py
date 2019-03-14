# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:16:02 2018

@author: exabefa
"""
import baseband as bb
import filterbranch as fb
import cmath
import numpy as np

#%%
'''
Digtal Up Convertion
Input: ([carrierIQ0,carrierIQ1,...,], [NCO0,NCO1,...,], sample rate)
Output: (duc IQ out, sample rate)
Note: NCO unit is Hz
'''
def duc(bbIQ_list,NCO_list,fs):
    dataout = np.zeros([len(bbIQ_list[0])],dtype=complex)
#    idx = 0
    for idx in range(len(bbIQ_list)):
#        frq_shift = np.zeros([len(bbIQ)],dtype=complex)
        frq_shift = np.exp(1j*2*cmath.pi*(NCO_list[idx]/fs)*np.arange(len(bbIQ_list[idx])))
#        for k in range(0,len(bbIQ)):
#            frq_shift[k] = cmath.exp(1j*2*cmath.pi*(NCO_list[idx]/fs)*k)
        dataout = dataout + bbIQ_list[idx] * frq_shift
#        idx = idx + 1
    return dataout,fs
#%%

if __name__ == '__main__' :
    bbIQ,sr = bb.baseband_Gen("64QAM",20,1)
    bbIQf = fb.channelfir(bbIQ)
    bbIQ2x,sr = fb.upsampling_2x(bbIQf,sr)
    bbIQ4x,sr = fb.upsampling_2x(bbIQ2x,sr)
    
    bbduc,sr = duc([bbIQ4x,bbIQ4x,bbIQ4x],[-20000000,0,20000000],sr)
    
    bb.PSD_Disp(bbduc,sr)