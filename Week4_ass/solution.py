import urllib
from bs4 import BeautifulSoup

count = 0
sum = 0
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
	count = count + 1
	sum = sum + int(tag.contents[0])
print "Count", count
print "Sum", sum