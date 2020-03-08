#!/usr/bin/env python
#-*- coding: utf8 -*-

from keras.datasets import mnist
from keras import models 
from keras import layers 

from keras.utils import to_categorical

import matplotlib.pyplot as plt 

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# neural network
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28, )))
network.add(layers.Dense(10, activation='softmax'))

# Compilation step
network.compile(optimizer='rmsprop',
	            loss='categorical_crossentropy',
	            metrics=['accuracy'])


# test a plot

digit = train_images[4]


plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

# Pre processing the image data to fit between intervals of 0-1 rather than [0, 255]
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


# Categorically encoding labels - preparing labels
train_labels = to_categorical(train_labels)
test_labels  = to_categorical(test_labels)

# training the model using fit
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# accuracy for training reaches 0.9887

# testing the model on test set 

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc', test_acc)

