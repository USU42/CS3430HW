#!/usr/bin/python

#####################################
# module: cs3430_s18_hw07.py
# Kelsye Anderson
# A02093326
#####################################

from __future__ import division
import __future__
import numpy as np
import random
import pickle as cPickle

#from cs3430_s18_hw07_data import *

#10,000 gets it right around 6 out of 7 times and is faster
#50,000 gets it right most of the time, but takes a lot longer
numIters = 50000


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
    binaryNums = np.zeros(shape=(129, 8))
    binaryAns = np.zeros(shape=(129, 2))
    for i in range(129):
        #create the binary number of i
        binNum = '{0:08b}'.format(i)
        for x in range(len(binNum)):
            binaryNums[i][x] = int(binNum[x])

        #put add 10 and 01 to binaryAns depending if i is even or odd
        if(i % 2 is 0):
            binaryAns[i] = [1, 0]
        else:
            binaryAns[i] = [0, 1]

    return (binaryNums, binaryAns)

def train_4_layer_nn(numIters, X, y, build):
    ## your code
    W1, W2, W3 = build()
    for i in range(numIters):
        Z2 = np.dot(X, W1)
        a2 = sigmoid(Z2)

        Z3 = np.dot(a2, W2)
        a3 = sigmoid(Z3)

        Z4 = np.dot(a3, W3)
        yHat = sigmoid(Z4)

        yHat_error = y - yHat
        yHat_delta = yHat_error * sigmoid(yHat, deriv=True)

        a3_error = yHat_delta.dot(W3.T)
        a3_delta = a3_error * sigmoid(a3, deriv=True)

        a2_error = a3_delta.dot(W2.T)
        a2_delta = a2_error * sigmoid(a2, deriv=True)

        W3 += a3.T.dot(yHat_delta)
        W2 += a2.T.dot(a3_delta)
        W1 += X.T.dot(a2_delta)
    return W1, W2, W3

def fit_4_layer_nn(x, wmats, thresh=0.4, thresh_flag=False):
    ## your code
    a2 = sigmoid(np.dot(x, wmats[0]))
    a3 = sigmoid(np.dot(a2, wmats[1]))
    yHat = sigmoid(np.dot(a3, wmats[2]))
    if thresh_flag == True:
        for y in np.nditer(yHat, op_flags=['readwrite']):
            if y > thresh:
                y[...] = 1
            else:
                y[...] = 0
        return yHat.astype(int)
    else:
        return yHat
    pass

def is_even_nn(n, wmats):
    ## your code
    binaryNum = np.zeros(shape=(1, 8))
    binNum = '{0:08b}'.format(n)
    for x in range(len(binNum)):
        binaryNum[0][x] = int(binNum[x])
    fit = fit_4_layer_nn(binaryNum, wmats, thresh_flag=True)
    print(fit)
    print(fit[0])
    print(fit[0][0])
    if (fit[0][0] == 1) and (fit[0][1] == 0):
        return True
    elif (fit[0][0] == 0) and (fit[0][1] == 1):
        return False
    else:
        print("Unable to tell if number is even or odd")


def eval_even_odd_nn(wmats):
    ## your code
    numRight = 0
    for i in range(129):
        # create the binary number of i
        binNum = '{0:08b}'.format(i)
        binaryArray = np.zeros(shape=(1, 8))
        for x in range(len(binNum)):
            binaryArray[0][x] = int(binNum[x])
        fit = fit_4_layer_nn(binaryArray, wmats, thresh_flag=True)

        # checks if i is an even or odd number and if it matches what the ANN said
        if (i % 2 is 0):
            if (fit[0][0] == 1) and (fit[0][1] == 0):
                numRight += 1
        else:
            if (fit[0][0] == 0) and (fit[0][1] == 1):
                numRight += 1
    percentage = numRight/129
    return percentage

def build_even_odd_nn():
    input = (8, 5, 7, 2)
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

even_odd_wmats = train_4_layer_nn(numIters, X, y, build_even_odd_nn)
# print(fit_4_layer_nn(X[3], even_odd_wmats))
# print(fit_4_layer_nn(X[3], even_odd_wmats, thresh_flag=True))
# print(is_even_nn(14, even_odd_wmats))
print(eval_even_odd_nn(even_odd_wmats))

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