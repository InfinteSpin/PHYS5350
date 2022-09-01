# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:03:52 2022

@author: Hilde

PHYS5350 FALL 2022

Homework 1 Problem 1 
"""
import numpy as np
#we consider a sodium atom at the origin, i = j = k = 0
#spacing on the lattice is a
#distance from origin to any atom is a*sqrt(i**2 + j**2 + k**2)
e = 1.6022*10**-19
a=5.63*10**-10 #NaCl spacing
eps_0 = 8.85*10**-12 #permittivity of free space
L = 12 #number of atoms 
    
def V_ijk(i,j,k,a):
    if abs(i+j+k)%2 == 0:
        V = e/(4*np.pi*eps_0*a*np.sqrt(i**2+j**2+k**2))
    else:
        V = -e/(4*np.pi*eps_0*a*np.sqrt(i**2+j**2+k**2))
    
    return V

def Mandelung(a):
    V_t = 0
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if i==0 and j==0 and k==0:
                    continue
                else:
                    V_t += V_ijk(i,j,k,a)
    #V_t = sum(V_list)                
    M =  V_t*4*np.pi*eps_0*a/e
    return M

print(Mandelung(a))