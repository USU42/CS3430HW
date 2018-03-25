#!/usr/bin/python

import argparse
import cv2
import sys
import os
import re
import _pickle as pickle

########################
# module: image_retrieval.py
# Kelsye Anderson
# A02093326
########################

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--imgpath', required = True, help = '/Users/kelsyeanderson/Desktop/Github/CS3430HW/Homework8/images/car_test/img01.png')
ap.add_argument('-bgr', '--bgr', required = True, help = 'bgr index file to unpickle')
ap.add_argument('-hsv', '--hsv', required = True, help = 'hsv index file to unpickle')
ap.add_argument('-gsl', '--gsl', required = True, help = 'gsl index file to unpickle')
args = vars(ap.parse_args())

def mean(v):
  return sum(v)/(len(v)*1.0)

# compute the bgr similarity between
# two bgr index vectors
def bgr_img_sim(img_index_vec1, img_index_vec2):
    #your code
    blueTop = 0
    greenTop = 0
    redTop = 0
    blueBot = 0
    greenBot = 0
    redBot = 0
    secondBbot = 0
    secondRbot = 0
    secondGbot = 0
    for x in range (len(img_index_vec1)):
        blueTop += img_index_vec1[x][0] * img_index_vec2[x][0]
        greenTop += img_index_vec1[x][1] * img_index_vec2[x][1]
        redTop += img_index_vec1[x][2] * img_index_vec2[x][2]
        blueBot += img_index_vec1[x][0]**2
        greenBot += img_index_vec1[x][1]**2
        redBot += img_index_vec1[x][2]**2
        secondBbot += img_index_vec2[x][0]**2
        secondGbot += img_index_vec2[x][1]**2
        secondRbot += img_index_vec2[x][2]**2
    blueSim = blueTop /( ((blueBot)**(1/2)) * ((secondBbot)**(1/2)) )
    greenSim = greenTop /( ((greenBot)**(1/2)) * ((secondGbot)**(1/2)) )
    redSim = redTop /( ((redBot)**(1/2)) * ((secondRbot)**(1/2)) )
    avgSim = (blueSim + greenSim + redSim)/3
    return avgSim
  
# compute the hsv similarity between
# two hsv index vectors
def hsv_img_sim(img_index_vec1, img_index_vec2):
  # your code
  hueTop = 0
  saturationTop = 0
  valueTop = 0
  hueBot = 0
  saturationBot = 0
  valueBot = 0
  secondHbot = 0
  secondSbot = 0
  secondVbot = 0
  for x in range(len(img_index_vec1)):
      hueTop += img_index_vec1[x][0] * img_index_vec2[x][0]
      saturationTop += img_index_vec1[x][1] * img_index_vec2[x][1]
      valueTop += img_index_vec1[x][2] * img_index_vec2[x][2]
      hueBot += img_index_vec1[x][0] ** 2
      saturationBot += img_index_vec1[x][1] ** 2
      valueBot += img_index_vec1[x][2] ** 2
      secondHbot += img_index_vec2[x][0] ** 2
      secondSbot += img_index_vec2[x][1] ** 2
      secondVbot += img_index_vec2[x][2] ** 2
  hueSim = hueTop / (((hueBot) ** (1 / 2)) * ((secondHbot) ** (1 / 2)))
  saturationSim = saturationTop / (((saturationBot) ** (1 / 2)) * ((secondSbot) ** (1 / 2)))
  valueSim = valueTop / (((valueBot) ** (1 / 2)) * ((secondVbot) ** (1 / 2)))
  avgSim = (hueSim + saturationSim + valueSim) / 3
  return avgSim

# compute the hsv similarity between
# two gsl index vectors
def gsl_img_sim(img_index_vec1, img_index_vec2):
  # your code
  grayTop = 0
  grayBot = 0
  secondGbot = 0
  for x in range(len(img_index_vec1)):
      grayTop += img_index_vec1[x] * img_index_vec2[x]
      grayBot += img_index_vec1[x] ** 2
      secondGbot += img_index_vec2[x] ** 2
  graySim = grayTop / (((grayBot) ** (1 / 2)) * ((secondGbot) ** (1 / 2)))
  avgSim = graySim / 3
  return avgSim

