import spotipy
import json


spotify=spotipy.Spotify()

def search(query):
	results=spotify.search(q=query,type='artist')
	str1=json.dumps(results)
	return str1

print search("Fast Car")