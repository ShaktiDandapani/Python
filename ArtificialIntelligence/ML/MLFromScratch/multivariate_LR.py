#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path = os.getcwd() + '/data/ex1data2.txt'
data2 = pd.read_csv(path, header=None, names=['Size', 'Bedrooms', 'Price'])

print(data2.head())
print(data2.describe())

# Feature Normalisation necessary as the units withi the data tables
# for each column are vastly different and the regression algorithm
# might end up being weighted too heavily by a variable which has
# higher number values and fluctuations, example bedrroms and size


data2 = (data2 - data2.mean()) / data2.std()
print(data2.head())


def compute_cost(X, y, theta):
	inner = np.power(((X*theta.T)-y), 2)
	return np.sum(inner)/ (2 * len(X))


def gradient_descent(X, y, theta, alpha, iters):
	temp = np.matrix(np.zeros(theta.shape))
	parameters = int(theta.ravel().shape[1])
	cost = np.zeros(iters)

	for i in range(iters):
		error = (X * theta.T) - y

		for j in range(parameters):
			term = np.multiply(error, X[:, j])
			temp[0, j] = theta[0, j] - ((alpha/len(X)) * np.sum(term))

		theta = temp 
		cost[i] = compute_cost(X, y, theta)

	return theta, cost

# add ones column
data2.insert(0, 'Ones', 1)

# set X and y 
cols = data2.shape[1]
X2 = data2.iloc[:, 0: cols-1]
y2 = data2.iloc[:, cols-1:cols]

# convert to matrices and initialisse theta 
X2 = np.matrix(X2.values)
y2 = np.matrix(y2.values)
theta2 = np.matrix(np.array([0, 0, 0]))

# perform linear regression on the data set 
alpha = 0.01
iters = 1000
g2, cost2 = gradient_descent(X2, y2, theta2, alpha, iters)

# get cost(error) of the model 
cost = compute_cost(X2, y2, g2)

# print(cost)

# Plot the error vs training epoch 

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(np.arange(iters), cost2, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')

plt.grid()
plt.show()