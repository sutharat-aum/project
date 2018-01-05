import re
from textblob.classifiers import NaiveBayesClassifier


FILE_NAME = ['love/text_emotion_love70','hate/text_emotion_hate70']
emotion = ['love','hate']
FILE_NAME_test = ['love/text_emotion_love30','hate/text_emotion_hate30']
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

acc = 0
for temp in test:
    a = cl.classify(temp[0])
    if temp[1]==a:
        acc = acc+1
    else:
        print("acc :" + temp[1] +" sen : "+ temp[0] +" ------- "+" result :" + a)

print(acc/test.__len__())

# print("Accuracy: {0}".format(cl.accuracy(test)))
# cl.show_informative_features(5)