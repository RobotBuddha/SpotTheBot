import tweepy
from tweepy import OAuthHandler

import getAllTweets
import feature_timedBot
import feature_percent_links
import feature_solo_links
import feature_activity
import feature_ends_with_rand_digits
import feature_clickbait
import feature_friends_to_followers
import feature_protected
import feature_verified

CONSUMER_KEY = '07Iv3RJnRPPToDS6a564cQ93h'
CONSUMER_SECRET = 'J19Zx8NsJo03R5WfiqVTu7lfmPySLrfd2IIGtzPvdXCEAUG9YB'
ACCESS_KEY = '748975287019405312-EfE9siMvpp4LS3McSj8EOmMxB3eLBuP'
ACCESS_SECRET = 'gzgZfuSNlE5e1F3VFsFyLfdWAVSom7gSuWavX7PnJ4fbU'
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
#user = api.get_user()

def calculateFeatureVector(user):
    # Trump as an example
    user = api.get_user(user)

    tweets = getAllTweets.getAllTweets(user.screen_name)

    # Feature extractors take user object as input, output the feature, e.g. a number between 0 and 1
    #feature_vector.append(extract_feature1(user))

    feature_vector = []

    #FEATURE: Is the user tweeting in a scheduled pattern?
    feature_vector.append(feature_timedBot.timedBot(tweets))

    #FEATURE: How many of the user's tweets contain links?
    feature_vector.append(feature_percent_links.get_feature(tweets))

    #FEATURE: How many of the user's tweets are just solo links?
    feature_vector.append(feature_solo_links.get_feature(tweets))
    
    #FEATURE: How many tweets is the user posting per day?
    feature_vector.append(feature_activity.get_feature(tweets))

    #FEATURE: Does the name of the user end with 8 random digits?
    feature_vector.append(feature_ends_with_rand_digits.get_feature(user))

    #FEATURE: How many of the user's tweets contain common clickbait phrases?
    feature_vector.append(feature_clickbait.clickbait(tweets))

    #FEATURE: Does the user have many more friends than followers?
    feature_vector.append(feature_friends_to_followers.friend_follower_ratio(user))

    #FEATURE: Does the user have an unprotected account?
    feature_vector.append(feature_protected.protected(user))

    #FEATURE: Does the user have an unverified account?
    feature_vector.append(feature_verified.verified(user))

    # FEATURE: Is the user posting in more than 3 languages? (seems to be garbage)
    #feature_vector.append(feature_many_languages.get_feature(tweets))

    return feature_vector

print calculateFeatureVector("@SandraFair66")
print calculateFeatureVector("@realDonaldTrump")
print calculateFeatureVector("@eduniTHSoc")
