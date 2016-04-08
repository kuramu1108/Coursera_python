import xml.etree.ElementTree as ET
import urllib
url = raw_input('Enter location: ')
print 'Retrieving', url
data = urllib.urlopen(url).read()

print 'Retrieved', len(data), 'characters'

xt = ET.fromstring(data)
counts = xt.findall('comments/comment')
sum = 0
for count in counts:
	sum = sum + int(count.find('count').text)

print 'Count:', len(counts)
print 'Sum:', sum