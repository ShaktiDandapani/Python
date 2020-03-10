#!/usr/bin/env pytho n
# -*- coding: utf-8 -*-

from sklearn import linear_model 

import os 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

path = os.getcwd()+'/data/ex1data2.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])

# append a ones coluumn to the front of the data set
data.insert(0, 'Ones', 1)

# set X (training data) and y
cols = data.shape[1]
X = data.iloc[:, 0:cols-1]
y = data.iloc[:, cols-1:cols]

# convert df to numpy matrices
X = np.matrix(X.values)
y = np.matrix(y.values)

# Fitting the model to the data
# without creating a model of our own
model = linear_model.LinearRegression()
model.fit(X, y)

x = np.array(X[:, 1].A1)
f = model.predict(X).flatten()

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Training Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')

plt.grid()
plt.show()
