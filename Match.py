import json



FILE_NAME_A = 'fun/word_fun70_gen.json'
FILE_NAME_B = 'worry/word_worry70_gen.json'
with open(FILE_NAME_A) as f1 , open(FILE_NAME_B) as f2:
    # FILE_NAME_A = set()
    a = json.load(f1)
    b = json.load(f2)
aList = []
bList = []
for i in a:
    aList.append(i[0])

for i in b:
    bList.append(i[0])

# c = json.intersection(happiness,sadness)
# c = set(happiness).intersection(sadness)
print (aList)