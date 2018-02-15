#!/usr/bin/python3

####################################################
# module: CharFreqMap.py
# author: vladimir kulyukin
# creates a dictionary that maps all
# characters in a given file to their frequencies
# in the file.
####################################################

class CharFreqMap(object):
    @staticmethod
    def computeCharFreqMap(fp):
        char_freq_map = {}
        with open(fp) as f:
          while True:
            c = f.read(1)
            if not c:
                break
            if c in char_freq_map:
                char_freq_map[c] += 1
            else:
                char_freq_map[c] = 1
        return char_freq_map
