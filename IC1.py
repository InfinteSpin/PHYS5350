# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:25:32 2022

Comp physics day 1 | August 31 2022

@author: Hilde
"""
#IC problem 2
def prime_factors(n):
    l1 = []
    i = 2
    while i<=n:
        while n % i ==0:
            l1.append(i)
            n//=i
        i+=1
    return l1

def primes():
    n = 10000 #limit
    pr = [] #list to hold the prime nubers we find
    for i in range(2,n): #loops from 2 to the limit
        l1 = prime_factors(i) #checks the prime factors of the current index
        if len(l1) == 1: #if the length of the prime factor list is 1, we know it is a prime number
            pr.append(i)
            
    return prime

print(primes())

