#!/usr/bin/python

#######################################################
# module: img_ann_data.py
# Kelsye Anderson
# A02093326
########################################################

'''
websites used
https://stackoverflow.com/questions/7755684/flatten-opencv-numpy-array
https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory
'''


import cv2
import numpy as np
import os

# change these values accordingly.
img_black_dir = '/home/pi/img_black/'
img_white_dir = '/home/pi/img_white/'
img_eval_black_dir = '/home/pi/img_eval_black/'
img_eval_white_dir = '/home/pi/img_eval_white/'

## training and evaluation data
DATA = []
X, y = [], []
EVAL_DATA = []
EX, ey = [], []

def normalize_image(fp):
    ## your code
    img = cv2.imread(fp)
    imgArray = np.array(img)
    imgArray = imgArray.flatten()
    output = []
    for x in range(len(imgArray)):
        temp = imgArray[x] / 255
        output.append(temp)

    return output

def create_data(img_dir, data_label):
    ## your code
    for path, stuff, name in os.walk(os.path.abspath(img_dir)):
        for file in name:
            norm = normalize_image(path + "/" + file)
            DATA.append((os.path.abspath(os.path.join(path, file)), norm, data_label))

def create_eval_data(img_dir, data_label):
    ## your code
    for path, stuff, name in os.walk(os.path.abspath(img_dir)):
        for file in name:
            norm = normalize_image(path + "/" + file)
            EVAL_DATA.append((os.path.abspath(os.path.join(path, file)), norm, data_label))


def create_Xy(DATA):
    global X, y
    for fp, img, yhat in DATA:
        X.append(img)
        y.append(yhat)
    X = np.array(X)
    y = np.array(y)

def create_EXey(EVAL_DATA):
    global EX, ey
    for fp, img, yhat in EVAL_DATA:
        EX.append(img)
        ey.append(yhat)
    EX = np.array(EX)
    ey = np.array(ey)
    
if __name__ == '__main__':
    create_data(img_black_dir, np.array([0, 1]))
    create_data(img_white_dir, np.array([1, 0]))
    np.random.shuffle(DATA)
    create_Xy(DATA)
    create_eval_data(img_eval_black_dir, np.array([0, 1]))
    create_eval_data(img_eval_white_dir, np.array([1, 0]))
    np.random.shuffle(EVAL_DATA)
    create_EXey(EVAL_DATA)


create_data('/Users/kelsyeanderson/Desktop/Github/CS3430HW/Exam2/img_white', np.array([1, 0]))
create_data('/Users/kelsyeanderson/Desktop/Github/CS3430HW/Exam2/img_black', np.array([0, 1]))
np.random.shuffle(DATA)

create_eval_data('/Users/kelsyeanderson/Desktop/Github/CS3430HW/Exam2/img_eval_black', np.array([0, 1]))
create_eval_data('/Users/kelsyeanderson/Desktop/Github/CS3430HW/Exam2/img_eval_white', np.array([1, 0]))
np.random.shuffle(EVAL_DATA)




