import json
import tweepy

def get_authenticated_API():
    auth = tweepy.OAuthHandler('SKuaMZ6iWCkHhnQBXvDmim5WF', 'm0TkxhZ6l2UIFk3BpMh8TJgAVw45kpBxF54lnhdAfIQq9xLx7J')
    auth.set_access_token('115824133-zV5X49gQen2nj09ci0EhhuC9HvsMsiAGl0194XUB',
                          'j45YHjZtWPyZrETmH10QJJGfxZhdwpv2adYDJl1I3W6E2')
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

api = get_authenticated_API()
def search_hashtag(query):
    l=[]
    for tweet in tweepy.Cursor(api.search, q='#'+query).items(10):
        l.append(str(tweet))

    with open ('tweets.json','w') as f:
        json.dump(l,f)

def search_keyword(query):
    l=[]
    for tweet in tweepy.Cursor(api.search, q=query).items(10):
        l.append(str(tweet))
    with open ('tweets.json','w') as f:
        json.dump(l,f)

def search_location(lat,long,radius):
    l=[]
    for tweet in tweepy.Cursor(api.search,geocode=str(lat)+","+str(long)+","+str(radius)).items(10):
        l.append(str(tweet))
    with open ('tweets.json','w') as f:
        json.dump(l,f)
