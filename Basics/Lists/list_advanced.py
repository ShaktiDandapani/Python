#!/usr/bin/env python
#-*- coding: utf-8


class ListOperations():

	def __init__(self):
		self.list_array = [] 

	def create_zeros_list(self, size):

		self.list_array = [0 for x in range(0, size)]

		return self.list_array 

	def create_ones_list(self, size):
		self.list_array = [1 for x in range(0, size)]

		return self.list_array 

	def even_numbers(self, max_number):

		self.list_array = [x for x in range(0, max_number) if x % 2 == 0]

		return self.list_array

	def odd_numbers(self, max_number):
		self.list_array = [x for x in range(0, max_number) if x % 2 != 0]		

		return self.list_array

	


if __name__ == '__main__':

	test_list = ListOperations()
	even_list = test_list.odd_numbers(11)
	ones_list = test_list.create_ones_list(10)

	print("Even Numbers: ", even_list)
	print("Ones List of Size {}: {}".format(10, ones_list))


