#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

Problem taken from:
https://edabit.com/challenge/dfep4NR2twAFTdt9k

Matrix Multiplication
Create a function that multiplies two matricies (n x n each).

Examples

matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]

matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]) ➞ [[66, 15], [67, 14]]

matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]) ➞ [[57, 59], [18, 18]]

Notes

Limit yourself to 2 x 2 matricies.

"""

def matrix_mult(matrix_1, matrix_2):
	# Try not using numpy
	# This is using a restriction i.e. 2x2
	# not applicable for nxn 
	# needs a generalisation
	number_of_rows = len(matrix_1)
	number_of_columns = len(matrix_1[0])

	# matrix_3 = c
	c00 = 0
	c01 = 0
	c10 = 0
	c11 = 0

	a = matrix_1
	b = matrix_2

	for i in range(0, number_of_rows):
		for j in range(0, number_of_columns):
			c00 = a[0][0] * b[0][0] + a[0][1] * b[1][0]
			c01 = a[0][0] * b[0][1] + a[0][1] * b[1][1]
			c10 = a[1][0] * b[0][0] + a[1][1] * b[1][0]
			c11 = a[1][0] * b[0][1] + a[1][1] * b[1][1]

	C = [[c00, c01], [c10, c11]]

	return C


if __name__ == '__main__':
	print(matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]))