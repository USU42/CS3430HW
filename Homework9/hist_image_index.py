#!/usr/bin/python

import argparse
import cv2
import sys
import os
import re
import _pickle as pickle

#####################################################################################
# module: hist_image_index.py
# author:  your name and A-number
# description: persistent image histogram indexer
# to run:
#
# $ python hist_image_index.py -imgdir images/ -clr rgb -hist rgb_hist16.pck -bin 16
# $ python hist_image_index.py -imgdir images/ -clr hsv -hist hsv_hist16.pck -bin 16
#
# the output will look as follows:
# indexing images/16_07_02_14_50_48_orig.png
# images/16_07_02_14_50_48_orig.png indexed
# images/16_07_02_14_37_38_orig.png
# images/16_07_02_14_37_38_orig.png indexed
# images/123473019.JPG
# images/123473019.JPG indexed
# indexing finished
#
# when indexing is finished, the persisted index object is
# saved in rgb_hist16.pck and hst_hist16.pck
######################################################################################

ap = argparse.ArgumentParser()
ap.add_argument('-imgdir', '--imgdir', required = True, help = 'image directory')
ap.add_argument('-hist', '--hist', required = True, help = 'histogram index file')
ap.add_argument('-bin', '--bin', required=True, help='histogram bin size')
ap.add_argument('-clr', '--clr', required=True, help='color space')
args = vars(ap.parse_args())

HIST_INDEX = {}

def generate_file_names(fnpat, rootdir):
  # your code
  for path, subdir, filelist in os.walk(rootdir):
      for name in filelist:
          if not name.startswith('.') and not re.match(fnpat, name) is None:
              yield os.path.join(path, name)
          for dir in subdir:
              generate_file_names(fnpat, dir)


def hist_index_img(imgp, color_space, bin_size=8):
  global HIST_INDEX
  ## your code
  img = cv2.imread(imgp)
  if (color_space is 'rgb'):
    input = cv2.calcHist([img], [0, 1, 2], None, [bin_size, bin_size, bin_size], [0, 256, 0, 256, 0, 256])
    norm_hist = cv2.normalize(input, input).flatten()
    HIST_INDEX[imgp] = norm_hist
  elif (color_space is 'hsv'):
    hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    input = cv2.calcHist([hsvImage], [0, 1, 2], None, [bin_size, bin_size, bin_size], [0, 256, 0, 256, 0, 256])
    norm_hist = cv2.normalize(input, input).flatten()
    HIST_INDEX[imgp] = norm_hist
  pass

def hist_index_img_dir(imgdir, color_space, bin_size):
  # your code
  print(imgdir)
  for imgp in generate_file_names(r'.+\.(jpg|png|JPG)', imgdir):
      print('indexing ' + imgp)
      hist_index_img(imgp, color_space, bin_size)
      print(imgp + ' indexed')
  pass

if __name__ == '__main__':
  hist_index_img_dir(args['imgdir'], args['clr'], int(args['bin']))
  with open(args['hist'], 'wb') as histpick:
    pickle.dump(HIST_INDEX, histpick)
  print('indexing finished')


