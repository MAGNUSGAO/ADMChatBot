import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

from tensorflow.python.framework import ops
import numpy
import tflearn
import tensorflow
import random
import json
import pickle

with open("intents.json") as file:
    data = json.load(file)

#try:
    #ACTIVIATE THE LINE AFTER IF NEW JSON
    #with open("data.pickle", "rb") as f:
        #words, labels, training, output = pickle.load(f)
    #save all 4 vars in our pickle file
#except:
#print("error at 1")
words = []
labels = []
docs_x = []
docs_y = []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        #return a list of words
        wrds = nltk.word_tokenize(pattern)

        #add the words in using extend
        words.extend(wrds)
        #append tokenize words
        docs_x.append(wrds)
        #pattern in x, tag in y
        docs_y.append(intent["tag"])

        #no duplication
        if intent["tag"] not in labels:
            labels.append(intent["tag"])

#remove duplicates and question marks
words = [stemmer.stem(w.lower()) for w in words if w != "?"]
#set as no duplicates
words = sorted(list(set(words)))

labels = sorted(labels)

#train the bag of words
training = []
output = []
out_empty =[0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    wrds = [stemmer.stem(w) for w in doc]

    for w in words:
        if w in wrds:
            #to show the word exists
            bag.append(1)
        else:
            bag.append(0)
    #make a copy
    output_row = list(out_empty)
    #see labels list, to see where the value is, then we will put 1 there
    output_row[labels.index(docs_y[x])] = 1
    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

with open("data.pickle", "wb") as f:
    pickle.dump((words, labels, training),f)


#reset the graph
#ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
# add this fully connected layer
net = tflearn.fully_connected(net, 8)
#another hidden layer
net = tflearn.fully_connected(net, 8)
#softwax will give probability of each network
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
#net = tflearn.fully_connected(net, 6, activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

#try:
    #model.load("model.tflearn")
#except:
    #see same data [batch]] times
model.fit(training, output, n_epoch=1000, batch_size = 8, show_metric=True)
model.save("model.tflearn")

def bag_of_words(s, words):
    #create empty bag of words
    bag = [0 for _ in range(len(words))]
    #list of tokenize words
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            #if current word = word in sentece
            if w ==se:
                bag[i] = 1

    return numpy.array(bag)

def chat(user_input):
    input_user = user_input
    #if input_user.lower() == "quit":
        #break
    result = model.predict([bag_of_words(input_user, words)])[0]
    #gives the index of the largest value
    result_index = numpy.argmax(result)
    #spits out the label
    tag = labels[result_index]

    if result[result_index] > 0.7:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg["responses"]
        return(str(random.choice(responses)))

    else:
        return("Sorry, I didn't get that")

#chat()
