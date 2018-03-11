from getAllTweets import *
import re

# Returns the percentage of a user's last 3220 tweets that are just links.
def get_feature(tweets):
    filteredTweets = 0
    for tweet in tweets:
        if re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet.text)=="":
            filteredTweets = filteredTweets + 1
    return (filteredTweets*1.0)/len(tweets)
