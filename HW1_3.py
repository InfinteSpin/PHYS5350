# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:28:55 2022

@author: Hilde
"""
import numpy as np

def factorial(n):
    s = 1
    for i in range(1,n+1):
        s*=i
    return s

def binomial(n,k):
    n_k = factorial(n)//(factorial(k)*factorial(n-k))
    return n_k

print(binomial(4,1))
print(binomial(2,0))

#part b: PAscal's triangle
def pascal(l): #l is how many lines of the triangle you want
    for n in range(1,l+1): #n ranges from 1 to as many lines of the triangle we want
        line_n = [] #This will store the current line in an array so printing is nicer
        for k in range(n+1): #k ranges from 0 to the current n
            line_n.append(binomial(n,k))
        print(line_n) #print the line

pascal(5)

#part c: coin toss
#probablility that a coin tossed n times will come up heads k times is (n k)/2**n
def prob(n,k):
    P = binomial(n,k)/(2**n)
    return P

print('Probability of the coin landing on heads exactly 60 times:',prob(100,60))

P_total = 0
n = 100 #total number of tosses
m = 60 #starting value for how mnay times we want heads to land, i.e. if we want the probability for it to land on heads 60 or more times this should be 60
for k in range(m,n+1):#loops through what we are given for options of how many times heads is landed on
    P_total+=prob(n, k)
    
print('Probability of the coin landing on heads 60 or more times:',P_total)