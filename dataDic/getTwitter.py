import re
import tweepy
import configparser
from tweepy import OAuthHandler
from textblob import TextBlob


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

        try:
            if type =='search':
                fetchedTweets = self.api.search(q=query, count=count)

            elif type == 'user':
                fetchedTweets = self.api.user_timeline(screen_name = query,count=200)

            for tweet in fetchedTweets:
                tweets.append(tweet.text)


            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def main():

    api = twitterClient()
    tweets = api.getSearchTweets(query='@Got', count=250)

    print("\n\n 5 top tweets:\n\n")
    for tweet in tweets[:5]:
        print(tweet+"\n")


if __name__ == "__main__":
    # calling main function
    main()