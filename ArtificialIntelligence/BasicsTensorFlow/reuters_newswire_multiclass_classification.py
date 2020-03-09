#!usr/bin/env python
#-*- coding: utf-8 -*-

from keras.datasets import reuters

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

print(len(train_data))
print(len(test_data))

word_index = reuters.get_word_index()

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

decoded_newswire = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])

print(reverse_word_index)

print("-"*30)

print(train_data[0])
print("*"*30)
print(decoded_newswire)