import tweepy
import csv

ckey = '07Iv3RJnRPPToDS6a564cQ93h'
csecret = 'J19Zx8NsJo03R5WfiqVTu7lfmPySLrfd2IIGtzPvdXCEAUG9YB'
akey = '748975287019405312-EfE9siMvpp4LS3McSj8EOmMxB3eLBuP'
asecret = 'gzgZfuSNlE5e1F3VFsFyLfdWAVSom7gSuWavX7PnJ4fbU'

def getAllTweets(screen_name):
	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(akey, asecret)
	api = tweepy.API(auth)
	alltweets = []
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	return outtweets
