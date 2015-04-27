import urllib
import json

def getRandom():
	random = urllib.urlopen('http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json')
	json_obj = json.load(random)
	titles = []
	for dict in json_obj['query']['random']:
		titles.append(dict['title'])
	return titles