# index the input image
def index_img(imgp):
    try:
        img = cv2.imread(imgp)
        if img is None:
          print('cannot read ' + imgp)
          return
        rslt = (index_bgr(img), index_hsv(img), index_gsl(img))
        del img
        return rslt
    except Exception as e:
        print(str(e))

# this is very similar to index_bgr in image_index.py except
# you do not have to save the index in BGR_INDEX. This index
# is used to match the indices in the unpickeld BGR_INDEX.
def index_bgr(img):
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
    return bgri


# this is very similar to index_hsv in image_index.py except
# you do not have to save the index in HSV_INDEX. This index
# is used to match the indices in the unpickeld HSV_INDEX.
def index_hsv(img):
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
        hsvi.append((hue/cols, saturation/cols, value/cols))
    return hsvi


# this is very similar to index_gs. in image_index.py except
# you do not have to save the index in GSL_INDEX. This index
# is used to match the indices in the unpickeld GSL_INDEX.
def index_gsl(img):
    # your code
    gray = 0
    gsli = []
    rows = img.shape[0]
    cols = img.shape[1]
    gImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for x in range(rows):
        for y in range(cols):
            gray += gImage[x, y]
        gsli.append((gray/cols))
    return gsli


# we will unpickle into these global vars below.
BGR_INDEX = None
HSV_INDEX = None
GSL_INDEX = None

# compute the similarities between the bgr
# index vector and all the vectors in the unpickled
# bgr index bgr_index and return the top one.
def compute_bgr_sim(bgr, bgr_index, topn=1):
  # your code
  max = 0
  index = 0
  topList = []
  totalList = []
  for x in bgr_index:
      totalList.append(bgr_img_sim(bgr, bgr_index[x]))
  totalList.sort(key = lambda x : x[0], reverse=True)
  for x in topn:
      topList.append(totalList[x])

# compute the similarities between the hsv
# index vector and all the vectors in the unpickled
# hsv index hsv_index and return the top one.
def compute_hsv_sim(hsv, hsv_index, topn=1):
  # your code
  max = 0
  index = 0
  topList = []
  totalList = []
  for x in hsv_index:
      totalList.append(hsv_img_sim(hsv, hsv_index[x]))
      totalList.sort(key=lambda x: x[0], reverse=True)
  for x in topn:
      topList.append(totalList[x])

# compute the similarities between the gsl
# index vector and all the vectors in the unpickled
# gsl index gls_index and return the top one.
def compute_gsl_sim(gsl, gsl_index, topn=1):
  # your code
  max = 0
  index = 0
  topList = []
  totalList = []
  for x in gsl_index:
      totalList.append(gsl_img_sim(gsl, gsl_index[x]))
  totalList.sort(key=lambda x: x[0], reverse=True)
  for x in topn:
      topList.append(totalList[x])

  return topList

# unpickle, match, and display
if __name__ == '__main__':
  with open(args['bgr'], 'rb') as bgrfile:
    BGR_INDEX = pickle.load(bgrfile)
  with open(args['hsv'], 'rb') as hsvfile:
    HSV_INDEX = pickle.load(hsvfile)
  with open(args['gsl'], 'rb') as gslfile:
    GSL_INDEX = pickle.load(gslfile)


  bgr, hsv, gsl = index_img(args['imgpath'])
  bgr_matches = compute_bgr_sim(bgr, BGR_INDEX)
  hsv_matches = compute_hsv_sim(hsv, HSV_INDEX)
  gsl_matches = compute_gsl_sim(gsl, GSL_INDEX)

  print(bgr_matches)
  print(hsv_matches)
  print(gsl_matches)

  orig = cv2.imread(args['imgpath'])
  bgr = cv2.imread(bgr_matches[0][0])
  hsv = cv2.imread(hsv_matches[0][0])
  gsl = cv2.imread(hsv_matches[0][0])
  cv2.imshow('Input', orig)
  cv2.imshow('BGR', bgr)
  cv2.imshow('HSV', hsv)
  cv2.imshow('GSL', gsl)
  cv2.waitKey()
  del orig
  del bgr
  del hsv
  del gsl
  cv2.destroyAllWindows()
    

