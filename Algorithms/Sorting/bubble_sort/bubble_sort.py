#!/usr/bin/env python
#-*- coding: utf-8 -*-


# Before each algo
# 1. Identify best case and worst case
# 2. Provide efficiency for each
# 3. Big OH :P
# what if duplicates
# what if array has only one value throughout	
# always be on the lookout for edge cases 
# and add them to your tests

def bubble_sort(input_array):

	# Based on the definition of bubble sort
	
	for i in range(0, len(input_array)-1):
		for j in range(0, len(input_array)-1):
			if input_array[j] > input_array[j+1]:
				temp_var = input_array[j]
				input_array[j] = input_array[j+1]
				input_array[j+1] = temp_var

	return input_array

def bubble_sort_improved(input_array):

	pass 

# if __name__ == '__main__':
# 	sample_array = [4, 1, 3, -1, 0, 10, 11]
# 	output = bubble_sort(sample_array)
# 	print(output)