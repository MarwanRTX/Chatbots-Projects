import nltk
from nltk.stem import WordNetLemmatizer
import json 
import pickle

words= []
classes = []
documents = []
ignorewords = ['?','!','.',',']
data_file = open('intents.json').read()
intents = json.loads(data_file)

for intent in intents['intents']:
    for pattern in intent["patterns"]:
        w= nltk.word_tokenize(pattern)
        print("token is : {}".format(w))
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent["tag"] not in classes:
            classes.append(intent['tag'])

print("classes are : {}".format(classes))
print("documents are : {}".format(documents))
print("words are : {}".format(words))