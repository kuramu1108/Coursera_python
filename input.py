print "Hello World!"
user = raw_input("What's your name? ")
print "Hello", user

try:
    hrs = raw_input("Enter Hours:")
    hrs = float(hrs)
    rate = raw_input("Enter Rate:")
    rate = float(rate)
except:
    print "Error, please enter a number"
    quit()

if hrs > 40:
    pay = 40 * rate + (hrs - 40) * rate * 1.5
else:
    pay = hrs * rate
print pay
