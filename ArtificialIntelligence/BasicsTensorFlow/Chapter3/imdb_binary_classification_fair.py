#!usr/bin/env python
#-*- coding: utf-8 -*-

from keras.datasets import imdb 

import numpy as np

import matplotlib.pyplot as plt 

from keras import models 
from keras import layers 

from keras import optimizers
from keras import losses 
from keras import metrics 

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)



# Print a review out just to see

# word_index = imdb.get_word_index()
# reverse_word_index = dict(
# 	[(value, key) for (key, value) in word_index.items()])

# decoded_review = ' '.join(
# 	[reverse_word_index.get(i-3, '?') for i in train_data[0]])

# print(decoded_review)

# Preparing the data

def vectorize_sequences(sequences, dimension=10000):
	results = np.zeros((len(sequences), dimension))
	for i, sequence in enumerate(sequences):
		results[i, sequence] = 1.
	return results 	

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

# vectorize labels 
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000, )))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

# We can also use functions for optimizers, loss, and metrics
# :) python ka keras has it's own within the compile method and 
# therefore it can be obtained using the input argument
# else use a function of your own or available ones.

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
	          loss=losses.binary_crossentropy,
	          metrics=[metrics.binary_accuracy])

model.fit(x_train, y_train, epochs=4, batch_size=512)

results = model.evaluate(x_test, y_test)

print(results)

# Predict
prediction = model.predict(x_test)