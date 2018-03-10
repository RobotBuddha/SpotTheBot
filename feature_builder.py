import tweepy
from tweepy import OAuthHandler

import getAllTweets
import feature_ends_with_rand_digits
import feature_percent_links
import feature_many_languages
import feature_activity
import feature_timedBot


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
user = api.get_user('@everyword')

tweets = getAllTweets.getAllTweets(user.screen_name)

feature_vector = []

#FEATURE: Checks if a User tweets in a scheduled pattern
feature_vector.append(feature_timedBot.timedBot(tweets))

# FEATURE: Percentage of tweets that are links
feature_vector.append(feature_percent_links.get_feature(tweets))

#FEATURE:  How many tweets is the user posting per day
feature_vector.append(feature_activity.get_feature(tweets))


# Feature extractors take user object as input, output the feature, e.g. a number between 0 and 1
#feature_vector.append(extract_feature1(user))

# FEATURE: Name of bot ends with 8 random digits
#feature_vector.append(feature_ends_with_rand_digits.get_feature(user))


# FEATURE: Is the user posting in more than 3 languages // seems to be garbage
#feature_vector.append(feature_many_languages.get_feature(tweets))


print feature_vector
