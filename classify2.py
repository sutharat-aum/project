import json
import re
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import operator
import string


FILE_NAME_pos = 'happiness/text_emotion_happiness70'
FILE_NAME_neg = 'sadness/text_emotion_sadness70'

def processTweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    return tweet

with open(FILE_NAME_pos, 'r') as fh , open(FILE_NAME_neg,'r') as fd:
    train = [[]]

    for line_pos in fh:
        line_pos = fh.readline()
        processedTweet = processTweet(line_pos)
        word_list_pos = processedTweet.replace(',', '') \
            .replace('@', '') \
            .replace('#', '') \
            .replace(';', '') \
            .replace(':', '') \
            .replace("\'", '') \
            .replace('/', '') \
            .replace('.', '') \
            .replace('?', '') \
            .replace('"', '') \
            .replace('"', '') \
            .replace('&', '') \
            .replace(';', '') \
            .replace('-', '') \
            .replace('!', '') \
            .replace('(', '') \
            .replace(")", '') \
            .replace('[', '') \
            .replace(']', '') \
            .replace('URL', '') \
            .replace('AT_USER', '')
        pos = (word_list_pos,'happy')
        train[0].append(pos)
        # print(word_list)
    for line_neg in fd:
        line_neg = fd.readline()
        processedTweet = processTweet(line_neg)
        word_list_neg = processedTweet.replace(',', '') \
            .replace('@', '') \
            .replace('#', '') \
            .replace(';', '') \
            .replace(':', '') \
            .replace("\'", '') \
            .replace('/', '') \
            .replace('.', '') \
            .replace('?', '') \
            .replace('"', '') \
            .replace('"', '') \
            .replace('&', '') \
            .replace(';', '') \
            .replace('-', '') \
            .replace('!', '') \
            .replace('(', '') \
            .replace(")", '') \
            .replace('[', '') \
            .replace(']', '') \
            .replace('URL', '') \
            .replace('AT_USER', '')
        neg = (word_list_neg, 'sad')
        train[0].append(neg)

print(train)

fh.close()
fd.close()
