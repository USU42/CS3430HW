#!/usr/bin/python

#####################################
# module: cs3430_s18_hw07.py
# Kelsye Anderson
# A02093326
#####################################

import numpy as np
import random
import pickle as cPickle

#from cs3430_s18_hw07_data import *


X_GATE = np.array([[0, 0],
[1, 0],
[0, 1],
[1, 1]])

y_and = np.array([[0],
[0],
[0],
[1]])

y_or = np.array([[0],
[1],
[1],
[1]])

# sigmoid function
def sigmoid(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

def build_nn_wmats(mat_dims):
    ## your code
    ansList = []
    whileList = list(mat_dims)
    for x in range(len(mat_dims) -1):
        ansList.append(np.random.randn(whileList[0], whileList[1]))
        del whileList[0]
    return tuple(ansList)

def build_231_nn():
    return build_nn_wmats((2, 3, 1))

def build_838_nn():
    return build_nn_wmats((8, 3, 8))

def create_nn_data():
    ## your code
    binaryNums = []
    binaryAns = []
    for i in range(129):
        #create the binary number of i
        binNum = '{0:08b}'.format(i)
        tempList = list()
        for x in binNum:
            tempList.append(int(x))
        binaryNums.append(tempList)
        print(tempList)

        #put add 10 and 01 to binaryAns depending if i is even or odd
        if(i % 2 is 0):
            binaryAns.append([1, 0])
        else:
            binaryAns.append([0, 1])

    return (binaryNums, binaryAns)

def train_4_layer_nn(numIters, X, y, build):
    ## your code
    pass

def fit_4_layer_nn(x, wmats, thresh=0.4, thresh_flag=False):
    ## your code
    pass

def is_even_nn(n, wmats):
    ## your code
    pass

def eval_even_odd_nn(wmats):
    ## your code
    pass

def build_even_odd_nn():
    input = (8, 5, 3, 2)
    return build_nn_wmats(input)

def train_3_layer_nn(numIters, X, y, build):
    W1, W2 = build()
    for j in range(numIters):
        Z2 = np.dot(X, W1)
        a2 = sigmoid(Z2)

        Z3 = np.dot(a2, W2)
        yHat = sigmoid(Z3)

        yHat_error = y - yHat
        yHat_delta = yHat_error * sigmoid(yHat, deriv=True)

        a2_error = yHat_delta.dot(W2.T)
        a2_delta = a2_error * sigmoid(a2, deriv=True)

        W2 += a2.T.dot(yHat_delta)
        W1 += X.T.dot(a2_delta)

    return W1, W2

def fit_3_layer_nn(x, W, thresh=0.4, thresh_flag=True):
    a2 = sigmoid(np.dot(x, W[0]))
    yHat = sigmoid(np.dot(a2, W[1]))
    if thresh_flag == True:
        for y in np.nditer(yHat, op_flags=['readwrite']):
            if y > thresh:
                y[...] = 1
            else:
                y[...] = 0
        return yHat.astype(int)
    else:
        return yHat


X, y = create_nn_data()
print(X[:10])
print()
print(y[:10])

# def matrix(row, col):
#     outMat = []
#     for x in range(row):
#         for y in range(col):
#             outMat[x][y] = random.gauss(0, 1)
#     return outMat
#
#
#
# wmats = build_nn_wmats((2, 3, 1))
# print(wmats[0])
# print(wmats[1])
#
# and_wmats = train_3_layer_nn(70000, X_GATE, y_and, build_231_nn)
# or_wmats = train_3_layer_nn(70000, X_GATE, y_or, build_231_nn)
#
# print(len(and_wmats))
# print(len(or_wmats))
#
# for i in range(len(X_GATE)):
#     print(X_GATE[i], fit_3_layer_nn(X_GATE[i], and_wmats), y_and[i])
#
# print()
#
# for i in range(len(X_GATE)):
#     print(X_GATE[i], fit_3_layer_nn(X_GATE[i], or_wmats), y_or[i])
#
# print()
#
# X8_ID = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1]])
#
# y8_id = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1]])
#
# wmats = train_3_layer_nn(700000, X8_ID, y8_id, build_838_nn)
#
# for i in range(len(X8_ID)):
#     print(X8_ID[i], fit_3_layer_nn(X8_ID[i], wmats))