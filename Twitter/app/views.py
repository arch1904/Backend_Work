from flask import Flask, request
from app import app
import twitter
# static url
@app.route('/')
def index():
    return "Hello, World!\n For Hashtag: /hashtag?=# \n For KeyWord: /word?= \n For GeoLocation: /location?=latitude,longitude,radiuswithunit"

# url parameters
@app.route('/endpoint/<input>')
def endpoint(input):
    return input

# api with endpoint for hashtag
@app.route('/hashtag', methods=['GET'])
def hashtag():
    l=[]
    #if 'name' in request.args:
    l=twitter.search(hashtag)
    return str(l)
    #return "Wrong!"

#api with endpoint for KeyWord
@app.route('/word', methods=['GET'])
def key_word():
    l=[]
    if 'word' in request.args:
        l=twitter.search(word)
    return str(l)

#api with endpoint for GeoLocation
@app.route('/location', methods=['GET'])
def location():
    l=[]
    if 'location' in request.args:
        l=twitter.search(location)
    return str(l)
