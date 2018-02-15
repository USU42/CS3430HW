#!/usr/bin/python3

#################################
# module: py3_dnas_analysis.py
# Kelsye Anderson
# A02093326
#################################

import re
import sys
import os
import fnmatch
import math

## --------- GENERATE_FILE_NAMES

def generate_file_names(fnpat, rootdir):
  # your code
  for path, subdir, filelist in os.walk(rootdir):
    for name in fnmatch.filter(filelist, fnpat):
      yield os.path.join(path,name)

def unit_test_01(fnpat, rootdir):
  for fn in generate_file_names(fnpat, rootdir):
    sys.stdout.write(fn + '\n')
  sys.stdout.flush()
        
## ----------- GENERATE_INPUT_STREAMS & GENERATE_LINES
      
def generate_input_streams(gen_filenames):
  # your code
  for x in gen_filenames:
    yield (x,open(x,'r'))

def generate_dna_strings(gen_instreams):
  # your code
  for x,y in gen_instreams:
    for z in y.readlines():
      output = ""
      if re.match(r'\S+', z):
        output = output + re.match(r'\S+', z).group(0)
      yield (x, output)

def unit_test_02(fnpat, rootdir):
  dna_fns  = generate_file_names(fnpat, rootdir)
  dna_ins  = generate_input_streams(dna_fns)
  dna_strs = generate_dna_strings(dna_ins)
  for fn, ds in dna_strs:
    sys.stdout.write(fn + '\t' + ds + '\t' + '\n')
  sys.stdout.flush()

def generate_pat_matches(pat, gen_dna_strings):
  # your code
  for path,txt in gen_dna_strings:
    match = re.finditer(pat, txt)
    for x in match:
      yield (path,(x.group(),x.start(),x.end()))


def unit_test_03(fnpat, repat, rootdir):
  dna_fns  = generate_file_names(fnpat, rootdir)
  dna_ins  = generate_input_streams(dna_fns)
  dna_strs = generate_dna_strings(dna_ins)
  pat_mats = generate_pat_matches(repat, dna_strs)
  for fn, pm in pat_mats:
    sys.stdout.write(fn + '\t' + str(pm) + '\n')
  sys.stdout.flush()

def find_max_pat_match(fnpat, repat, rootdir):
  max = []
  for x in generate_pat_matches(repat,
                                generate_dna_strings(generate_input_streams(generate_file_names(fnpat, rootdir)))):
    max.append(x)
  max.sort(key=lambda x: x[1][1] - x[1][2], reverse=False)
  return max[0]


def find_min_pat_match(fnpat, repat, rootdir):
  min = []
  for x in generate_pat_matches(repat,
                                generate_dna_strings(generate_input_streams(generate_file_names(fnpat, rootdir)))):
    min.append(x)
  min.sort(key=lambda x: x[1][1] - x[1][2], reverse=True)
  return min[0]

def unit_test_04(fnpat, repat, rootdir):
  max_match = find_max_pat_match(fnpat, repat, rootdir)
  min_match = find_min_pat_match(fnpat, repat, rootdir)
  sys.stdout.write(repr(max_match)+'\n')
  sys.stdout.write(repr(min_match)+'\n')
  
if __name__ == '__main__':
  #unit_test_01(sys.argv[1], sys.argv[2])
  #unit_test_02(sys.argv[1], sys.argv[2])
  #unit_test_03(sys.argv[1], sys.argv[2], sys.argv[3])
  unit_test_04(sys.argv[1], sys.argv[2], sys.argv[3])
  pass














