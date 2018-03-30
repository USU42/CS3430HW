#!/usr/bin/python

import argparse
import cv2
import sys
import os
import _pickle as pickle
import matplotlib.pyplot as plt
from os.path import basename

#######################################################################################################
# module: hist_image_retrieval.py
# author:  your name and A-Number
# description: persistent image retriever
# to run:
# $ python hist_image_retrieval.py -ip horfood_test/img01.JPG -hist hsv_hist16.pck -bin 16 -sim bhatta
#
# the output should print the matches for the top 3 images and display the input image
# and the top 3 matches in 4 matplotlib figures.
# images/123472793.JPG --> 0.914982328755
# images/123465243.JPG --> 0.921478476016
# images/123465992.JPG --> 0.923478808005
########################################################################################################

ap = argparse.ArgumentParser()
ap.add_argument('-ip', '--imgpath', required = True, help = 'image path')
ap.add_argument('-hist', '--hist', required = True, help = 'hist index file')
ap.add_argument('-bin', '--bin', required = True, help = 'hist bin size')
ap.add_argument('-sim', '--sim', required = True, help = 'hist similarity')
ap.add_argument('-clr', '--clr', required = True, help = 'color space')
args = vars(ap.parse_args())

inimg = cv2.imread(args['imgpath'])
bin_size = int(args['bin'])
# compute the histogram of inimg and save it in inhist
inhist = None
# normalize and flatten the inhist into a feature vector
inhist_vec = None

# get the similarity metric string from the command line parameter.
hist_sim = args['sim']

HIST_INDEX = args['hist']

def hist_correl_sim(norm_hist1, norm_hist2):
  # compute correlation similarity b/w normalized and flattened histograms
  correl = cv2.compareHist(norm_hist1, norm_hist2, cv2.HISTCMP_CORREL)
  return correl

def hist_chisqr_sim(norm_hist1, norm_hist2):
  # compute chi square similarity b/w normalized and flattened histograms
  chisqr = cv2.compareHist(norm_hist1, norm_hist2, cv2.HISTCMP_CHISQR)
  return chisqr

def hist_intersect_sim(norm_hist1, norm_hist2):
  # compute intersection similarity b/w normalized and flattened histograms
  intersect = cv2.compareHist(norm_hist1, norm_hist2, cv2.HISTCMP_INTERSECT)
  return intersect

def hist_bhatta_sim(norm_hist1, norm_hist2):
  # compute bhattacharyya similarity b/w normalized and flattened histograms
  bhatta = cv2.compareHist(norm_hist1, norm_hist2, cv2.HISTCMP_BHATTACHARYYA)
  return bhatta

# compute the topn matches using the value saved in hist_sim above.
def compute_hist_sim(inhist_vec, hist_index, topn=3):
  # your code
  topList = []
  totalList = []

  if (args['clr'] == 'rgb'):
    input = cv2.calcHist([inimg], [0, 1, 2], None, [bin_size, bin_size, bin_size], [0, 256, 0, 256, 0, 256])
    inhist_vec = cv2.normalize(input, input).flatten()
  elif (args['clr'] == 'hsv'):
    hsvImage = cv2.cvtColor(inimg, cv2.COLOR_BGR2HSV)
    input = cv2.calcHist([hsvImage], [0, 1, 2], None, [bin_size, bin_size, bin_size], [0, 256, 0, 256, 0, 256])
    inhist_vec= cv2.normalize(input, input).flatten()

  if hist_sim == 'correl':
    for imgp in hist_index:
      totalList.append((imgp, hist_correl_sim(inhist_vec, hist_index[imgp])))
  elif hist_sim == 'chisqr':
    for imgp in hist_index:
      totalList.append((imgp, hist_chisqr_sim(inhist_vec, hist_index[imgp])))
  elif hist_sim == 'inter':
    for imgp in hist_index:
      totalList.append((imgp, hist_intersect_sim(inhist_vec, hist_index[imgp])))
  elif hist_sim == 'bhatta':
    for imgp in hist_index:
      totalList.append((imgp, hist_bhatta_sim(inhist_vec, hist_index[imgp])))

  totalList.sort(reverse=True, key=lambda x: x[1])
  for x in range(topn):
    topList.append(totalList[x])

  return topList

def show_images(input_image, match_list):
  # show 4 images in matplotlib figures

  orig = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
  top1 = cv2.cvtColor(cv2.imread(match_list[0][0]), cv2.COLOR_BGR2RGB)
  top2 = cv2.cvtColor(cv2.imread(match_list[1][0]), cv2.COLOR_BGR2RGB)
  top3 = cv2.cvtColor(cv2.imread(match_list[2][0]), cv2.COLOR_BGR2RGB)

  path1 = os.path.basename(match_list[0][0])
  path2 = os.path.basename(match_list[1][0])
  path3 = os.path.basename(match_list[2][0])

  name1 = 'Matched image 1: ' + str(path1) + 'Sim = ' + str(match_list[0][1])
  name2 = 'Matched image 2: ' + str(path2) + 'Sim = ' + str(match_list[1][1])
  name3 = 'Matched image 3: ' + str(path3) + 'Sim = ' + str(match_list[2][1])

  origPlt = plt.figure(1)
  origPlt.suptitle('Input image')
  plt.imshow(orig)

  fig1 = plt.figure(2)
  fig1.suptitle(name1)
  plt.imshow(top1)


  fig2 = plt.figure(3)
  fig2.suptitle(name2)
  plt.imshow(top2)

  fig3 = plt.figure(4)
  fig3.suptitle(name3)
  plt.imshow(top3)


  plt.show()

 
if __name__ == '__main__':
  with open(args['hist'], 'rb') as histfile:
    HIST_INDEX = pickle.load(histfile)
  sim_list = compute_hist_sim(inhist_vec, HIST_INDEX)
  for imagepath, sim in sim_list:
    print(imagepath + ' --> ' + str(sim))
  show_images(inimg, sim_list)


