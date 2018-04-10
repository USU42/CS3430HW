#!/usr/bin/python

####################################################
## module: leave_one_out_cross_validation.py
## Kelsye Anderson
## A02093326
##
## Bugs to vladimir dot kulyukin at usu dot edu
####################################################

from __future__ import division
import __future__
from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

# let's load the iris dataset
data = load_iris()
flowers = data.data ## 150x4 array flower feature vectors
feature_names = data.feature_names ## names of features 
target = data.target ## target numbers
target_names = data.target_names ## target names
 
## let's get an array of flower names
flower_names = target_names[target]

# let's build three boolean indexes to retrieve
# setosas, virginicas, and versicolors from flowers, e.g.
# flowers[is_setosa] retrieves all setosas.
is_setosa     = (flower_names == 'setosa')
is_virginica  = (flower_names == 'virginica')
is_versicolor = (flower_names == 'versicolor')

def compute_model_accuracy(predictions, ground_truth):
    correct = np.sum(predictions == ground_truth)
    total = len(ground_truth)
    return (correct / total) * 100

def run_model(model, flowers):
    ans = []
    loop = flowers[model]
    for x in loop:
        if model[something] == 'setosa':
            ans.append(compute_model_accuracy(x, is_setosa))
        elif model[something] == 'virginica':
            ans.append(compute_model_accuracy(x, is_virginica))
        elif model[something] == 'versicolor':
            ans.append(compute_model_accuracy(x, is_versicolor))
    return ans
    
def learn_best_th_model_for(flower_name, flowers, bool_index):
    assert len(flowers) == len(bool_index)
    best_fn = 0
    best_th = 0
    best_reverse = False
    best_acc = -1
    if flower_name == 'setosa':
        predictList = flowers[bool_index]
        reverseList = flowers[~bool_index]
        per = compute_model_accuracy(prediction, )
    if flower_name == 'virginica':
        per = compute_model_accuracy(prediction, )
    if flower_name == 'versicolor':
        per = compute_model_accuracy(prediction, )
    for fn in rqange(reverseList.shape[1]):
        possThresholdList = reverseList[:,fn]
        for possThresh in possThresholdList:
            featVal = [:,fn]
            predict = (featVal > pt)
            acc = (predict == is_virginica).mean()
            rv_acc = (predict == ~is_virginica).mean()
            if rev.acc > acc:
                reverse = True
                acc = rev_acc
            else:
                reverse = False

            if acc > best_acc:
                best_acc = acc
                best_fn = fn
                best_th = pt
                best_reverse = reverse
    return (best_fn, best_th, best_reverse, best_acc)
            
def leave_one_out_cross_validation(flower_name, flowers):
    if flower_name == 'setosa':
        bestSet = learn_best_th_model_for(flower_name, flowers, is_setosa)
    elif flower_name == 'virginica':
        bestVir = learn_best_th_model_for(flower_name, flowers, is_virginica)
    elif flower_name == 'versicolor':
        bestVer = learn_best_th_model_for(flower_name, flowers, is_versicolor)
    pass

# ---------------- UNIT TESTS ------------------------

def unit_test_01():
    '''learn single feature classifier for setosa'''
    setosa_model = learn_best_th_model_for('setosa', flowers,
                                           is_setosa)
    print ('setosa model:', setosa_model)

def unit_test_02():
    '''learn single feature classifier for virginica'''
    virginica_model = learn_best_th_model_for('virginica', flowers,
                                              is_virginica)
    print ('virginica model:', virginica_model)

def unit_test_03():
    '''learn single feature classifier for versicolor'''
    versicolor_model = learn_best_th_model_for('versicolor', flowers,
                                               is_versicolor)
    print ('versicolor model:', versicolor_model)

def unit_test_04():
    '''learn and run single feature classifier for setosa'''
    model = learn_best_th_model_for('setosa', flowers, is_setosa)
    predictions = run_model(model, flowers)
    print ('setosa model acc:', compute_model_accuracy(predictions, is_setosa))

def unit_test_05():
    '''learn and run single feature classifier for virginica'''
    model = learn_best_th_model_for('virginica', flowers, is_virginica)
    predictions = run_model(model, flowers)
    print ('virginica model acc:', compute_model_accuracy(predictions, is_virginica))
    
def unit_test_06():
    '''learn and run single feature classifier for versicolor'''
    model = learn_best_th_model_for('versicolor', flowers, is_versicolor)
    predictions = run_model(model, flowers)
    print ('versicolor model acc:', compute_model_accuracy(predictions, is_versicolor))

def unit_test_07():
    '''run leave-one-out cross-validation for setosas'''
    acc = leave_one_out_cross_validation('setosa', flowers)
    print ('leave-1-out cross_valid acc for setosa:', acc)

def unit_test_08():
    '''run leave-one-out cross-validation for virginicas'''
    acc = leave_one_out_cross_validation('virginica', flowers)
    print ('leave-1-out cross_valid acc for virginica:', acc)  

def unit_test_09():
    '''run leave-one-out cross-validation for versicolors'''
    acc = leave_one_out_cross_validation('versicolor', flowers)
    print ('leave-1-out cross_valid acc for versicolor:', acc)
    
## comment out the unit tests to run them
if __name__ == '__main__':
     #unit_test_01()
     #unit_test_02()
     #unit_test_03()
     #unit_test_04()
     #unit_test_05()
     #unit_test_06()
     #unit_test_07()
     #unit_test_08()
     #unit_test_09()
     pass

