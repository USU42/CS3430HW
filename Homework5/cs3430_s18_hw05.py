#!/usr/bin/python

##########################################
## module: cs3430_s18_hw05.py
## Kelsye Anderson
## A02093326
##########################################


from __future__ import division
import __future__
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


def solveLinSys(m):
   ## your code
   reduceToREF(m)
   numRows = len(m)
   numCol = len(m[0])
   rowAns = 0
   colAns = 0
   for y in range(numRows):
       for x in m[y]:
           if x == 0:
               rowAns += 1
               if rowAns >= numCol:
                   return False
       rowAns = 0

   for y in range(numCol - 1):
       for z in range(numRows):
            if m[z][y] == 0:
                colAns += 1
                if colAns >= numRows:
                    return False
       colAns = 0

   return True


def invertMat(m):
    ## your code
    numRows = len(m)
    numCol = len(m[0])
    invertm = m.copy()
    for x in range(numRows):
        for y in range(numCol):
            if x == y:
                invertm[x][y] = 1
            else:
                invertm[x][y] = 0
    tempm = np.column_stack((m, invertm))
    reduceToREF(tempm)
    return tempm[:,np.s_[2:]]



m = np.array([
[1, 2],
[3, 7],
], dtype=float)

print(m)

m = invertMat(m)

print("\n", m)





#
# m = np.array([
# [2, -1, 3, 4],
# [3, 0, 2, 5],
# [-2, 1, 4, 6]
# ],
# dtype=float)
#
# print(solveLinSys(m))
# print(m)


# print(m)
#
# reduceToREF(m)
#
# print("\n", m, "\n")
#
# m2 = np.array([
# [1, 6, 3, 4],
# [1, 2, 1, 1],
# [-1, 2, 1, 2],
# ],
# dtype=float)
#
# print(m2, "\n")
#
# reduceToREF(m2)
#
# print(m2, "\n")
#







