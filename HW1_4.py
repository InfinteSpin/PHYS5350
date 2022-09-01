# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 13:08:06 2022

@author: Hilde
"""
#Catalan Numbers

def catalan_next(n,Cn):
    C_next = ((4*n + 2)/(n+2))*Cn
    return C_next

def first_few(lim):
    C_0 = 1
    C_list = [C_0]
    k = 0
    while C_list[-1] <= lim:
        s = catalan_next(k, C_list[-1])
        if s >= lim:
            break
        else:
            C_list.append(catalan_next(k,C_list[-1]))
            k+=1
    
    return C_list
    
lim = 10**3
print('printing Catalan numbers in increasing order less than one billion')
print(first_few(lim))