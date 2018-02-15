#######################
# dnaf_to_dnas.py
# Kelsye Anderson
# A02093326
#######################

import sys
import re
import decrypt
import encrypt
import half_interval_method

output = ""

for x in sys.stdin.readlines():
    if re.match(r'\S+', x):
        output = output + re.match(r'\S+', x).group(0)
sys.stdout.write(output)
sys.stdout.flush()







