#!/usr/bin/python

##########################################
## module: cs3430_s18_hw05.py
## Kelsye Anderson
## A02093326
##########################################

import numpy as np

def reduceToREF(m):
    ## your code

    curCol = 0
    numRows = len(m)
    numCol = len(m[0])

    for x in range(numRows):
        if curCol >= numCol:
            return
        curRow = x
        while m[curRow][curCol] == 0:
            curRow += 1
            if curRow == numRows:
                curRow = x
                curCol += 1
                if curCol == numCol:
                    return
        temp = m[curRow]
        m[curRow] = m[x]
        m[x] = temp
        pivot = m[x][curCol]
        m[x] /= float(pivot)
        for num in range(numRows):
            if num != x:
                pivot = m[num][curCol]
                temp = m[x] * pivot
                m[num] = m[num] - temp
        curCol += 1

    pass

def solveLinSys(m):
   ## your code
   reduceToREF(m)
   numRows = len(m)
   for x in range(numRows):
       if m[x] == 0:
           return False

   return True
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










# for x in range(len(m)):
#     m[0][x] *= (1 / 2)
#
# for x in range(len(m)):
#     m[1][x] += -2 * m[0][x]
#     m[2][x] += -4 * m[0][x]
#
# for x in range(len(m)):
#     m[2][x] += m[1][x]
#     m[3][x] += m[1][x]
#
# for x in range(len(m)):
#     m[0][x] += -1 * m[1][x]
#
# for x in m:


# numRows = m
# numCol = m[0]
# for i in range(len(numRows)):
#
#     if m[i][i] is not 0:
#         for x in range(len(numCol)):
#             m[i][x] = m[i][x]/m[i][i]
#     for y in range(i+1, len(numRows)):
#         if m[y][0] is not 0:
#             for z in range(len(numCol)):
#                 m[i+1][z] = (-m[i+1][z] * m[i][z]) + m[i+1][z]
