# Extracting Data from Twitter
#                       Pavan Narayanan, 2016

import sys
import jsonpickle
import tweepy

auth = tweepy.AppAuthHandler("GET YOUR OWN AUTHETICATION", "SAME GOES HERE")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

searchQuery = '"verizon"'
maxTweets = 10000000
tweetsPerQry = 200
fName = 'tweets_'+searchQuery+'.txt'
sinceId = None
max_id = -1L
tweetCount = 0

with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if max_id <= 0:
                if not sinceId:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since_id=sinceId)
            else:
                if not sinceId:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))