#######################
# dnaf_to_dnas.py
# Kelsye Anderson
# A02093326
#######################

# your code here
import sys
import re

output = ""

for x in sys.stdin.readlines():
    if re.match(r'\S+', x):
        output = output + re.match(r'\S+', x).group(0)
sys.stdout.write(output)
sys.stdout.flush()







