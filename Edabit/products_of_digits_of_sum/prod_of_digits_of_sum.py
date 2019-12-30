#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
This problem has been taken from 
https://edabit.com/challenge/HrQoXJYqpYZ2Rqvtb

"""
from functools import reduce

def sum_dig_prod(*args):
	# Convert *args to a list
	input_list = list(args)
	final_result = 0
	# 1. Add the numbers
	addition_result = sum(input_list)

	# 2. Obtain products till only one number
	#    remains
	result = product_of_digits(addition_result)
	return result

def product_of_digits(input):

	# 1. Create a list of the added digits
	input_digits = list(str(input))

	# 2. Convert each element into an int 
	input_digits = [int(x) for x in input_digits]

	# 3. Recursive loop to keep multiplying the resul
	#    till a single number is present in the list
	#    Fulfilling the criteria "until the answer 
	#    is only 1 digit long"
	if len(input_digits) == 1:
		digit = input_digits[0]
		return digit
	elif len(input_digits) > 1:
		product = reduce((lambda x,y: x * y), input_digits)
		# Multiply each digit in product using recursion	
		return product_of_digits(product)
