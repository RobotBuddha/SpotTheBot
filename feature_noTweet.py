import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)



api = tweepy.API(auth)
def noTweet(user):
    if(user.followers_count==0):
        return 1
    if(user.followers_count >=100000):
        return 0
    else:
        return (float(user.followers_count)-0)/100000
