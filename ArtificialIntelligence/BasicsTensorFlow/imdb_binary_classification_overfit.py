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

# Ready for the Neural Network
model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

# Validating our approach for training
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

# We can also use functions for optimizers, loss, and metrics
# :) python ka keras has it's own within the compile method and 
# therefore it can be obtained using the input argument
# else use a function of your own or available ones.

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
	          loss=losses.binary_crossentropy,
	          metrics=[metrics.binary_accuracy])

# epchs = 20 overfits it :D 

# Training the model

history = model.fit(partial_x_train,
	                partial_y_train,
	                epochs=20,
	                batch_size=512,
	                validation_data=(x_val, y_val), verbose=0)

history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
acc = history_dict['binary_accuracy']

epochs = range(1, len(acc) + 1 )

# PLotting training and validation loss 
plt.figure()
plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Plotting training and validation acccuracy
acc_values = history_dict['val_binary_accuracy']

plt.figure()
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, acc_values, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()