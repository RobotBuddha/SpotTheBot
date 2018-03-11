import tweepy
from tweepy import OAuthHandler

import getAllTweets
import feature_ends_with_rand_digits
import feature_percent_links
import feature_many_languages
import feature_activity
import feature_timedBot
import feature_copy
import feature_noTweet

CONSUMER_KEY = '07Iv3RJnRPPToDS6a564cQ93h'
CONSUMER_SECRET = 'J19Zx8NsJo03R5WfiqVTu7lfmPySLrfd2IIGtzPvdXCEAUG9YB'
ACCESS_KEY = '748975287019405312-EfE9siMvpp4LS3McSj8EOmMxB3eLBuP'
ACCESS_SECRET = 'gzgZfuSNlE5e1F3VFsFyLfdWAVSom7gSuWavX7PnJ4fbU'
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)



api = tweepy.API(auth)
#user = api.get_user()
# Trump as an example
user = api.get_user('@Apple')

tweets = getAllTweets.getAllTweets(user.screen_name)

feature_vector = []
if (len(tweets)==0):
#FEATURE: Identifying bots with no tweets posted using followers_count
    feature_vector.append(feature_noTweet.noTweet(user))
    feature_vector.append(0)
    feature_vector.append(0)
    feature_vector.append(0)
    feature_vector.append(0)

elif(len(tweets) != 0):
    feature_vector.append(0)
#FEATURE: Checking for bot users based on similar tweets
    feature_vector.append(feature_copy.copy(tweets))
#FEATURE: Checks if a User tweets in a scheduled pattern
    feature_vector.append(feature_timedBot.timedBot(tweets))
# FEATURE: Percentage of tweets that are links
    feature_vector.append(feature_percent_links.get_feature(tweets))
#FEATURE:  How many tweets is the user posting per day
    feature_vector.append(feature_activity.get_feature(tweets))

print feature_vector
