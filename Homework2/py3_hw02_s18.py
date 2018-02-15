#/usr/bin/python3

#########################################
## CS 3430: S2018: HW02: DNA String Analysis
## Kelsye Anderson
## A02093326
#########################################

from dna_data import *

import re

pat00 = r'CC' 
pat01 = r'T{3,5}'
pat02 = r'T{3,5}(A|G)'
pat03 = r'(A|G)(T{3,10}|C{2,5})G?'
pat04 = r'(A|T)(G{5,15}|C{2,11})T*(AA|GGG)'

pat05 = r'A{4,}'
pat06 = r'G{4,}'
pat07 = r'C{4,}'
pat08 = r'T{4,}'

pat09 = r'G{2,5}(A+)(C)G{2,5}'
pat10 = r'C{2,5}(A+)(T)C{2,5}'
pat11 = r'T{2,5}(A+)(G)T{2,5}'

def find_pat_matches(pat, txt):
    match=re.finditer(pat,txt)
    out = []
    for x in match:
        out.append((x.group(),[x.start(), x.end()]))
    return out

def sort_pat_matches_by_span(pat, txt, reverse):
    match = find_pat_matches(pat,txt)
    if reverse == False:
        match.sort(key=lambda x: x[1][1]-x[1][0], reverse = False)
    else:
        match.sort(key=lambda x: x[1][1]-x[1][0], reverse = True)

    return match

def top_n_pat_matches_by_span(pat, txt, n):
    match=sort_pat_matches_by_span(pat,txt,reverse=True)
    topNum = []
    if len(match)>0:
     for x in range(n):
          topNum.append((match[x]))
    return topNum

def find_dnas_with_longest_span_match_for_pattern(pat, dna_list):
    match = []
    for x in dna_list:
        temp = top_n_pat_matches_by_span(pat,x[1],1)
        if len(temp)>0:
            match.append((x[0],temp[0][0], temp[0][1]))
    match.sort(key=lambda x: x[2][1]-x[2][0], reverse = True)
    return match[0]

def count_pattern_matches(pat, dna_list):
    count = 0
    for x in dna_list:
        count = count + len(find_pat_matches(pat,x[1]))
    return count













