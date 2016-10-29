from flask import Flask, request
from app import app
import twitter
# static url
@app.route('/')
def index():
    return None

# api with endpoint for hashtag
@app.route('/hashtag', methods=['GET'])
def hashtag():
    l=[]
    if 'hash' in request.args:
        return twitter.search(request.args['hash'])
    return "Wrong!"

#api with endpoint for KeyWord
@app.route('/word', methods=['GET'])
def key_word():
    l=[]
    if 'word' in request.args:
        return twitter.search(request.args['word'])
    return "Wrong!"

#api with endpoint for GeoLocation
@app.route('/location', methods=['GET'])
def location():
    l=[]
    if 'location' in request.args:
        return twitter.search_location(request.args['location'])
    return "Wrong"

