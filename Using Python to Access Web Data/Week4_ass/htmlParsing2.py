import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
urlhop = ""
print "Retrieving: ", url
for hop in range(count):
	urlhop = tags[position - 1].get('href', None)
	if hop == count - 1:
		print "Last URL:", urlhop
	else:
		print "Retrieving:", urlhop
	html = urllib.urlopen(urlhop).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')

