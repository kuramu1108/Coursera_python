import random
import math

#for i in range(10):
#    print random.random()

#print random.randint(5,10)

#t = [1,2,3]
#print random.choice(t)

#print math.pi

def roll(times):
    print "rolling a dice " + str(times)
    for i in range(times):
        print random.randint(1,6)

inp = raw_input("Enter times to roll the dice: ")
inp = int(inp)
roll(inp)
