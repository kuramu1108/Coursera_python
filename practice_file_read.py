fname = raw_input("Enter file name: ")
handle = open(fname)
total = 0
count = 0
for line in handle:
    if  not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    line = line[20:]
    confidence = float(line)
    total = total + confidence
    count = count + 1
print "Average spam confidence:", total/count
