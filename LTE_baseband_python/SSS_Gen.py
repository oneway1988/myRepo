# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:33:06 2018

@author: exabefa
"""

import numpy as np
import matplotlib.pyplot as plt

def sss_gen(NID1,NID2):
    if NID2 not in [0,1,2]:
        print("error:NID2 is out of [0,1,2]")
    if NID1 not in range(0,168):
        print("error:NID1 is out of range(0~167)")
    q_prime = np.floor(NID1/30)
    q = np.floor((NID1+q_prime*(q_prime+1)/2)/30)
    m_prime = NID1+q*(q+1)/2
    m0 = np.mod(m_prime,31) 
    m1 = np.mod((m0+np.floor(m_prime/31)+1),31)
    # =============================================================================
    # ======== Generate d_even()
    # =============================================================================
    # Generate the sequence x_s() : x() for calculating s_tilda()
    x_s = np.zeros(31)
    x_s[0:5] = [0,0,0,0,1]
    for i in range(0,26):
        x_s[i+5] = np.mod(x_s[i+2]+x_s[i],2)
    # Generate the sequence s_tilda()
    s_tilda = 1-2*x_s
    # Generate the sequence x_c() : x() for calculating c_tilda()
    x_c = np.zeros(31)
    x_c[0:5] = [0,0,0,0,1]
    for i in range(0,26):
        x_c[i+5] = np.mod(x_c[i+3]+x_c[i],2)
    # Generate the sequence c_tilda()
    c_tilda = 1-2*x_c
    # Generate the sequence x_z() : x() for calculating z_tilda()
    x_z = np.zeros(31)
    x_z[0:5] = [0,0,0,0,1]
    for i in range(0,26):
        x_z[i+5] = np.mod(x_z[i+4]+x_z[i+2]+x_z[i+1]+x_z[i],2)
    # Generate the sequence z_tilda()
    z_tilda = 1-2*x_z
    
    # Generate s0_m0 and s1_m1
    s0_m0 = np.zeros(31)
    s1_m1 = np.zeros(31)
    for n in range(0,31):
        s0_m0[n] = s_tilda[int(np.mod(n+m0,31))]
        s1_m1[n] = s_tilda[int(np.mod(n+m1,31))]
    
    # Generate c0() and c1()
    c0 =  np.zeros(31)
    c1 =  np.zeros(31)
    for n in range(0,31):
        c0[n] = c_tilda[int(np.mod(n+NID2,31))]
        c1[n] = c_tilda[int(np.mod(n+NID2+3,31))]
     
    # Generate z1_m0() and z1_m1()
    z1_m0 =  np.zeros(31)
    z1_m1 =  np.zeros(31)
    for n in range(0,31):
        z1_m0[n] = z_tilda[int(np.mod(n+np.mod(m0,8),31))]
        z1_m1[n] = z_tilda[int(np.mod(n+np.mod(m1,8),31))]
        
    # Generate SSS for subframe0 and subframe5
    sss_subf0 = np.zeros(62)
    sss_subf5 = np.zeros(62)
    for i in range(0,31):
        sss_subf0[2*i] = s0_m0[i]*c0[i]
        sss_subf0[2*i+1] = s1_m1[i]*c1[i]*z1_m0[i]
        sss_subf5[2*i] = s1_m1[i]*c0[i]
        sss_subf5[2*i+1] = s0_m0[i]*c1[i]*z1_m1[i]
    return sss_subf0,sss_subf5

if __name__ == '__main__' :
    Nid1 = 167    # 0~167
    Nid2 = 1    # 0~2   
    CellId = Nid1*3+Nid2
    sss_0,sss_5 = sss_gen(Nid1,Nid2)
    plt.figure(1)
    plt.plot(np.real(sss_0),np.imag(sss_0),'ro')
    plt.title("CellID=%d "%(CellId)+ "Subfame0 SSS Constellation")
    plt.figure(2)
    plt.plot(sss_0,'ro-')
    plt.title("Subfame0 SSS Sequences")
    
