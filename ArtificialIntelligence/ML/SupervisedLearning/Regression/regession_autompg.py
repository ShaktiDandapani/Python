#!usr/bin/env python
#-*- coding: utf-8 -*-

"""

taken from:
https://www.tensorflow.org/tutorials/keras/regression

"""

import pathlib

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import seaborn as sns 

import tensorflow as tf 

from tensorflow import keras 
from tensorflow.keras import layers 


import tensorflow_docs as tfdocs 
import tensorflow_docs.plots
import tensorflow_docs.modeling

dataset_path = "autompgdata/auto-mpg.data"


column_names = ['MPG', 'Cylinders', 'Displacement', 
                'Horsepower', 'Weight', 'Acceleration',
                'Model Year', 'Origin']

raw_dataset = pd.read_csv(dataset_path, names=column_names,
	                      na_values = "?", comment="\t",
	                      sep=" ", skipinitialspace=True)

dataset = raw_dataset.copy() # shallow or deep - check
# print(dataset.tail())	                                  


# Cleaning the dataet 
dataset.isna().sum()

# drop those rows just for now, since this tutorial doest need it
dataset = dataset.dropna()

# Converting Origin column to be numeric
dataset['Origin'] = dataset['Origin'].map(({1: 'USA',
	                                        2: 'Europe',
	                                        3: 'Japan'}))

dataset = pd.get_dummies(dataset, prefix='', prefix_sep='')
# print(dataset.tail())	                                        


# Splitting data into training and test sets 
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# Plot them using pairplot
sns.pairplot(train_dataset[["MPG", "Cylinders", "Displacement", "Weight"]], diag_kind="kde")

# plt.show()

# Looking at overall statistics
train_stats = train_dataset.describe()
train_stats.pop("MPG")
train_stats = train_stats.transpose()
# print(train_stats)

# Split features from labels
# ----------------------------------------------------------------
# Separate the target value, or "label", from the features. 
# This label is the value that you will train the model to predict.

train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')

# feature normalisation if scales and ranges are different

def norm(x):
	return (x - train_stats['mean']) / train_stats['std']

normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

# Build the model 
def build_model():
	model = keras.Sequential([
		layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
		layers.Dense(64, activation='relu'),
		layers.Dense(1)
		])

	optimizer = tf.keras.optimizers.RMSprop(0.001)

	model.compile(loss='mse',
				  optimizer=optimizer,
				  metrics=['mae', 'mse'])

	return model

model = build_model()

# print(model.summary())

# Batch of 10 examples from training data and predict
example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
# print(example_result)

# Train the model 

EPOCHS = 1000

history = model.fit(
	normed_train_data, train_labels,
	epochs= EPOCHS, validation_split=0.2, verbose=0,
	callbacks=[tfdocs.modeling.EpochDots()])

# Visualise using history object
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch 
print(hist.tail())

# PLot and visualise on a graph 
plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)

plt.figure()
plotter.plot({'Basic': history}, metric = "mean_absolute_error")
plt.ylim([0, 10])
plt.ylabel('MAE [MPG]')

plt.figure()
plotter.plot({'Basic': history}, metric = "mean_squared_error")
plt.ylim([0, 20])
plt.ylabel('MSE [MPG]')

# plt.show()


# EarlyStopping callback - stop if the training does not 
# show improvements in validation error

model = build_model()

# Patience parameter - amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss',
	                                       patience=10)

early_history = model.fit(normed_train_data, train_labels, 
	                      epochs=EPOCHS, validation_split=0.2, verbose=0,
	                      callbacks=[early_stop, tfdocs.modeling.EpochDots()])

plt.figure()
plotter.plot({'Early Stopping': early_history}, metric="mean_absolute_error")
plt.ylim([0, 10])
plt.ylabel('MAE[MPG]')


# Finally testing our model using test data set
loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} MPG".format(mae))

# Making predictions :D 
test_predictions = model.predict(normed_test_data).flatten()

plt.figure()
a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [MPG]')
plt.ylabel('Predictions [MPG]')
lims = [0, 50]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)


# Error Distribution
error = test_predictions - test_labels 

plt.figure()
plt.hist(error, bins=25)
plt.xlabel("Prediction Error [MPG]")
_=plt.ylabel("Count")

plt.show()

