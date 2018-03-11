import tweepy
import csv

ckey = ""
csecret = ""
akey = ""
asecret = ""

def getAllTweets(screen_name):
	authorise = tweepy.OAuthHandler(ckey, csecret)
	authorise.set_access_token(akey, asecret)
	api = tweepy.API(authorise)
	alltweets = []
	newTweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(newTweets)
	if(len(alltweets)>0):
		oldest = alltweets[-1].id - 1
	while len(newTweets) > 0:
		newTweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(newTweets)
		oldest = alltweets[-1].id - 1
	return alltweets
