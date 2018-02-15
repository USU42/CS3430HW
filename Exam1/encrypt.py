#!/usr/bin/python3

###########################################
# module: encrypt.py
# Kelsye Anderson
# A02093326
###########################################

from pascal import *
from half_interval_method import half_interval_method
import sys
import math

#code_separator = 2311 # euclid_number(4)
code_separator = 29819592777931214269172453467810429868925511217482600306406141434158091 # euclid_number(40)

def encrypt_char(c):
    ## your code
    s = pascal_square_row_sum(30, 29)
    z = half_interval_method(lambda x: 100*x**10 + 200*x**5 + 4*x**2 + x - s, 0, 1000)
    encrypted = str(code_separator) + str(int(math.floor(z)) + ord(c)) + str(code_separator)
    return encrypted

def encrypt_text(txt):
    enc = ''
    for c in txt: enc += encrypt_char(c)
    return enc

print(encrypt_text('efg, !@'))

