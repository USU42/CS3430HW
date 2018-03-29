#!/usr/bin/python

###################################
# module: satyamitra_numbers.py
# Kelsye Anderson
# A02093326
###################################

'''
websites used
https://docs.python.org/3/tutorial/controlflow.html
https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.empty.html
'''

'''
list from satyamitra_numbers_in_range(1, 20000):
[(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595), (17296, 18416)]
determinate: 4581409242816
'''



import numpy as np
import math

# function that computes the list of proper
# factors of n.
def proper_factors(n):
    ## your code
    output = []
    for x in range(1, int(n/2) + 1):
        if (n/x).is_integer():
            output.append(x)
    return output

# function that computes the determinant of
# 2d numpy array
def det(mat):
    numCol=len(mat)
    if (numCol>2):
        multiplier = 1
        x = 0
        ans = 0
        while x <= (numCol - 1):
            output = {}
            y = 1
            while y <= (numCol - 1):
                z = 0
                output[y] = []
                while z <= (numCol-1):
                    if z == x:
                        num = 0
                    else:
                        output[y].append(mat[y][z])
                    z += 1
                y += 1
            tempList = [output[x] for x in output]
            ans += multiplier * (mat[0][x]) * (det(tempList))
            multiplier *= -1
            x += 1
        return ans
    else:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


# function that computes the list of pairs
# of satyamitra numbers in [lower, upper].
def satyamitra_numbers_in_range(lower, upper):
    ## your code
    output = []
    found = False
    for x in range(lower, upper):
        tempFac = sum(proper_factors(x))
        for y in range(lower,upper):
            if(x != y) and (tempFac == y):
                if(sum(proper_factors(y)) == x):
                    for z in range(len(output)):
                        if(output[z][0] == y) and (output[z][1] == x):
                            found = True
                    if found is not True:
                        output.append((x,y))
                    found = False

    return output

# function that computes creates an n x n
# matrix from the list of satyamitra number
# pairs.
def satyamitra_matrix(sn_list):
    ## your code
    size = (len(sn_list) * 2)**(1/2)
    if not (size.is_integer()):
        return "input list not a perfect square"
    size = int(size)
    mat = np.empty([size, size], dtype=int)
    y = 0
    for x in range(int(size)):
        while y < size:
            mat[x][y] = sn_list[0][0]
            mat[x][y + 1] = sn_list[0][1]
            del sn_list[0]
            y += 2
        y = 0
    return det(mat)


print(satyamitra_matrix(satyamitra_numbers_in_range(1, 20000)))





                



