import json
import urllib

url = raw_input('Enter Location: ')
data = urllib.urlopen(url).read()
print 'Retrieving', url
print 'Retrieved', len(data), 'characters'

js = json.loads(str(data))
count = 0
sum = 0
for u in js['comments']:
	count = count + 1
	sum = sum + u['count']
	
print 'Count:', count
print 'Sum:', sum