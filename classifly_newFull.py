import re
from textblob.classifiers import NaiveBayesClassifier



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
        with open(FILE_NAME[i], 'r', encoding="utf-8") as fh:
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
                    .replace('AT_USER', '') \
                    .replace(' i ', ' ') \
                    .replace(' you ', ' ') \
                    .replace(' we ', ' ') \
                    .replace(' they ', ' ') \
                    .replace(' he ', ' ') \
                    .replace(' she ', ' ') \
                    .replace(' it ', ' ') \
                    .replace(' me ', ' ') \
                    .replace(' you ', ' ') \
                    .replace(' us ', ' ') \
                    .replace(' them ', ' ') \
                    .replace(' him ', ' ') \
                    .replace(' her ', ' ') \
                    .replace(' my ', ' ') \
                    .replace(' your ', ' ') \
                    .replace(' our ', ' ') \
                    .replace(' their ', ' ') \
                    .replace(' his ', ' ') \
                    .replace(' hes ', ' ') \
                    .replace(' its ', ' ') \
                    .replace(' and ', ' ') \
                    .replace(' but ', ' ') \
                    .replace(' nor ', ' ') \
                    .replace(' so ', ' ') \
                    .replace(' for ', ' ') \
                    .replace(' yet ', ' ') \
                    .replace(' or ', ' ') \
                    .replace(' is ', ' ') \
                    .replace(' am ', ' ') \
                    .replace(' are ', ' ') \
                    .replace(' was ', ' ') \
                    .replace(' were ', ' ') \
                    .replace(' have ', ' ') \
                    .replace(' has ', ' ') \
                    .replace(' had ', ' ') \
                    .replace(' do ', ' ') \
                    .replace(' does ', ' ') \
                    .replace(' did ', ' ') \
                    .replace(' will ', ' ') \
                    .replace(' would ', ' ') \
                    .replace(' shall ', ' ') \
                    .replace(' should ', ' ') \
                    .replace(' can ', ' ') \
                    .replace(' could ', ' ') \
                    .replace(' may ', ' ') \
                    .replace(' might ', ' ') \
                    .replace(' must ', ' ') \
                    .replace(' need ', ' ') \
                    .replace(' dare ', ' ') \
                    .replace(' ought to ', ' ') \
                    .replace(' used to ', ' ') \
                    .replace(' what ', ' ') \
                    .replace(' where', ' ') \
                    .replace(' when ', ' ') \
                    .replace(' whenever ', ' ') \
                    .replace(' whether ', ' ') \
                    .replace(' while ', ' ') \
                    .replace(' how ', ' ') \
                    .replace(' why ', ' ')
                sentence = (word_list, emotion[i])
                train.append(sentence)
        fh.close()
    return train

def process_test(FILE_NAME_test):
    test = []
    for i in range(0,len(FILE_NAME_test)):
        with open(FILE_NAME_test[i], 'r') as fh:
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
                    .replace('AT_USER', '') \
                    .replace(' i ', ' ') \
                    .replace(' you ', ' ') \
                    .replace(' we ', ' ') \
                    .replace(' they ', ' ') \
                    .replace(' he ', ' ') \
                    .replace(' she ', ' ') \
                    .replace(' it ', ' ') \
                    .replace(' me ', ' ') \
                    .replace(' you ', ' ') \
                    .replace(' us ', ' ') \
                    .replace(' them ', ' ') \
                    .replace(' him ', ' ') \
                    .replace(' her ', ' ') \
                    .replace(' my ', ' ') \
                    .replace(' your ', ' ') \
                    .replace(' our ', ' ') \
                    .replace(' their ', ' ') \
                    .replace(' his ', ' ') \
                    .replace(' hes ', ' ') \
                    .replace(' its ', ' ') \
                    .replace(' and ', ' ') \
                    .replace(' but ', ' ') \
                    .replace(' nor ', ' ') \
                    .replace(' so ', ' ') \
                    .replace(' for ', ' ') \
                    .replace(' yet ', ' ') \
                    .replace(' or ', ' ') \
                    .replace(' is ', ' ') \
                    .replace(' am ', ' ') \
                    .replace(' are ', ' ') \
                    .replace(' was ', ' ') \
                    .replace(' were ', ' ') \
                    .replace(' have ', ' ') \
                    .replace(' has ', ' ') \
                    .replace(' had ', ' ') \
                    .replace(' do ', ' ') \
                    .replace(' does ', ' ') \
                    .replace(' did ', ' ') \
                    .replace(' will ', ' ') \
                    .replace(' would ', ' ') \
                    .replace(' shall ', ' ') \
                    .replace(' should ', ' ') \
                    .replace(' can ', ' ') \
                    .replace(' could ', ' ') \
                    .replace(' may ', ' ') \
                    .replace(' might ', ' ') \
                    .replace(' must ', ' ') \
                    .replace(' need ', ' ') \
                    .replace(' dare ', ' ') \
                    .replace(' ought to ', ' ') \
                    .replace(' used to ', ' ') \
                    .replace(' what ', ' ') \
                    .replace(' where', ' ') \
                    .replace(' when ', ' ') \
                    .replace(' whenever ', ' ') \
                    .replace(' whether ', ' ') \
                    .replace(' while ', ' ') \
                    .replace(' how ', ' ') \
                    .replace(' why ', ' ')
                sentence = (word_list)
                test.append(sentence)
        fh.close()
    return test

def start_train():
    FILE_NAME = ['happiness/text_emotion_happiness70', 'sadness/text_emotion_sadness70','fun/text_emotion_fun70','worry/text_emotion_worry70','love/text_emotion_love70','hate/text_emotion_hate70']
    emotion = ['happiness', 'sadness','fun','worry','love','hate']
    train = process(FILE_NAME, emotion)
    cl = NaiveBayesClassifier(train)
    return cl

def classify_String(inputString):
    input = process_test(inputString)
    train.classify(input)
    return input

def classify_list(inputList):
    list = []
    test = process_test(inputList)
    for temp in test:
        a = train.classify(test)
        list.append(a)
        print(" sen : " + temp + " result :" + a)
    return list

train = start_train()
# classify_Str = classify_String("Reading my book in the sunshine, goona be a good day")
list = classify_list(FILE_NAME_test)
print (list)





# print("Accuracy: {0}".format(cl.accuracy(test)))
# cl.show_informative_features(5)