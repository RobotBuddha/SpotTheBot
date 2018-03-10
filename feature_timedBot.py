import datetime, time

def timedBot(tweets):
     dates = []
     seconds = []
     sec_list = []

     i=0
     j=0
     for tweet in tweets:
        dates.append(tweet.created_at)
     for sec in range(0, len(dates)):
        seconds.append(dates[sec].second)
     for sec in range(0, len(seconds)):
         for second_1 in range(0, (len(seconds)-1)):
             if seconds[sec] == seconds[second_1]:
                j = j+1
         sec_list.append(j)
         j=0
     return float(max(sec_list))/len(tweets)
