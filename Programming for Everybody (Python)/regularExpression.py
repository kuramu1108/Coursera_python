import re

fh = open("mbox-short.txt")
"""
for line in fh:
    line = line.rstrip()
    if re.search("^From .*?:", line):
        print re.findall("^From .*:?", line)
"""

numlist = list()
for line in fh:
    line = line.rstrip()
    data = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(data) != 1: continue
    num = float(data[0])
    numlist.append(num)

print "Maxmium:", max(numlist)

### list comprehensive

print "Maxmium:", max([float(x) for x in re.findall("X-DSPAM-Confidence: ([0-9.]+)", open("mbox-short.txt").read())])