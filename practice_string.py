text = "X-DSPAM-Confidence:    0.8475"

start = text.find("0")
number = text[start :]
print float(number)
