#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest 
import time 
from bubble_sort import bubble_sort, bubble_sort_pythonic
# use time it

class TestBubbleSortAlgorithm(unittest.TestCase):

	def setUp(self):
		self.start_time = time.time()

	def tearDown(self):
		t = time.time() - self.start_time
		print("{} : {} seconds".format(self.id(), t))

	def test_bubble_sort_unordered_list(self):
		input_array = [-10, 4, 20, 1, -100, 50]
		self.assertEqual(bubble_sort(input_array), sorted(input_array))

	def test_bubble_sort_sorted_list(self):
		input_array = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		self.assertEqual(bubble_sort(input_array), sorted(input_array))

	def test_bubble_sort_characters(self):
		input_array = ['a', 'b', 'z', 'x', 'y', 'o', 'd']
		self.assertEqual(bubble_sort(input_array), sorted(input_array))

class TestBubbleSortPythonic(unittest.TestCase):

	def setUp(self):
		self.start_time = time.time()

	def tearDown(self):
		t = time.time() - self.start_time
		print("{} : {} seconds".format(self.id(), t))

	def test_bubble_sort_unordered_list(self):
		input_array = [-10, 4, 20, 1, -100, 50]
		self.assertEqual(bubble_sort_pythonic(input_array), sorted(input_array))

	def test_bubble_sort_sorted_list(self):
		input_array = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		self.assertEqual(bubble_sort_pythonic(input_array), sorted(input_array))

	def test_bubble_sort_characters(self):
		input_array = ['a', 'b', 'z', 'x', 'y', 'o', 'd']
		self.assertEqual(bubble_sort_pythonic(input_array), sorted(input_array))
		
if __name__ == '__main__':
	unittest.main()
