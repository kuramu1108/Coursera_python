name = raw_input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] == "From":
        count[words[1]] = count.get(words[1], 0) + 1
most = None
mostCount = 0
for sender, times in count.items():
    if most is None or times > mostCount:
        most = sender
        mostCount = times

print most, mostCount
