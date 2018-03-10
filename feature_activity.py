import datetime, time

def get_feature(tweets):
    dates = []
    ages = []
    tweet_1  = tweets[len(tweets)-1]
    tweet_2  = tweets[0]
    dates.append(tweet_2.created_at)
    dates.append(tweet_1.created_at)
    age_1 = time.time() - (dates[0] - datetime.datetime(1970,1,1)).total_seconds()
    ages.append(age_1)
    age_2 = time.time() - (dates[1] - datetime.datetime(1970,1,1)).total_seconds()
    ages.append(age_2)
    diff = (ages[1]-ages[0])/3600
    avg_tweet = len(tweets)/diff
    avg_tweet = avg_tweet*24
    if avg_tweet == 20:
     return 0
    if avg_tweet >= 40:
     return 1
    else:
     return (float(avg_tweet)-0)/40
