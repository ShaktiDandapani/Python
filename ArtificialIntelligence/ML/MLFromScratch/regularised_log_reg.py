#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt


path = os.getcwd() + '/data/ex2data2.txt'
data2 = pd.read_csv(path, header=None, names=['Test 1', 'Test 2', 'Accepted'])

# Sort input data into positives and negatives based 
# on acceptance
positive = data2[data2['Accepted'].isin([1])]
negative = data2[data2['Accepted'].isin([0])]

fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(positive['Test 1'], positive['Test 2'], s=50, c='b', marker='o', label='Accepted')
ax.scatter(negative['Test 1'], negative['Test 2'], s=50, c='r', marker='x', label='Rejected')
ax.legend()
ax.set_xlabel('Test 1 Score')
ax.set_ylabel('Test 2 Score')



# Since data set is not simple, it would be necessary to 
# use a polynomial

degree = 5 
x1 = data2['Test 1']
x2 = data2['Test 2']

data2.insert(3, 'Ones', 1)

for i in range(1, degree):
	for j in range(0, i):
		data2['F' + str(i) + str(j)] = np.power(x1, i-j) * np.power(x2, j)

print(data2.head())

data2.drop('Test 1', axis=1, inplace=True)
data2.drop('Test 2', axis=1, inplace=True)


# Modify cost and gradient functions to include the regularization term.
# In each case the regulariser s added on to the previous calculation.
def sigmoid(z):
	return 1 / (1 + np.exp(-z))

def cost_reg(theta, X, y, learning_rate):
	theta = np.matrix(theta)
	X = np.matrix(X)
	y = np.matrix(y)
	first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
	second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
	reg = (learning_rate / 2 * len(X)) * np.sum(np.power(theta[:, 1:theta.shape[1]], 2))

	# reg - penalty function
	# learning_rate - how much wieght reg holds in the cost function (hyper plane)

	return np.sum(first - second / len(X)) + reg


def gradient_reg(theta, X, y, learning_rate):
	theta = np.matrix(theta)
	X = np.matrix(X)
	y = np.matrix(y)

	parameters = int(theta.ravel().shape[1])
	grad = np.zeros(parameters)

	error = sigmoid(X * theta.T) - y

	for i in range(parameters):
		term = np.multiply(error, X[:, i])

		if (i == 0):
			grad[i] = np.sum(term) / len(X)
		else:
			grad[i] = (np.sum(term) / len(X)) + ((learning_rate / len(X)) * theta[:, i])

	return grad 

# Predict on a dataset X

def predict(theta, X):
	probability = sigmoid(X * theta.T)
	return [1 if x>=0.5 else 0 for x in probability]	

# set X and yy
cols = data2.shape[1]
X2 = data2.iloc[:,1:cols]
y2 = data2.iloc[:, 0:1]

# numpy arrays
X2 = np.array(X2.values)
y2 = np.array(y2.values)
theta2 = np.zeros(11)

learning_rate = 1 

cost_ = cost_reg(theta2, X2, y2, learning_rate)

# From scipy
result2 = opt.fmin_tnc(func=cost_reg, x0=theta2, fprime=gradient_reg, args=(X2, y2, learning_rate))

# Performance evaluation
theta_min = np.matrix(result2[0])
predictions = predict(theta_min, X2)
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y2)]
accuracy = (sum(map(int, correct)) % len(correct))

print('accuracy = {0}%'.format(accuracy))

plt.show()