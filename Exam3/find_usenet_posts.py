#!/usr/bin/python

##############################################################
# module: find_usenet_posts.py
# Kelsye Anderson
# A02093326
# bugs to vladimir dot kulyukin at usu dot edu
###############################################################

from __future__ import division
import __future__
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

import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')
class SnowballTfidfVectorizer(TfidfVectorizer):
   ## your code here
   def build_analyzer(self):
      analyzer = super(TfidfVectorizer, self).build_analyzer()
      return lambda doc: english_stemmer.stemWords(analyzer(doc))d

english_stemmer = nltk.stem.porter('english')
class PorterTfidfVectorizer(TfidfVectorizer):
  ## your code here
   def build_analyzer(self):
      analyzer = super(TfidfVectorizer, self).build_analyzer()
      return lambda doc: english_stemmer.stemWords(analyzer(doc))
    
## let's create two vectorizer objects.
SnowballVectorizer = SnowballTfidfVectorizer(min_df=10,
                                    stop_words='english',
                                    decode_error='ignore')
PorterVectorizer = PorterTfidfVectorizer(min_df=10,
                                        stop_words='english',
                                        decode_error='ignore')

def compute_feat_mat(data, vectorizer):
   ## your code
   return vectorizer.fit_transform(data)

def fit_km(feat_mat, num_clusters):
   ## your code
   km = KMeans(n_clusters=num_clusters, n_init=1, verbose=1, random_state=3)
   return km.fit(feat_mat)

def find_posts_similar_to(post, feat_mat, data, vectorizer, km, top_n=10):
   ## your code
   new_post_vec = vectorizer.transform([post]).getrow(0).toarray()
   km_predicted_labels = km.predict(new_post_vec)
   top_new_post_label = km.predict(new_post_vec)[0]
   posts_in_same_cluster = (km.labels_ == top_new_post_label).nonzero()[0]
   similar_posts = []
   for i in posts_in_same_cluster:
      dist = sp.linalg.norm(new_post_vec - feat_mat[i])
      similar_posts.append((dist, data.data[i]))
   similar_posts.sort(key=lambda post: post[0])
   output = []
   for num in range(top_n):
      output.append(similar_posts[num])
   return output

