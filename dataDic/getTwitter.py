import re
import tweepy
import configparser
import datetime
import io

from nltk import pr
from tweepy import OAuthHandler
from textblob import TextBlob
from tweepy.streaming import json


class twitterClient(object):

    def __init__(self):

        config = configparser.ConfigParser()
        config.sections()
        config.read('config.ini')
        CONSUMER_KEY = config['KEY']['consumer_key']
        CONSUMER_SECRET = config['KEY']['consumer_secret']
        ACEESS_TOKEN = config['KEY']['access_token']
        ACCESS_TOKEN_SECRET = config['KEY']['access_token_secret']

        try:
            self.auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            self.auth.set_access_token(ACEESS_TOKEN, ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(self.auth)

        except:
            print("Error: Authentication Failed")

    # def cleanTweet(self, tweet):
    #     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w +:\ / \ / \S +)", " ", tweet).split())


    def getSearchTweets(self, query,type='search', count=200):
        tweets = []

        # startDate = datetime.datetime(2018, 2, 10, 0, 0, 0)g
        # endDate = datetime.datetime(2018, 2, 14, 0, 0, 0)

        try:
            if type =='search':
                fetchedTweets = self.api.search(q=query, count=count)

            elif type == 'user':
                fetchedTweets = self.api.user_timeline(screen_name = query,count=200)

            # for tweet in fetchedTweets:
            #     tweets.append(tweet.text)
            for tweet in fetchedTweets:
                # if tweet.created_at < endDate and tweet.created_at > startDate:
                    tweets.append(tweet.text)

            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    twwrite = []


    api = twitterClient()
    tweets = api.getSearchTweets(query='SuperBowl', count=500)
    # print("\n\n 10 top tweets:\n\n")
    for tweet in tweets:
        # print(">>>>>>   "+tweet+"\n")
        twwrite.append(tweet)
        # twwrite = tweet
        with io.open("Output", "w", encoding="utf-8") as f:
            for i in range(0, len(twwrite)):
                # print(str(i)+">>>"+twwrite[i])
                f.write(str(i) + ">>>" + twwrite[i]+"\n")
                #f.write('"'+(twwrite[i])+'"' + "\n")
                data = (list(twwrite))

            # f.write('\n'.join(str(line) for line in data))
            # f.write(str(data))
        f.close()

 # for i in range(0,len(test)):
#     a = cl.classify(test[i][0])
#     if test[i][1] == a:
#         acc = acc+1
#     else:
#         print("line number "+ str(i) +" acc :" + test[i][1] +" sen : "+ test[i][0] +" result :" + a)


if __name__ == "__main__":
    # calling main function
    main()