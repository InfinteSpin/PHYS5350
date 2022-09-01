# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:39:39 2022

@author: Hilde

PHYS5350 Fall 2022
Homework 1 problem 2

"""
#Semi-empirical mass formula
a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2


#part a 

def bind(A,Z):
    if A%2 != 0: #conditional for the a5 coefficient
        a5 = 0
    elif A%2 == 0 and Z%2 == 0:
        a5 = 12.0
    elif A%2 == 0 and Z%2 !=0:
        a5 = -12.0
        
    B = a1*A - a2*A**(2/3) - (a3*Z**2)/(A**(1/3)) - a4*((A-2*Z)**2/A) + a5/A**(1/2) #semi-empirical BE formula
    return B

A = 58#values given by the problem
Z = 28
BE = bind(A,Z)
print(BE)

#part b
def be_per_nucleon(A,Z): #quick function that does division
    BE = bind(A,Z)
    BperA = BE/A
    return BperA

BperA = be_per_nucleon(A, Z)
print(BperA)

#part c
def stable(Z):
    a_list = [] #list for A values
    be_list = [] #list for binding energies
    for A in range(Z,3*Z+1): #looping through Z to 3Z as a value for A
        a_list.append(A) #we add the current A to a list
        be_list.append(be_per_nucleon(A, Z)) #That A's minding energy per nucleon is added at the same index on a different list
    
    stable_be = max(be_list) 
    sbe_index = be_list.index(stable_be)
    stable_a = a_list[sbe_index]
    return [stable_a, stable_be]

sa = stable(Z)
print('Most stable A value:',sa[0],'The most stable Binding energy: ',sa[1])
    
    
#part d
def most_stable():
    Z_list = []#lists to hold things of interest
    A_list = []
    BE_list = []
    for Z in range(1,101):#looping Z from 1 to 100
        Z_list.append(Z)#current z value gets put into list of Z's
        a_be = stable(Z) #this is a tuple returned by the function in part c to determine the max be/n and corresponding A value for a certain Z
        A_list.append(a_be[0]) #A values from the tuple go into the A list
        BE_list.append(a_be[1])
        print('Most stable A value for Z=',Z,': A=',a_be[0],' BE/N:',a_be[1]) #this line prints every value we find
    max_ben = max(BE_list) #finds the max binding energy
    max_ben_index = BE_list.index(max_ben) #grabs the index of the max binding energy
    z_max_ben = Z_list[max_ben_index]#grabs the z corresponding to the index of the max binding energy.
    A_max_ben = A_list[max_ben_index]#grabs the a corresponding to the index of max binding energy
    return[z_max_ben,A_max_ben,max_ben] #gives us a three value array of the values at max binding energy per nucleon
    
max_vals = most_stable()#function call
print('\nMaximum binding energy per nucleon of nuclei from Z=1 to Z=100: Z =',max_vals[0],' A =',max_vals[1],' BE =',max_vals[2],'.')
