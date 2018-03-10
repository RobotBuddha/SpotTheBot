from getAllTweets import *
import re

# Returns the percentage of a user's last 3220 tweets that contain a link.
def linkRatio(tweets):
    filteredTweets = 0
    for tweet in tweets:
        if (re.search('((www\.[^\s]+)|(https?://[^\s]+))', tweet.text) is not None):
            filteredTweets = filteredTweets + 1
    return (filteredTweets*1.0)/len(tweets)

# Main runs the method on Donald Trump's Twitter
if __name__ == '__main__':
    #ratio = linkRatio(getAllTweets("J_tsar"))
    ratio = linkRatio(getAllTweets("@realDonaldTrump"))
    print "ratio for '@realDonaldTrump': " + str(ratio)
