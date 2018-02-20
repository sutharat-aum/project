import tweepy
import datetime
import xlsxwriter
import sys

# credentials from https://apps.twitter.com/
consumerKey = 'H0zsL9t0o7ebSv5oEaYnLS8kd'
consumerSecret = 'zY3HcbCO6vJFWBeeKIZowQJsyQxhIjJuGRjBS0ukhWiEteihTn'
accessToken = '816223789604212736-RcGR6pgdOOu4TFzEYuLyfMsQd8YebBi'
accessTokenSecret = 'k2GcZGhpeacZWQCnlUKFoLRJBmm2M0bysRMDoQOnWNjYX'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

username = sys.argv[1]
startDate = datetime.datetime(2014, 6, 1, 0, 0, 0)
endDate =   datetime.datetime(2015, 1, 1, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

for tweet in tweets:
    print(tweet)

# workbook = xlsxwriter.Workbook(username + ".xlsx")
# worksheet = workbook.add_worksheet()
# row = 0
# for tweet in tweets:
#     worksheet.write_string(row, 0, str(tweet.id))
#     worksheet.write_string(row, 1, str(tweet.created_at))
#     worksheet.write(row, 2, tweet.text)
#     worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
#     row += 1
#
# workbook.close()
# print("Excel file ready")