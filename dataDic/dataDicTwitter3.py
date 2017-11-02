import json
import re
import operator
import string


FILE_NAME = 'happiness/text_emotion_happiness70'
wordCounter = {}

def processTweet(tweet):
    # process the tweets
    # Convert to lower case
    tweet = tweet.lower()
    # Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    # Convert @username to AT_USER
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    # Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    # trim
    # tweet = tweet.strip('\'"')
    return tweet


with open(FILE_NAME, 'r') as fh:

    for line in fh:

        line = fh.readline()
        processedTweet = processTweet(line)
        word_list = processedTweet.replace(',', '') \
            .replace(':', '') \
            .replace('\'', '') \
            .replace('/', '') \
            .replace('.', '') \
            .replace('?', '') \
            .replace('"', '') \
            .replace('"', '') \
            .replace('&', '') \
            .replace(';', '') \
            .replace('-', '') \
            .replace('!', '').lower().split()


        for word in word_list:
            if word not in wordCounter:
                wordCounter[word] = 1
            else:
                wordCounter[word] = wordCounter[word] + 1
                # print('{:50}{:10}'.format('Word','Count'))
                # print('----------------------------------'

    data = {}

    def writeToJSONFile(path, fileName, data):
            filePathNameWExt = './' + path + '/' + fileName + '.json'
            with open(filePathNameWExt, 'w') as fp:
                # นับคำ
                for (word, occurance) in wordCounter.items():
                    # print('{:50}{:10}'.format(word,occurance))
                    data[word] = occurance


                sorted_x = sorted(data.items(), key=operator.itemgetter(1))
                json.dump(sorted_x, fp)
                print("complete")                # json.dump(data, fp)


    writeToJSONFile('./', 'test', data)

fh.close()
