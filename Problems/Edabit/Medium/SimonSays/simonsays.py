#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

The problem has been taken from: 
https://edabit.com/challenge/YzcnFjMEKQfyHAg6B

Simon Says

Create a function that takes in two lists and returns True 
if the second list follows the first list by one element, 
and False otherwise. In other words, determine if the second 
list is the first list shifted to the right by 1.


Examples

simon_says([1, 2], [5, 1]) ➞ True

simon_says([1, 2], [5, 5]) ➞ False

simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True

simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False

Notes

Both input lists will be of the same length, 
and will have a minimum length of 2.

The values of the 0-indexed element in the first list 
and the n-1th indexed element in the second list do 
not matter.

"""


def simon_says(list_1, list_2):

	if list_1[-2] == list_2[-1]: 
		return True
	return False
	 

if __name__ == '__main__':
	list_1 = [1, 2, 3]
	list_2 = [0, 1, 2]
	print(simon_says(list_1, list_2))

