#!/usr/bin/python

####################################################
## module: leave_one_out_cross_validation.py
## Your Name
## Your A-Number
##
## Bugs to vladimir dot kulyukin at usu dot edu
####################################################

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
    pass

def run_model(model, flowers):
    pass
    
def learn_best_th_model_for(flower_name, flowers, bool_index):
    assert len(flowers) == len(bool_index)
    pass
            
def leave_one_out_cross_validation(flower_name, flowers):
    pass

# ---------------- UNIT TESTS ------------------------

def unit_test_01():
    '''learn single feature classifier for setosa'''
    setosa_model = learn_best_th_model_for('setosa', flowers,
                                           is_setosa)
    print 'setosa model:', setosa_model

def unit_test_02():
    '''learn single feature classifier for virginica'''
    virginica_model = learn_best_th_model_for('virginica', flowers,
                                              is_virginica)
    print 'virginica model:', virginica_model

def unit_test_03():
    '''learn single feature classifier for versicolor'''
    versicolor_model = learn_best_th_model_for('versicolor', flowers,
                                               is_versicolor)
    print 'versicolor model:', versicolor_model

def unit_test_04():
    '''learn and run single feature classifier for setosa'''
    model = learn_best_th_model_for('setosa', flowers, is_setosa)
    predictions = run_model(model, flowers)
    print 'setosa model acc:', compute_model_accuracy(predictions, is_setosa)

def unit_test_05():
    '''learn and run single feature classifier for virginica'''
    model = learn_best_th_model_for('virginica', flowers, is_virginica)
    predictions = run_model(model, flowers)
    print 'virginica model acc:', compute_model_accuracy(predictions, is_virginica)

def unit_test_06():
    '''learn and run single feature classifier for versicolor'''
    model = learn_best_th_model_for('versicolor', flowers, is_versicolor)
    predictions = run_model(model, flowers)
    print 'versicolor model acc:', compute_model_accuracy(predictions, is_versicolor)

def unit_test_07():
    '''run leave-one-out cross-validation for setosas'''
    acc = leave_one_out_cross_validation('setosa', flowers)
    print 'leave-1-out cross_valid acc for setosa:', acc

def unit_test_08():
    '''run leave-one-out cross-validation for virginicas'''
    acc = leave_one_out_cross_validation('virginica', flowers)
    print 'leave-1-out cross_valid acc for virginica:', acc  

def unit_test_09():
    '''run leave-one-out cross-validation for versicolors'''
    acc = leave_one_out_cross_validation('versicolor', flowers)
    print 'leave-1-out cross_valid acc for versicolor:', acc
    
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
