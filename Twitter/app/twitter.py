import json
import tweepy
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_authenticated_API():
    auth = tweepy.OAuthHandler('SKuaMZ6iWCkHhnQBXvDmim5WF', 'm0TkxhZ6l2UIFk3BpMh8TJgAVw45kpBxF54lnhdAfIQq9xLx7J')
    auth.set_access_token('115824133-zV5X49gQen2nj09ci0EhhuC9HvsMsiAGl0194XUB',
                          'j45YHjZtWPyZrETmH10QJJGfxZhdwpv2adYDJl1I3W6E2')
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

api = get_authenticated_API()

def search(query):
    l=[]   
    for tweet in tweepy.Cursor(api.search, q=query).items(10):
        l.append(tweet.text)
    str1=json.dumps(l)
    return str1

def search_location(query):
    query=query.split(",")
    l=[]
    for tweet in tweepy.Cursor(api.search,geocode=str(query[0])+","+str(query[1])+","+str(query[2])).items(10):
        l.append(tweet.text)
    str1=json.dumps(l)
    return str1