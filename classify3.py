import re
from textblob.classifiers import NaiveBayesClassifier
import itertools

# FILE_NAME = ['happiness/text_emotion_happiness70','sadness/text_emotion_sadness70','love/text_emotion_love70','hate/text_emotion_hate70','fun/text_emotion_fun70','worry/text_emotion_worry70']
FILE_NAME = ['happiness/text_emotion_happiness70','sadness/text_emotion_sadness70']
emotion = ['happiness','sadness','love','hate','fun','worry']
# FILE_NAME_test = ['happiness/text_emotion_happiness30','sadness/text_emotion_sadness30','love/text_emotion_love30','hate/text_emotion_hate30','fun/text_emotion_fun30','worry/text_emotion_worry30']
FILE_NAME_test = ['happiness/text_emotion_happiness30','sadness/text_emotion_sadness30']
def processTweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    return tweet

def process(FILE_NAME,emotion):
    train = []
    train2 = []
    for i in range(0,len(FILE_NAME)):
        with open(FILE_NAME[i], 'r') as fh:
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
                sentence = (word_list_pos, emotion[i])
                train.append(sentence)

        fh.close()
    return train

train = process(FILE_NAME,emotion)
test = process(FILE_NAME_test,emotion)
cl = NaiveBayesClassifier(train)


# for i,j in enumerate(test):
#     print(i)
#     print(j)
#
# for i in range(len(test)):
#     num = test.index(test[i])
#     print(len(test))

acc = 0

for i,temp in range(len(test)):
    a = cl.classify(temp[0])
        # print("acc :" + temp[1] + " result :" + a)
        # print(a==temp[1])
    if temp[1]==a:
        acc = acc+1
    else:
            # print(str(tt)+str(i))
            #print(str(i)+temp[0])
        print(len(test)+" ------- "+"acc :" + temp[1] +" sen : "+ temp[0] +" result :" + a)


# print(acc/test.__len__())
#
# print("Accuracy: {0}".format(cl.accuracy(test)))

# cl.show_informative_features(5)