import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '07Iv3RJnRPPToDS6a564cQ93h'
CONSUMER_SECRET = 'J19Zx8NsJo03R5WfiqVTu7lfmPySLrfd2IIGtzPvdXCEAUG9YB'
ACCESS_KEY = '748975287019405312-EfE9siMvpp4LS3McSj8EOmMxB3eLBuP'
ACCESS_SECRET = 'gzgZfuSNlE5e1F3VFsFyLfdWAVSom7gSuWavX7PnJ4fbU'
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
