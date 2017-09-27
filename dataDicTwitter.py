import json
import operator

FILE_NAME = 'hate/text_emotion_hate70'
wordCounter = {}


with open(FILE_NAME, 'r') as fh:

    for line in fh:
        line = fh.readline()
        word_list = line.replace(',', '') \
            .replace('+', '') \
            .replace('$', '') \
            .replace('\'', '') \
            .replace('/', '') \
            .replace('.', '') \
            .replace('?', '') \
            .replace('"', '') \
            .replace('"', '') \
            .replace('&', '') \
            .replace('%', '') \
            .replace(':', '') \
            .replace(';', '') \
            .replace('#', '') \
            .replace('(', '') \
            .replace(')', '') \
            .replace('[', '') \
            .replace(']', '') \
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
                # data['count'] = occurance
                # print(data)                # ใส่ข้อมูล
                # data.sort
                # sorted(occurance)
            sorted_x = sorted(data.items(), key=operator.itemgetter(1))
            json.dump(sorted_x, fp)
            print("complete")
            # json.dump(data, fp)


    writeToJSONFile('./', 'word_hate70', data)


fh.close()
