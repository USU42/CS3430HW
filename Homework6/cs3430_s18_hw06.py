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
    ans = 0
    for x in range(mat.shape[0]): #columns
        ans += cofactor(mat, r, x) * mat[r][x]
    return ans

def expandByColMinors(mat, c):
    ## your code
    ans = 0
    for x in range(len(mat)): #rows
        ans += cofactor(mat, x, c) * mat[x][c]
    return ans

def cofactorMat(mat):
    ## your code
    cofacMat = mat.copy()
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            cofacMat[i][j] = cofactor(mat, i, j)
    return cofacMat

def adjointMat(mat):
    ## your code
    adjoinMat = mat.copy()
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            adjoinMat[i][j] = cofactor(mat, j, i)
    return adjoinMat

def inverseMat(mat):
    ## your code
    invDet = 1/det(mat)
    adjMat = adjointMat(mat)
    invMat = mat.copy()
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            invMat[i][j] = invDet * adjMat[i][j]
    return invMat

def cramer(A, b):
    ## your code
    pass
    
def checkInverse(A):
    D = det(A)
    print(D)
    if D != 0.0:
        print(inverseMat(A))
        print(np.dot(A, inverseMat(A)))
