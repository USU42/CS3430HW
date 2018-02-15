#######################
# find_pat_mats.py
# Kelsye Anderson
# A02093326
#######################

import re
import sys

r = sys.argv[1]
output = ""

txt = sys.stdin.readline()

match=re.finditer(r,txt)
for x in match:
    sys.stdout.write(x.group()+"\t"+str(x.start())+"\t"+str(x.end())+"\n")
    sys.stdout.flush()








