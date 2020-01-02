#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""

This problem has been taken from: https://edabit.com/challenge/FF6kYPHdAcJnoosr5

Create a function that takes an integer and returns the factorial of that integer. 
That is, the integer multiplied by all positive lower integers.

Examples

factorial(3) ➞ 6

factorial(5) ➞ 120

factorial(13) ➞ 6227020800

Notes

Assume all inputs are greater than or equal to 0.

"""

def factorial(num):
	# based on recursion 
	if num <= 1: 
		return 1
	else:
		return num * factorial(num-1)

def factorial_iterative(num):
	# based on iterative method
	factorial_result = 1

	if num <= 1:# or num == 0:
		return 1 
	else:
		for i in range(1, num+1):
			# print(">", i, factorial_result)
			factorial_result *= i

	return factorial_result

if __name__ == '__main__':
	num = 55 
	print(factorial_iterative(num), "\n", factorial(num))