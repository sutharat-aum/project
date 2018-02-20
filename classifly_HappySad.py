import re
from textblob.classifiers import NaiveBayesClassifier


FILE_NAME = ['happiness/text_emotion_happiness70','sadness/text_emotion_sadness70']
emotion = ['happiness','sadness']
FILE_NAME_test = ['dataDic/Output']
def processTweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    return tweet

def process(FILE_NAME,emotion):
    train = []
    for i in range(0,len(FILE_NAME)):
        with open(FILE_NAME[i], 'r') as fh:
            for line in fh:
                line = fh.readline()
                processedTweet = processTweet(line)
                word_list = processedTweet.replace(',', '') \
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
                sentence = (word_list, emotion[i])
                train.append(sentence)
        fh.close()
    return train

train = process(FILE_NAME,emotion)
test = process(FILE_NAME_test,emotion)
cl = NaiveBayesClassifier(train)

acc = 0
for temp in test:
    a = cl.classify(temp[0])
    if temp[1]==a:
        acc = acc+1
        print("acc :" + temp[1] + " sen : " + temp[0] + " >>>True>>> " + " result :" + a)
    else:
        print("acc :" + temp[1] +" sen : "+ temp[0] +" ---False--- "+" result :" + a)

print(acc/test.__len__())














# print("Accuracy: {0}".format(cl.accuracy(test)))
# cl.show_informative_features(5)