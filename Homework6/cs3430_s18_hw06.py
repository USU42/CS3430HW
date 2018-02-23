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
    temp = np.delete(temp, np.s_[i], 0)#row
    temp = np.delete(temp, np.s_[j], 1) #column
    return temp

def det(mat):
    ## your code
    if (len(mat) > 2):
        det(minorMat(mat, , ))
    return (mat[0][0] * mat[1][1]) - (mat[0][1] - mat[1][0])


def cofactor(mat, i, j):
    ## your code
    pass

def expandByRowMinors(mat, r):
    ## your code
    pass

def expandByColMinors(mat, c):
    ## your code
    pass

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
    
    
