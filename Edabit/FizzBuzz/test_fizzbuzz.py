#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fizzbuzz import fizzbuzz

# Problem can be found on 
# https://edabit.com/challenge/WXqH9qvvGkmx4dMvp

"""
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

    If the number is a multiple of 3 the output should be "Fizz".
    If the number given is a multiple of 5, the output should be "Buzz".
    If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
    If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.

"""


class TestFizzBuzz(unittest.TestCase):

	def test_fizz(self):
		input_number = 6
		self.assertEqual(fizzbuzz(input_number), "Fizz")


	def test_buzz(self):
		input_number = 25
		self.assertEqual(fizzbuzz(input_number), "Buzz")


	def test_fizzbuzz(self):
		input_number = 15
		self.assertEqual(fizzbuzz(input_number), "FizzBuzz")

	def test_no_fizzbuzz(self):
		input_number = 4
		self.assertEqual(fizzbuzz(input_number), 4)


if __name__ == '__main__':
	unittest.main()

	