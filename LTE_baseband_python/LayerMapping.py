# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:30:54 2018

@author: exabefa
"""
import numpy as np


def layerMap(d,v):
    q, M_max_symb= d.shape
    if ((v == 1) & (q == 1)) or ((v == 2) & (q == 2)):
        M_layer_symb = M_max_symb
        x = np.zeros([v,M_layer_symb],dtype=complex)
        x = d
    elif (v == 2) & (q == 1):
        M_layer_symb = int(M_max_symb/2)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,2*i] 
            x[1,i] = d[0,2*i+1]
    elif (v == 3) & (q == 1):
        M_layer_symb = int(M_max_symb/3)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,3*i] 
            x[1,i] = d[0,3*i+1]
            x[2,i] = d[0,3*i+2]
    elif (v == 3) & (q == 2):
        M_layer_symb = int(M_max_symb/2)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,i] 
            x[1,i] = d[1,2*i]
            x[2,i] = d[1,2*i+1]
    elif (v == 4) & (q == 1):
        M_layer_symb = int(M_max_symb/4)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,4*i] 
            x[1,i] = d[0,4*i+1]
            x[2,i] = d[0,4*i+2]
            x[3,i] = d[0,4*i+3]
    elif (v == 4) & (q == 2):
        M_layer_symb = int(M_max_symb/2)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,2*i] 
            x[1,i] = d[0,2*i+1]
            x[2,i] = d[1,2*i]
            x[3,i] = d[1,2*i+1]        
    elif (v == 5) & (q == 2):
        M_layer_symb = int(M_max_symb/3)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,2*i] 
            x[1,i] = d[0,2*i+1]
            x[2,i] = d[1,3*i]
            x[3,i] = d[1,3*i+1]
            x[4,i] = d[1,3*i+2]
    elif (v == 6) & (q == 2):
        M_layer_symb = int(M_max_symb/3)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,3*i] 
            x[1,i] = d[0,3*i+1]
            x[2,i] = d[0,3*i+2]
            x[3,i] = d[1,3*i]
            x[4,i] = d[1,3*i+1]
            x[5,i] = d[1,3*i+2]
    elif (v == 7) & (q == 2):
        M_layer_symb = int(M_max_symb/4)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,3*i] 
            x[1,i] = d[0,3*i+1]
            x[2,i] = d[0,3*i+2]
            x[3,i] = d[1,4*i]
            x[4,i] = d[1,4*i+1]
            x[5,i] = d[1,4*i+2]
            x[6,i] = d[1,4*i+3]
    elif (v == 8) & (q == 2):
        M_layer_symb = int(M_max_symb/4)
        x = np.zeros([v,M_layer_symb],dtype=complex)
        for i in range(0,M_layer_symb):
            x[0,i] = d[0,4*i] 
            x[1,i] = d[0,4*i+1]
            x[2,i] = d[0,4*i+2]
            x[3,i] = d[0,4*i+3]
            x[4,i] = d[1,4*i]
            x[5,i] = d[1,4*i+1]
            x[6,i] = d[1,4*i+2]
            x[7,i] = d[1,4*i+3]
    else:
        print("Error:invaid layer number or codeword number")
        x = 0
    return x
    
if __name__ == '__main__' :

    d = np.random.random_sample([2,12])
    v = 8
    x1 = layerMap(d,v)