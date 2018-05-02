#!/usr/bin/python
from __future__ import division
import __future__
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import os
import argparse
import cv2
import sys
import re
import random
import numpy as np
from sklearn import tree, metrics
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_predict
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier

#################################################
# module: dtr_rf.py
# Kelsye Anderson
# A02093326
##################################################

## ================== LOADING DATA =======================

## Change the value of BEE_DIR accordingly
BEE = []
BEE_DIR = '/Desktop/Homework/CS3430HW/Exam3'
TARGET = []
DATA = []

def generate_file_names(fnpat, rootdir):
  # your code
  for path, subdir, filelist in os.walk('.'):
    for name in filelist:
        if not name.startswith('.') and not re.match(fnpat, name) is None:
            yield os.path.join(path, name)
        for dir in subdir:
            generate_file_names(fnpat, dir)

def load_data(imgdir):
  ## your code
  for imgp in generate_file_names(r'.+\.(jpg|png|JPG)', imgdir):
    oldImg = cv2.imread(imgp)
    img = cv2.cvtColor(oldImg, cv2.COLOR_BGR2GRAY)
    input = cv2.calcHist([img], [0], None, [8], [0, 256])
    norm_hist = cv2.normalize(input, input).flatten()
    DATA.append(norm_hist)
    if(imgp[:9] == './yes_bee'):
      TARGET.append(1)
    else:
      TARGET.append(0)

  random.shuffle(TARGET)
  random.shuffle(DATA)
  # print('Target size:', len(TARGET))
  # print('Data size:', len(DATA))
  # print('data at 999', DATA[999])
  # print('target at 999', TARGET[999])
  pass

## ===================== DECISION TREES ==============================

def run_dtr_train_test_split(data, target, n, test_size):
  ## your code
  output = {}
  for i in range(n):
    dtr = tree.DecisionTreeClassifier(random_state = random.randint(0, 100))
    train_data, test_data, train_target, test_target = \
                train_test_split(data, target,
                                 test_size = test_size,
                                 random_state = random.randint(0, 1000))
    dtr = dtr.fit(train_data, train_target)
    clf_expected = test_target
    clf_predicted = dtr.predict(test_data)
    correct = 0
    for x in range(len(clf_expected)):
        if clf_expected[x] == clf_predicted[x]:
            correct += 1
    acc = correct / len(clf_expected)
    print('---------------------------------------')
    print('Train/Test run %i: accuracy= %f' %(i, acc))
    
    output[i] = acc
  print('---------------------------------------')
  return output
  pass

def plot_dtr_train_test_split(output, n, test_size):
  ## your code
  graph = plt.figure(1)
  graph.suptitle('DTR Train/Test split; Test size = %f' % test_size)

  probs = []
  for x in output.keys():
    probs.append(output[x])

  num_nodes_start = 0
  num_nodes_end = n
  plt.plot(output.keys(), probs, 'go')
  plt.xticks(np.arange(num_nodes_start, num_nodes_end - 1, 1.0))
  plt.yticks(np.arange(-0.1, 1.1, .1))
  plt.xlabel('Expiriment label')
  plt.ylabel('Accuracy')
  plt.grid(True)

  plt.show()
  pass

def run_dtr_cross_validation(data, target, test_size):
  ## your code
  output = {}

  dtr = tree.DecisionTreeClassifier(random_state = random.randint(0, 100))
  train_data, test_data, train_target, test_target = \
              train_test_split(data, target,
                                test_size = test_size,
                                random_state = random.randint(0, 1000))
  dtr = dtr.fit(train_data, train_target)
  clf_expected = test_target
  clf_predicted = dtr.predict(test_data)
  
  for cv in xrange(5, 21):
    cross_val = cross_val_predict(dtr, DATA,
                                  TARGET, cv=cv)
    acc = sum(cross_val==target)/float(len(target))
    output[cv] = acc
    print('Num folders %i: accuracy= %f' %(cv, acc))
    print('---------------------------------------')
  return output

def plot_dtr_cross_validation(output, nf_lower, nf_upper, test_size):
  ## your code
  graph = plt.figure(2)
  graph.suptitle('DTR Cross Validation: Test size = %f' % test_size)

  probs = []
  for x in output.keys():
    probs.append(output[x])

  num_nodes_start = nf_lower
  num_nodes_end = nf_upper
  plt.plot(output.keys(), probs, 'go')
  plt.xticks(np.arange(num_nodes_start, num_nodes_end, 1.0))
  plt.yticks(np.arange(-0.1, 1.1, .1))
  plt.xlabel('Expiriment label')
  plt.ylabel('Accuracy')
  plt.grid(True)

  plt.show()
  
  pass

def compute_cr_cm(data, target, test_size):
  ## your code
  dtr = tree.DecisionTreeClassifier(random_state = random.randint(0, 100))
  train_data, test_data, train_target, test_target = \
                train_test_split(data, target,
                                 test_size = test_size,
                                 random_state = random.randint(0, 1000))
  dtr = dtr.fit(train_data, train_target)
  clf_expected = test_target
  clf_predicted = dtr.predict(test_data)
  print('Classification report for decision tree %s:\n%s\n'
        %(dtr, classification_report(clf_expected, clf_predicted)))
  print('Confusion matrix: \n%s' % confusion_matrix(clf_expected,
                                                    clf_predicted))
  pass

## ================= RANDOM FORESTS ==============================
    
def create_rfs(n, num_trees, data, target):
  ## your code
  output = []
  possibleTS = [0.2, 0.25, 0.3, 0.35, 0.4]
  for x in range(n):
    rf = RandomForestClassifier(n_estimators = num_trees, random_state = random.randint(0, 1000))
    test_size = random.choice(possibleTS)
    train_data, test_data, train_target, test_target = \
                train_test_split(data, target,
                                 test_size = test_size,
                                 random_state = random.randint(0, 1000))
    rf = rf.fit(train_data, train_target)
    clf_expected = test_target
    clf_predicted = rf.predict(test_data)
    correct = 0
    for x in range(len(clf_expected)):
        if clf_expected[x] == clf_predicted[x]:
            correct += 1
    acc = correct / len(clf_expected)
    output.append(rf)
  return output

def classify_with_rfs_aux(rand_forests, data_item):
  ## your code
  pass

def classify_with_rfs(rfs, data, target):
  ## your code
  pass

def run_rf_mv_experiments(rfs, data, target, n):
  ## your code
  pass

def collect_rf_mv_stats(rfs_list, data, target, n):
  num_trees_acc_list = []
  for num_trees, rfs in rfs_list:
    num_trees_acc_list.append((num_trees,
                               run_rf_mv_experiments(rfs,
                                                     data,
                                                     target,
                                                     n)))
  return num_trees_acc_list

def create_rf_list(ntrees_in_rf, data, target):
  ## your code
  pass

def plot_rf_mv_stats(rf_mv_stats, num_trees_lower, num_trees_upper):
  ## your code
  pass
  

load_data(BEE_DIR)
#output = run_dtr_train_test_split(DATA, TARGET, 10, .3)

