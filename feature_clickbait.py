from getAllTweets import *
import re

def removeSingleLinks(tweets):
    newtweets = []
    for tweet in tweets:
        if re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet.text)!="":
            newtweets.append(tweet)
    return newtweets

def clickbait(tweets):
    filteredTweets = removeSingleLinks(tweets)
    score = 0
    for tweet in filteredTweets:
        if "how to" in tweet.text.lower():
            score = score + 1
        if "home remedy" in tweet.text.lower():
            score = score + 1
        if "click here" in tweet.text.lower():
            score = score + 1
        if "download" in tweet.text.lower():
            score = score + 1
        if "you won't believe" in tweet.text.lower():
            score = score + 1
        if "will surprise you" in tweet.text.lower():
            score = score + 1
        if "the end result?" in tweet.text.lower():
            score = score + 1
        if "simple ingredient" in tweet.text.lower():
            score = score + 1
        if "simple trick" in tweet.text.lower():
            score = score + 1
        if "says about your personality" in tweet.text.lower():
            score = score + 1
        if "what happens next" in tweet.text.lower():
            score = score + 1
        if "click to find out" in tweet.text.lower():
            score = score + 1
        if "blew my mind" in tweet.text.lower():
            score = score + 1
        if "blow your mind" in tweet.text.lower():
            score = score + 1
        if "life hack" in tweet.text.lower():
            score = score + 1
    if (2*((score*1.0)/len(filteredTweets)))>1:
        return 1
    else:
        return 2*((score*1.0)/len(filteredTweets))

if __name__ == '__main__':
    bait = clickbait(getAllTweets("@SandraFair66"))
    #bait = clickbait(getAllTweets("@realDonaldTrump"))
    print "Clickbait for '@SandraFair66': " + str(bait)
