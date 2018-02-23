#/usr/bin/python

##########################################
# module: cs3430_s18_hw06.py
# Kelsye Anderson
# A02093326
##########################################

import numpy as np

def minorMat(mat, i, j):
    ## your code
    temp = mat
    temp = np.delete(temp, np.s_[i], 0) #row
    temp = np.delete(temp, np.s_[j], 1) #column
    return temp

def det(mat):
    ## your code
    return round(np.linalg.det(mat))



def cofactor(mat, i, j):
    ## your code
    ans = det(minorMat(mat, i, j))
    ans *= (-1)**(i+j)
    return ans

def expandByRowMinors(mat, r):
    ## your code
    ans1 = 0
    ans2 = 0
    for x in range(len(mat)):
        ans1 = minorMat(mat, x, r)
        ans2 = cofactor(mat,x,r)
    return (ans1, ans2)

def expandByColMinors(mat, c):
    ## your code
    ans1 = 0
    ans2 = 0
    for x in range(len(mat)):
        ans1 = minorMat(mat, c, x)
        ans2 = cofactor(mat, c, x)
    return (ans1, ans2)

def cofactorMat(mat):
    ## your code
    pass

def adjointMat(mat):
    ## your code
    pass

def inverseMat(mat):
    ## your code
    pass

def cramer(A, b):
    ## your code
    pass
    
    
