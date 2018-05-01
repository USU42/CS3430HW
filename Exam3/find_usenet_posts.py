#!/usr/bin/python

##############################################################
# module: find_usenet_posts.py
# YOUR NAME
# YOUR A-NUMBER
# bugs to vladimir dot kulyukin at usu dot edu
###############################################################

import os
import sys
import sklearn.datasets
import scipy as sp
from sklearn.cluster import KMeans
import nltk.stem
from sklearn.feature_extraction.text import TfidfVectorizer

## Get the USENET POSTS
usenet_posts = sklearn.datasets.fetch_20newsgroups()

## Sample user posts
user_post1 = \
    """Disk drive problems. Hi, I have a problem with my hard disk.
After 1 year it is working only sporadically now.
I tried to format it, but now it doesn't boot any more.
Any ideas? Thanks.
"""

user_post2 = 'is fuel injector cleaning necessary?'
user_post3 = 'are diesel engines more fuel efficient than gas ones?'
user_post4 = 'how many european players play in the nhl?'

## create objects for the Snowball and Porter stemmers.
snowball_stemmer = None
porter_stemmer = None

class SnowballTfidfVectorizer(TfidfVectorizer):
   ## your code here
   pass

class PorterTfidfVectorizer(TfidfVectorizer):
  ## your code here
  pass
    
## let's create two vectorizer objects.
SnowballVectorizer = SnowballTfidfVectorizer(min_df=10,
                                    stop_words='english',
                                    decode_error='ignore')
PorterVectorizer = PorterTfidfVectorizer(min_df=10,
                                        stop_words='english',
                                        decode_error='ignore')

def compute_feat_mat(data, vectorizer):
    ## your code
    pass

def fit_km(feat_mat, num_clusters):
    ## your code
    pass

def find_posts_similar_to(post, feat_mat, data, vectorizer, km, top_n=10):
    ## your code
    pass





