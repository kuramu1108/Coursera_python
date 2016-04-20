fname = raw_input("Enter file name: ")
handle = open(fname, "w")

while True:
    line = raw_input("Enter a script:\n")
    if line != "end":
        handle.write(line + "\n")
    else:
        handle.close()
        break

ohandle = open(fname)
for line in ohandle:
    line = line.rstrip()
    print line
