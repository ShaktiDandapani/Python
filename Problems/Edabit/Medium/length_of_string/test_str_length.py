#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest
from string_length_rec import length


class TestStringLengthRecFunction(unittest.TestCase):

	def setUp(self):

		self.str1 = "apple"
		self.str2 = "exclusion"
		self.str3 = "proclivity"
		self.str4 = "exonerate"


	def test_length_fnc(self):

		self.assertEqual(length(self.str1), 5)
		self.assertEqual(length(self.str2), 9)
		self.assertEqual(length(self.str3), 10)
		self.assertEqual(length(self.str4), 9)




if __name__ == '__main__':
	unittest.main()
