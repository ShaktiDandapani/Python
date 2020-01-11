#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest

from working9to5 import over_time



class TestWorkingOverTime(unittest.TestCase):


	def setUp(self):

		self.time_sequence_1 = [9, 17, 30, 1.5]
		self.time_sequence_2 = [16, 18, 30, 1.8]
		self.time_sequence_3 = [13.25, 15, 30, 1.5]


	def test_over_time_function(self):

		self.assertEqual(over_time(self.time_sequence_1), '$240.00')
		self.assertEqual(over_time(self.time_sequence_2), '$84.00')
		self.assertEqual(over_time(self.time_sequence_3), '$52.50')

	def tearDown(self):

		self.time_sequence_1.clear()
		self.time_sequence_2.clear()
		self.time_sequence_3.clear()


if __name__ == '__main__':
	unittest.main()