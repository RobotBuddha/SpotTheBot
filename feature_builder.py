import tweepy
from tweepy import OAuthHandler

import getAllTweets
import feature_ends_with_rand_digits
import feature_percent_of_tweets_that_are_links


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
user = api.get_user('@realDonaldTrump')

tweets = getAllTweets.getAllTweets(user.screen_name)

feature_vector = []

# Feature extractors take user object as input, output the feature, e.g. a number between 0 and 1
#feature_vector.append(extract_feature1(user))

feature_vector.append(feature_ends_with_rand_digits.get_feature(user))
feature_vector.append(feature_percent_of_tweets_that_are_links.linkRatio(tweets))

print feature_vector