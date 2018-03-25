#!/usr/bin/python

from __future__ import division
import __future__
import argparse
import cv2
import sys
import os
import re
import numpy as np
import fnmatch
import cPickle as pickle

########################
# module: image_index.py
# Kelsye Anderson
# A02093326
########################

ap = argparse.ArgumentParser()
ap.add_argument('-imgdir', '--imgdir', required = True, help = 'image directory')
ap.add_argument('-bgr', '--bgr', required = True, help = 'bgr index file to pickle')
ap.add_argument('-hsv', '--hsv', required = True, help = 'hsv index file to pickle')
ap.add_argument('-gsl', '--gsl', required = True, help = 'gsl index file to pickle')
args = vars(ap.parse_args())

def generate_file_names(fnpat, rootdir):
  # your code
  for path, subdir, filelist in os.walk(rootdir):
      for name in filelist:
          if not name.startswith('.') and not re.match(fnpat, name) is None:
              yield os.path.join(path, name)
          for dir in subdir:
              generate_file_names(fnpat, dir)


## three index dictionaries
HSV_INDEX = {}
BGR_INDEX = {}
GSL_INDEX = {}

def index_img(imgp):
    try:
        img = cv2.imread(imgp)
        index_bgr(imgp, img)
        index_hsv(imgp, img)
        index_gsl(imgp, img)
        del img
    except Exception as e:
        print(str(e))

# compute the bgr vector for img saved in path imgp and
# index it in BGR_INDEX under imgp.
def index_bgr(imgp, img):
    # your code
    blue = 0
    green = 0
    red = 0
    bgri = []
    rows = img.shape[0]
    cols = img.shape[1]
    for x in range(rows):
        for y in range(cols):
            blue += img[x, y, 0]
            green += img[x, y, 1]
            red += img[x, y, 2]
        bgri.append((blue/cols, green/cols, red/cols))
    BGR_INDEX[imgp] = bgri


# compute the hsv vector for img saved in path imgp and
# index it in HSV_INDEX under imgp.
def index_hsv(imgp, img):
    # your code
    hue = 0
    saturation = 0
    value = 0
    hsvi = []
    rows = img.shape[0]
    cols = img.shape[1]
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for x in range(rows):
        for y in range(cols):
            hue += hsvImage[x, y, 0]
            saturation += hsvImage[x, y, 1]
            value += hsvImage[x, y, 2]
        hsvi.append((hue / cols, saturation / cols, value / cols))
    HSV_INDEX[imgp] = hsvi


# compute the gsl vector for img saved in path imgp and
# index it in GSL_INDEX under imgp.
def index_gsl(imgp, img):
  # your code
  gray = 0
  gsli = []
  rows = img.shape[0]
  cols = img.shape[1]
  gImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  for x in range(rows):
      for y in range(cols):
          gray += gImage[x, y]
      gsli.append((gray / cols))
  GSL_INDEX[imgp] = gsli

# index image directory imgdir
def index_img_dir(imgdir):
  print(imgdir)
  for imgp in generate_file_names(r'.+\.(jpg|png|JPG)', imgdir):
    print('indexing ' + imgp)
    index_img(imgp)
    print(imgp + ' indexed')

# index and pickle
if __name__ == '__main__':
  index_img_dir(args['imgdir'])
  with open(args['bgr'], 'wb') as bgrfile:
    pickle.dump(BGR_INDEX, bgrfile)
  with open(args['hsv'], 'wb') as hsvfile:
    pickle.dump(HSV_INDEX, hsvfile)
  with open(args['gsl'], 'wb') as gslfile:
    pickle.dump(GSL_INDEX, gslfile)
  print('indexing finished')
    

