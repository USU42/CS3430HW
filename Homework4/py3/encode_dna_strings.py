#!/usr/bin/python3

#################################
# module: encode_dna_strings.py
# Kelsye Anderson
# A02093326
#################################

import re
import sys
import os
import fnmatch

from HuffmanTree import HuffmanTree
from HuffmanTreeNode import HuffmanTreeNode
from BinHuffmanTree import BinHuffmanTree
from CharFreqMap import CharFreqMap

work_dir = '/Users/kelsyeanderson/Desktop/Homework4/dna_data'

def generate_file_names(fnpat, rootdir):
  # your code
  for path, subdir, filelist in os.walk(rootdir):
    for name in fnmatch.filter(filelist, fnpat):
      yield (name)

def encode_dna_strings(fnpat, rootdir, encdir):
  ## your code
  for x in generate_file_names(fnpat, rootdir):
      cfm2 = CharFreqMap.computeCharFreqMap(work_dir + rootdir + x)
      nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm2)
      ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
      bht = BinHuffmanTree(root=ht.getRoot())
      bht.encodeTextFromFileToFile(work_dir + rootdir + x,
                                   work_dir + encdir + x)



  
if __name__ == '__main__':
  encode_dna_strings(sys.argv[1], sys.argv[2], sys.argv[3])














