# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:59:44 2018

@author: exabefa
"""
import numpy as np
import matplotlib.pyplot as plt

def mod_map(bit_in,mod_method):
    if mod_method == "BPSK":
        mod_rank = 1
        norm = np.sqrt(1/2)
        const_re = np.array([1, -1])
        const_im = np.array([1, -1])
        
    elif mod_method == "QPSK":
        mod_rank = 2
        norm = np.sqrt(1/2)
        const_re = np.array([1, 1, -1, -1])
        const_im = np.array([1, -1, 1, -1])
        
    elif mod_method == "16QAM":
        mod_rank = 4
        norm = np.sqrt(1/10)
        const_re = np.array([1, 1, 3, 3, 1, 1, 3, 3, -1, -1, -3, -3, -1, -1, -3, -3])
        const_im = np.array([1, 3, 1, 3, -1, -3, -1, -3, 1, 3, 1, 3, -1, -3 ,-1, -3])
        
    elif mod_method == "64QAM":
        mod_rank = 6
        norm = np.sqrt(1/42)
        const_re = np.array([3,3,1,1,3,3,1,1,5,5,7,7,5,5,7,7,3,3,1,1,3,3,1,1,5,5,7,7,5,5,7,7,-3,-3,-1,-1,-3,-3,-1,-1,-5,-5,-7,-7,-5,-5,-7,-7,-3,-3,-1,-1,-3,-3,-1,-1,-5,-5,-7,-7,-5,-5,-7,-7])
        const_im = np.array([3,1,3,1,5,7,5,7,3,1,3,1,5,7,5,7,-3,-1,-3,-1,-5,-7,-5,-7,-3,-1,-3,-1,-5,-7,-5,-7,3,1,3,1,5,7,5,7,3,1,3,1,5,7,5,7,-3,-1,-3,-1,-5,-7,-5,-7,-3,-1,-3,-1,-5,-7,-5,-7])
        
    else:
        print("error: unsupported or unknown mod_map type")
    mod_set = norm * (const_re + 1j*const_im)
    symbol_len = int(len(bit_in)/mod_rank)
    symbol_tem = np.reshape(bit_in,(symbol_len,mod_rank))
    symbol_in = np.zeros(symbol_len,dtype=int)
    for n in range(0,symbol_len):
        for i in range(0,mod_rank):
            symbol_in[n] = symbol_in[n] + symbol_tem[n,i] * (2**(mod_rank-1-i))
    return mod_set[symbol_in]

if __name__ == '__main__' :
    mod_method = "16QAM"
    bit_input = np.random.randint(0,2,[3600])
    sym_out = mod_map(bit_input,mod_method)
    plt.plot(sym_out.real,sym_out.imag,'ro')
    plt.title("Constellation of " + mod_method)
