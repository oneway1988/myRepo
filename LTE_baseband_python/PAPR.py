# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:45:22 2018

@author: exabefa
"""
import math
import duc
import baseband as bb
import filterbranch as fb
import numpy as np
import matplotlib.pyplot as plt

def papr_Calc(datain):
    power = datain.real **2 + datain.imag **2
    ##papr = 10 * math.log((np.max(power) / np.mean(power)),10)
    power = np.sort(power)
    papr = 10 * math.log((power[int(len(power)*0.9999)] / np.mean(power)),10) ##0.00001 PAPR
    return papr

bbIQ0,sr0 = bb.baseband_Gen("64QAM",20,1)
bbIQ1,sr1 = bb.baseband_Gen("64QAM",20,1)

bbIQ_20M_0,sr0 = fb.firbranch_DL(bbIQ0,sr0)
bbIQ_20M_1,sr1 = fb.firbranch_DL(bbIQ1,sr1)

bbIQ_2x20M_20,sr3 = duc.duc([bbIQ_20M_0,bbIQ_20M_1],[-20000000,20000000],sr0)

plt.figure(0)
bb.PSD_Disp(bbIQ_2x20M_20,sr3)


papr_40 = papr_Calc(bbIQ_2x20M_20)
papr_20_0 = papr_Calc(bbIQ_20M_0)
papr_20_1 = papr_Calc(bbIQ_20M_1)


power = bbIQ_2x20M_20.real **2 + bbIQ_2x20M_20.imag **2
thrsh = np.mean(power) * math.pow(10,0.75)
plt.figure(1)
plt.plot(power)
plt.axhline(thrsh, color= 'r')

