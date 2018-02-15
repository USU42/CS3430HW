#!/usr/bin/python3

###########################################
# module: decrypt.py
# Kelsye Anderson
# A02093326
###########################################
#websites used
##https://docs.python.org/3/library/re.html
##https://www.tutorialspoint.com/python3/string_split.htm
##https://docs.python.org/3/library/functions.html

from pascal import *
from half_interval_method import half_interval_method
from encrypt import *
import math
import sys
import re

    
def decrypt_text(txt):
    ## your code
    s = pascal_square_row_sum(30, 29)
    z = half_interval_method(lambda x: 100 * x ** 10 + 200 * x ** 5 + 4 * x ** 2 + x - s, 0, 1000)
    out = ''
    match = txt.split(str(code_separator))
    match[:] = [item for item in match if item]
    for x in match:
        temp = int(x) - int(math.floor(z))
        out += chr(temp)
    return out





print(decrypt_text(encrypt_text('Raise your words, not voice.\n It is rain that grows flowers, not thunder.\n Rumi')))

