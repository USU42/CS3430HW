#!/usr/bin/python

'''
========================================
module: random_audio_forests.py
Kelsye Anderson
A02093326
========================================
'''

from __future__ import division
import __future__
import numpy as np
import scipy
import random
import os
import glob
import argparse

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import KFold
import matplotlib.colors
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report


## change the base_dir as needed
base_dir = '/home/Desktop/Homework/CS3430HW/Homework12/audio_data/'
sub_dir = ['beefv','cricketfv','noisefv']

## Reading the files and creating feature and response object
def read_audio_data(base_dir):
    global sub_dir
    data, target = [], []
    for label,class_names in enumerate(sub_dir, start = 0):
        vector_dir = os.path.join(base_dir, class_names, '*.mvector.npy')
        all_files = glob.glob(vector_dir)
        for f in all_files :
            value = np.load(f)
            data.append(value[:])
            target.append(label)

    return np.array(data), np.array(target)

def train_test_split_eval_dtr(dtr, data, target, test_size=0.4):
    ## your code
    pass

def train_test_split_eval_rf(rf, data, target, test_size=0.4):
    ## your code
    pass

def train_test_split_dtr_range_eval(n, data, target):
    ## your code
    pass

def train_test_split_rf_range_eval(lower_tree_bound, upper_tree_bound, data, target):
    ## your code
    pass

   

