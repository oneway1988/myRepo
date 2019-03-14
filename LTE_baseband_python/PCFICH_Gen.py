# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:23:33 2018

@author: exabefa
"""

import numpy as np
import modulation as mod
import DL_RS as rs
import matplotlib.pyplot as plt
import LayerMapping as lm

def cfi_map(CFI):
    CFI_bits = np.zeros(32,dtype=int)
    if CFI == 1:
        CFI_bits = [0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1]
    elif CFI == 2:
        CFI_bits = [1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0]
    elif CFI == 3:
        CFI_bits = [1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1]   
    elif CFI == 4:
        CFI_bits = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    else:
        print("Error:invalid CFI")
    return CFI_bits

def pcfich_gen(CFI_bits,N_S,NID_cell):
    # Scrambling 
    c_init = (np.floor(N_S/2)+1)*(2*NID_cell+1)*512+NID_cell
    c = rs.prs_gen(32,c_init)
    bit_scrambling = np.zeros(32, dtype=int)
    bit_scrambling = np.mod(CFI_bits+c,2)
    # Modulation QPSK
    d = np.zeros(16, dtype=complex)
    d= mod.mod_map(bit_scrambling,"QPSK")
    # Layer Mapping
    
    
    return d

if __name__ == '__main__' :
    
    CFI = 1
    CFI_bits = cfi_map(CFI)
    N_S = 0
    NID_cell = 0
    pcfich = pcfich_gen(CFI_bits,N_S,NID_cell)
    x = lm.layerMap(np.reshape(pcfich,[1,16]),4)
    
    
    plt.plot(x.real,x.imag,'ro')
    plt.title("Constellation of PCFICH" )