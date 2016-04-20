total = 0
count = 0
while True:
    inp = raw_input("Enter a value: ")
    if inp == "done":
        break
    if len(inp) < 1:
        break
    else:
        try:
            number = float(inp)
        except:
            print "Bad input"
            continue
    total = total + number
    count = count + 1

print "Done!"
print "average", total/count
