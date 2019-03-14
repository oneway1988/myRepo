# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:49:41 2018

@author: exabefa
"""
import math
import duc
import baseband as bb
import filterbranch as fb
import numpy as np
import matplotlib.pyplot as plt

bbIQ0,sr0 = bb.baseband_Gen("64QAM",20,1)
plt.figure(0)
bb.PSD_Disp(bbIQ0,sr0)
power = bbIQ0.real **2 + bbIQ0.imag **2
power = np.sort(power)
b = len(power)
a = int(len(power)*0.9999)
r = power[a]
papr = 10 * math.log((r / np.mean(power)),10)
papr1 = 10 * math.log((power[int(len(power)*0.9999)] / np.mean(power)),10)