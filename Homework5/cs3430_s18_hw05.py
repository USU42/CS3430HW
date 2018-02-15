#!/usr/bin/python

##########################################
## module: cs3430_s18_hw05.py
## Kelsye
## A02093326
##########################################

import numpy as np

def reduceToREF(m):
    ## your code
    for x in range(len(m)):
        m[0][x] *= (1/2)

    for x in range(len(m)):
        m[1][x] += -2 * m[0][x]
        m[2][x] += -4 * m[0][x]

    for x in range(len(m)):
        m[2][x] += m[1][x]
        m[3][x] += m[1][x]

    for x in range(len(m)):
        m[0][x] += -1 * m[1][x]
    pass

def solveLinSys(m):
   ## your code
   if m[1][1]
   pass

def invertMat(m):
    ## your code
    pass


m = np.array([
[2, -4, 2, -2],
[2, -4, 3, -4],
[4, -8, 3, -2],
[0, 0, -1, 2]
],
dtype=float)

print(m)

reduceToREF(m)

print("\n", m, "\n")

m2 = np.array([
[1, 6, 3, 4],
[1, 2, 1, 1],
[-1, 2, 1, 2],
],
dtype=float)

print(m2, "\n")

reduceToREF(m2)

print(m2, "\n")



            
    


    

