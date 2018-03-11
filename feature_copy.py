
import time
import json
import re
import sys
import os.path
def copy(tweets):
    similar = []
    i = 0
    j = 0

    for tweet in range(0, len(tweets)):
        for tweet_1 in range(1, len(tweets)-1):
            if(tweets[tweet]==tweets[tweet_1]):
                j = j+1
        similar.append(j)
        j = 0
    return  float(max(similar))/len(tweets)
