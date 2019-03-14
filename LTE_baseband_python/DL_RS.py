# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:14:16 2018

@author: exabefa
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Generate Pseudo-random sequences c[n]
# =============================================================================
def prs_gen(M_PN,c_init):
    N_C = 1600
    x2_init = int(c_init)
    # initialize x1[0:30]
    x1 = np.zeros([M_PN+N_C],dtype=int)
    x1[0] = 1
    # initialize x2[0:30]
    x2 = np.zeros([M_PN+N_C],dtype=int)
    for i in range(0,31):
        x2[30-i] = x2_init >> (30-i)
        x2_init = x2_init - x2[30-i]*(2**(30-i))
    # initialize x1 and x2 for required length
    for n in range(0,M_PN+N_C-31):
        x1[n+31] = np.mod(x1[n+3]+x1[n],2)
        x2[n+31] = np.mod(x2[n+3]+x2[n+2]+x2[n+1]+x2[n],2)
    # Generate c sequence
    c = np.zeros([M_PN],dtype=int)
    for n in range(0,M_PN):
        c[n] = np.mod(x1[n+N_C]+x2[n+N_C],2)
    return c
# =============================================================================
# Generate CRS 
#   Normal CP : N_CP=1
#   Extended CP : N_CP=0
# =============================================================================
def crs_gen(NID_cell,N_RB_DL_MAX,L,N_S,N_CP,frame_structure):
    if frame_structure == "type3" :
        N_S_prime = 10*np.floor(N_S/10)+np.mod(N_S,2)
    else:
        N_S_prime = N_S
        
    c_init = 1024*(7*(N_S_prime+1)+L+1)*(2*NID_cell+1)+2*NID_cell+N_CP
    c = prs_gen(4*N_RB_DL_MAX,c_init)
    crs = np.zeros([2*N_RB_DL_MAX],dtype=complex)
    for m in range(0,2*N_RB_DL_MAX):
        crs[m] = (1/np.sqrt(2))*(1-2*c[2*m])+1j*(1/np.sqrt(2))*(1-2*c[2*m+1])
    return crs
# =============================================================================
# Generate MBSFN RS
# =============================================================================
def mbsfn_rs_gen(NID_MBSFN,N_RB_DL_MAX,L,N_S):
    c_init = 512*(7*(N_S+1)+L+1)*(2*NID_MBSFN+1)+2*NID_MBSFN
    c = prs_gen(12*N_RB_DL_MAX,c_init)
    mbsfn_rs = np.zeros([6*N_RB_DL_MAX],dtype=complex)
    for m in range(0,6*N_RB_DL_MAX):
        mbsfn_rs[m] = (1/np.sqrt(2))*(1-2*c[2*m])+1j*(1/np.sqrt(2))*(1-2*c[2*m+1])
    return mbsfn_rs
# =============================================================================
# Generate UE-specific RS
# =============================================================================
#def uers_gen()


if __name__ == '__main__' :

#    crs = crs_gen(10,50,0,0,1,"type1")   
    MBSFN_RS = mbsfn_rs_gen(0,100,0,0)
    plt.plot(MBSFN_RS.real,MBSFN_RS.imag,'ro')
