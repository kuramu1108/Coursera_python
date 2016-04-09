import re

fh = open("regex_sum_205591.txt")
nums = list()
for line in fh:
	line = line.rstrip()
	data = re.findall("[0-9]+", line)
	if len(data) == 0: continue
	for num in data:
		nums.append(int(num))

print sum(nums)

print sum([int(x) for x in re.findall('[0-9]+', open("regex_sum_205591.txt").read())])