#!/usr/bin/python3

#########################################
# module: pascal.py
# Kelsye Anderson
# A02093326
#########################################
#websites used
#https://docs.python.org/3/library/math.html

import numpy as np
import math

def pascal_tri_row(n):
    ## your code
    out = []
    nFac = n
    for k in range(n+1):
        out.append(int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))
    return out

def generate_pascal_tri_rows(num_rows):
    ## your code
    out = []
    for x in range(num_rows+1):
        out.append(pascal_tri_row(x))
    return out

def pascal_square_row(n, r):
    ## your code
    matrix = compute_pascal_square(n)
    row = []
    for x in range(n):
        row.append(matrix[x][r])
    return row

def pascal_tri_row_sum(n):
    ## your code
    row = pascal_tri_row(n)
    sum = 0
    if is_prime(n):
        for x in row:
            if x is not 1:
                sum += int(x / n)
        sum += 2
        return sum
    else:
        return -1

def pascal_square_row_sum(n, r):
    ## your code
    row = pascal_square_row(n, r)
    sum = 0
    for x in row:
        sum += x
    return sum

def compute_pascal_square(num_rows):
    ## your code
    row = generate_pascal_tri_rows(num_rows)
    matrix = [[0 for x in range(num_rows+1)] for y in range(num_rows+1)]
    for x in range(num_rows+1):
        for y in range(num_rows+1):
            if y <= x:
                matrix[x][y] = row[x][y]
            else:
                matrix[x][y] = row[y][x]
    return matrix

#------------ added helpful functions ----------

def is_prime(n):
    # your code here
    ans = True
    for x in range(2,(n-1)):
        if ((n%x) == 0):
            ans = False

    if n == 0 or n == 1:
        ans = False

    return ans


# print(pascal_square_row_sum(5, 2))

