#######################
# sort_pat_mats.py
# Kelsye Anderson
# A02093326
#######################

# your code here
import re
import sys

sort = sys.argv[1]

lines = []
for x in sys.stdin.readlines():
    lines.append(x.split())

for x in lines:
    x[1] = int(x[1])
    x[2] = int(x[2])

if sort == "dsc":
        lines.sort(key=lambda x: x[1]-x[2], reverse = False)
elif sort == "asc":
        lines.sort(key=lambda x: x[1]-x[2], reverse = True)

for x in lines:
    sys.stdout.write(str(x[0]) + "\t" + str(x[1]) + "\t" +str(x[2]) + "\n")
    sys.stdout.flush()