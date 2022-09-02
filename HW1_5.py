# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:42:19 2022

@author: Hilde
"""
#Catalan numbers recursion function
def catalan_r(n):
    if n == 0:
        return 1
    else:
        p = (4*n-2)/(n+1) #placeholder for the coeffcient 
        return p*catalan_r(n-1) #recursive call with n being replaced with n-1

print('C_100 = ',catalan_r(100))

def gcd(m,n):
    if n == 0: #base case
        return m 
    else:
        return gcd(n,m%n) #recursive call with the modulo of m and n replacing n and n replacing m
    
print('Greatest common divisor of 108 and 192:',gcd(108,192)) 