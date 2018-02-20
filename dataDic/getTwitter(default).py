import re
import tweepy
import configparser
from tweepy import OAuthHandler
from textblob import TextBlob


class twitterClient(object):

    def __init__(self):

        # set parameter twitterAPI
        config = configparser.ConfigParser()
        config.sections()
        config.read('config.ini')
        CONSUMER_KEY = config['KEY']['consumer_key']
        CONSUMER_SECRET = config['KEY']['consumer_secret']
        ACEESS_TOKEN = config['KEY']['access_token']
        ACCESS_TOKEN_SECRET = config['KEY']['access_token_secret']

        #authentication
        try:
            self.auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            self.auth.set_access_token(ACEESS_TOKEN, ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def cleanTweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w +:\ / \ / \S +)", " ", tweet).split())

    # def get_tweet_sentiment(self, tweet):
    #     analysis = TextBlob(self.cleanTweet(tweet))
    #     # set sentiment
    #     if analysis.sentiment.polarity > 0:
    #         return 'positive'
    #     elif analysis.sentiment.polarity == 0:
    #         return 'neutral'
    #     else:
    #         return 'negative'

    def getSearchTweets(self, query,type='hashtag', count=10):
        tweets = []

        try:
            if type =='hashtag':
                fetchedTweets = self.api.search(q=query, count=count)
            elif type == 'user':
                fetchedTweets = self.api.user_timeline(screen_name = query,count=200)

            for tweet in fetchedTweets:
                tweets.append(tweet.text)
                # parsedTweet = []
                #
                # parsed_tweet = {}
                # parsed_tweet['text'] = tweet.text
                # # parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                # # if tweet has retweets, ensure that it is appended only once
                # if tweet.retweet_count > 0:
                #     if parsed_tweet not in tweets:
                #         tweets.append(parsed_tweet)
                # else:
                #     tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def main():
    # creating object
    api = twitterClient()
    # calling function to get tweets
    tweets = api.getSearchTweets(query='GoodNightAltRight', count=500)


    print("\n\n 20 top tweets:")
    for tweet in tweets[:30]:
        print(">>>"+tweet)

    # # picking positive tweets from tweets
    # ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # # percentage of positive tweets
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets)/len(tweets)))
    # # picking negative tweets from tweets
    # ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # # percentage of negative tweets
    # print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # # percentage of neutral tweets
    # # print("Neutral tweets percentage: {} % ".format(100*len(tweets-ntweets-ptweets)/len(tweets)))
    #
    # # printing first 5 positive tweets
    # print("\n\nPositive tweets:")
    # for tweet in ptweets[:10]:
    #     print(tweet['text'])
    #
    # # printing first 5 negative tweets
    # print("\n\nNegative tweets:")
    # for tweet in ntweets[:10]:
    #     print(tweet['text'])

if __name__ == "__main__":
    # calling main function
    main()