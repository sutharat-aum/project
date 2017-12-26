import re
from textblob.classifiers import NaiveBayesClassifier
import pickle
import unicodedata as uni

FILE_NAME = ['happiness/text_emotion_happiness70','sadness/text_emotion_sadness70','love/text_emotion_love70','hate/text_emotion_hate70','fun/text_emotion_fun70','worry/text_emotion_worry70']
# FILE_NAME_neg = 'worry/text_emotion_worry70'
emotion = ['happiness','sadness','love','hate','fun','worry']
FILE_NAME_test = ['happiness/text_emotion_happiness30','sadness/text_emotion_sadness30','love/text_emotion_love30','hate/text_emotion_hate30','fun/text_emotion_fun30','worry/text_emotion_worry30']
# FILE_NAME_neg_test  = 'worry/text_emotion_worry30'

def processTweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    return tweet

def process(FILE_NAME,emotion):
    train = []
    for i in range(0,1):
        with open(FILE_NAME[i], 'r') as fh:
            all = fh.readlines()
            for line_pos in all:
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
                sentence = (word_list_pos, emotion[i])
                train.append(sentence)
        fh.close()
    return train

train = process(FILE_NAME,emotion)
test = process(FILE_NAME_test,emotion)
cl = NaiveBayesClassifier(train)

f = open('train.pkl', 'wb')
pickle.dump(cl, f)
f.close()

f = open('train.pkl', 'rb')
cl = pickle.load(f)
f.close()

# numbers_list = cl.train()
# list_pickle_path = 'train.pkl'
#
# # Create an variable to pickle and open it in write mode
# list_pickle = open(list_pickle_path, 'wb')
# pickle.dump(numbers_list, list_pickle)
# list_pickle.close()


# f = open('train.pckl', 'rb')
# cl = pickle.load(f)
# f.close()
#dumfile
# print(len(test))


# acc = 0
# for i in range(0,len(test)):
#     a = cl.classify(test[i][0])
#     if test[i][1] == a:
#         acc = acc+1
#     else:
#         print("line number "+ str(i) +" acc :" + test[i][1] +" sen : "+ test[i][0] +" result :" + a)

# for temp in test:
#     a = cl.classify(temp[0])
#     # print("acc :" + temp[1] + " result :" + a)
#     # print(a==temp[1])
#     if temp[1]==a:
#         acc = acc+1
#     # else:
#     #     print(temp[0])
#     #     print("acc :" + temp[1] +" sen : "+ temp[0] +" result :" + a)

# print(acc/test.__len__())

# print("Accuracy: {0}".format(cl.accuracy(test)))

# cl.show_informative_features(5)