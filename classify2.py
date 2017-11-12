import json
import re
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import operator
import string
import numpy as np
from sklearn.metrics import accuracy_score

FILE_NAME_pos = 'happiness/text_emotion_happiness70'
FILE_NAME_neg = 'sadness/text_emotion_sadness70'
FILE_NAME_pos_test = 'happiness/text_emotion_happiness30'
FILE_NAME_neg_test  = 'sadness/text_emotion_sadness30'

def processTweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    return tweet

def process(FILE_NAME_pos,FILE_NAME_neg):
    with open(FILE_NAME_pos, 'r') as fh, open(FILE_NAME_neg, 'r') as fd:
        train = []

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
            pos = (word_list_pos, 'happy')
            train.append(pos)
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
            train.append(neg)

    fh.close()
    fd.close()
    return train



# print (train)

# with open(FILE_NAME_pos_test, 'r') as fht, open(FILE_NAME_neg_test, 'r') as fdt:
#     test = []
#     for line_pos_test in fht:
#         line_pos_test = fht.readline()
#         processedTweet = processTweet(line_pos_test)
#         word_list_pos_test = processedTweet.replace(',', '') \
#             .replace('@', '') \
#             .replace('#', '') \
#             .replace(';', '') \
#             .replace(':', '') \
#             .replace("\'", '') \
#             .replace('/', '') \
#             .replace('.', '') \
#             .replace('?', '') \
#             .replace('"', '') \
#             .replace('"', '') \
#             .replace('&', '') \
#             .replace(';', '') \
#             .replace('-', '') \
#             .replace('!', '') \
#             .replace('(', '') \
#             .replace(")", '') \
#             .replace('[', '') \
#             .replace(']', '') \
#             .replace('URL', '') \
#             .replace('AT_USER', '')
#         pos_test = (word_list_pos_test,'happy')
#         test.append(pos_test)
#         # print(word_list)
#     for line_neg_test in fdt:
#         line_neg_test = fdt.readline()
#         processedTweet = processTweet(line_neg_test)
#         word_list_neg_test = processedTweet.replace(',', '') \
#             .replace('@', '') \
#             .replace('#', '') \
#             .replace(';', '') \
#             .replace(':', '') \
#             .replace("\'", '') \
#             .replace('/', '') \
#             .replace('.', '') \
#             .replace('?', '') \
#             .replace('"', '') \
#             .replace('"', '') \
#             .replace('&', '') \
#             .replace(';', '') \
#             .replace('-', '') \
#             .replace('!', '') \
#             .replace('(', '') \
#             .replace(")", '') \
#             .replace('[', '') \
#             .replace(']', '') \
#             .replace('URL', '') \
#             .replace('AT_USER', '')
#         neg_test = (word_list_neg_test, 'sad')
#         test.append(neg_test)
#
# fht.close()
# fdt.close()

train = process(FILE_NAME_pos,FILE_NAME_neg)
test = process(FILE_NAME_pos_test,FILE_NAME_neg_test)
cl = NaiveBayesClassifier(train)

# Classify some text
# print(cl.classify("tonight was fun"))  # "happy"
# print(cl.classify("family bbq today &amp; my fave cousin comes too"))   # "happy"
# print(cl.classify("@veropperez great!!  i've gpt tp put the lyrics in, finsih the background, then go over some writing, and then done!!"))   # "happy"
# print(cl.classify("Yesssssssssss! A rocket to the moon is  going on warped!"))   # "happy"
# print(cl.classify("ready for a day full of His presence  i'm expecting the best!"))   # "happy"
# print(cl.classify("I always feel sickly when I wake up.  Well got a busy day ahead of me! Yippeee"))   # "sad"
# print(cl.classify("Now every Saturday till 8/4 for work.  sucks. And no Friday or Monday off for July 4th either."))   # "sad"
# print(cl.classify("Tired. Going to take a nap. My finger hurts.  143"))   # "sad"
# print(cl.classify("just watched BGT on catch up, aw i felt so sorry for holly"))   # "sad"
# print(cl.classify("Is going to sleep now"))   # "sad"

acc = 0
for temp in test:
    a = cl.classify(temp[0])
    # print("acc :" + temp[1] + " result :" + a)
    # print(a==temp[1])
    if temp[1]==a:
        acc = acc+1

print(acc/test.__len__())
#         print (accuracy_score(np.array[temp[1], cl.classify(temp[0])]))



# print("Accuracy: {0}".format(cl.accuracy(test)))
#
#
# cl.show_informative_features(5)
