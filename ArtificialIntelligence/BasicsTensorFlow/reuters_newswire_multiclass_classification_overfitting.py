#!usr/bin/env python
#-*- coding: utf-8 -*-

from keras.datasets import reuters

from keras import models 
from keras import layers

import numpy as np 

import matplotlib.pyplot as plt 

import seaborn as sns 

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

# word_index = reuters.get_word_index()

# reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# decoded_newswire = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])

def vectorize_sequences(sequences, dimension=10000):
	results = np.zeros((len(sequences), dimension))
	for i, sequence in enumerate(sequences):
		results[i, sequence] = 1.
	return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)


def to_one_hot(labels, dimension=46):
	results = np.zeros((len(labels), dimension))
	for i, label in enumerate(labels):
		results[i, label] = 1.
	return results	

print(train_data[0], train_labels[0])

one_hot_train_labels = to_one_hot(train_labels)
one_hot_test_labels = to_one_hot(test_labels)

# Model 
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

# Compute and compile
model.compile(optimizer='rmsprop',
	          loss='categorical_crossentropy',
	          metrics=['accuracy'])

# Validating approach
x_val = x_train[:1000]
partial_x_train = x_train[1000:]

y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]


# training 
history = model.fit(partial_x_train,
	                partial_y_train,
	                epochs=20,
	                batch_size=512,
	                validation_data=(x_val, y_val))

# print(history.history.keys())

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(loss) + 1)

sns.set()

# Loss Plots
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()



acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

# Accuracy plots
plt.figure()
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and Vaidation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()


plt.show()


