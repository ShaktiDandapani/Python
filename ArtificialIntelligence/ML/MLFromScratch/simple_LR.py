#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

path = os.getcwd()+'/data/ex1data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])

# print(data.head())

# print(data.describe())

data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
plt.grid()

def compute_cost(X, y, theta):
	inner = np.power(((X*theta.T)-y), 2)
	return np.sum(inner)/ (2 * len(X))


# append a ones coluumn to the front of the data set
data.insert(0, 'Ones', 1)

# set X (training data) and y
cols = data.shape[1]
X = data.iloc[:, 0:cols-1]
y = data.iloc[:, cols-1:cols]

# convert df to numpy matrices
X = np.matrix(X.values)
y = np.matrix(y.values)

theta = np.matrix(np.array([0, 0]))

cost = compute_cost(X, y, theta)

print(cost)

def gradient_descent(X, y, theta, alpha, iters):
	temp = np.matrix(np.zeros(theta.shape))
	parameters = int(theta.ravel().shape[1])
	cost = np.zeros(iters)

	for i in range(iters):
		error = (X * theta.T) - y 

		for j in range(parameters):
			term = np.multiply(error, X[:,j])
			temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

		theta = temp
		cost[i] = compute_cost(X, y, theta)

	return theta, cost 

# initialise the variables for learning rate and iterations 
alpha = 0.01 
iters = 1000 

# perform gradient descent to "fit" the model parameters
g, cost = gradient_descent(X, y, theta, alpha, iters)


# Plot the resulting regression line
x = np.linspace(data.Population.min(), data.Population.max(), 100)
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Training Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.grid()


# Plot the error for each iteration - convex optimisation problem
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(np.arange(iters), cost, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')

plt.xlim([0, 1000])
plt.grid()
plt.show()

