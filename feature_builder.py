import tweepy
import time
from tweepy import OAuthHandler

import getAllTweets
import feature_timedBot
import feature_percent_links
import feature_solo_links
import feature_activity

import feature_timedBot
import feature_copy
import feature_noTweet

import feature_ends_with_rand_digits
import feature_clickbait
import feature_friends_to_followers
import feature_protected
import feature_verified


CONSUMER_KEY = undefined
CONSUMER_SECRET = undefined
ACCESS_KEY = undefined
ACCESS_SECRET = undefined
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)
#user = api.get_user()

def calculateFeatureVector(user):
    # Trump as an example
    try:
        if user[0] != '@':
            user = api.get_user('@' + user)
        else:
            user = api.get_user(user)
    except tweepy.TweepError:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if user.protected:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0]
    try:
        tweets = getAllTweets.getAllTweets(user.screen_name)
    except tweepy.TweepError:
        time.sleep(15 * 60)
        tweets = getAllTweets.getAllTweets(user.screen_name)

    # Feature extractors take user object as input, output the feature, e.g. a number between 0 and 1
    #feature_vector.append(extract_feature1(user))

    feature_vector = []


    if (len(tweets)==0):
        #FEATURE: Identifying bots with no tweets posted using followers_count
        feature_vector.append(feature_noTweet.noTweet(user))
        feature_vector.append(0)
        feature_vector.append(0)
        feature_vector.append(0)
        feature_vector.append(0)
        feature_vector.append(0)
        feature_vector.append(0)

    elif(len(tweets) > 0):
        feature_vector.append(0)

        #FEATURE: Checking for bot users based on similar tweets
        feature_vector.append(feature_copy.copy(tweets))

        #FEATURE: Checks if a User tweets in a scheduled pattern
        feature_vector.append(feature_timedBot.timedBot(tweets))

        #FEATURE: Percentage of tweets that are links
        feature_vector.append(feature_percent_links.get_feature(tweets))

        #FEATURE:  How many tweets is the user posting per day
        feature_vector.append(feature_activity.get_feature(tweets))

        #FEATURE: How many of the user's tweets are just solo links?
        feature_vector.append(feature_solo_links.get_feature(tweets))

        #FEATURE: How many of the user's tweets contain common clickbait phrases?
        feature_vector.append(feature_clickbait.clickbait(tweets))




    #FEATURE: Does the user have many more friends than followers?
    feature_vector.append(feature_friends_to_followers.friend_follower_ratio(user))

    #FEATURE: Does the user have an unprotected account?


    #FEATURE: Does the user have an unverified account?
    feature_vector.append(feature_verified.verified(user))

    return feature_vector
