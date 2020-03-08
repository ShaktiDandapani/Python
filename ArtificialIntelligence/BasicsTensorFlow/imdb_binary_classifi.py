#!usr/bin/env python
#-*- coding: utf-8 -*-

from keras.datasets import imdb 

import numpy as np

# check signature for load_data() from keras andn what 
# type is imdb

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
		results[i, sequence] = 1 .
	return results 	

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

# vectorize labels 
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

# Ready for the Neural Network