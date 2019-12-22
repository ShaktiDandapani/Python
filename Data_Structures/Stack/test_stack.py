#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from stack import Stack


class TestStack(unittest.TestCase):

	def setUp(self):
		self.stack_size = 10 
		self.new_stack = Stack(self.stack_size)

	def test_size_check(self):
		self.assertEqual(self.new_stack.get_size(), self.stack_size)

	def test_full_stack(self):
		for i in range(0, 10):
			self.new_stack.push(i)
		self.assertTrue(self.new_stack.is_full())

	def test_empty_stack(self):
		for i in range(0, 10):
			self.new_stack.push(i)
		self.assertTrue(self.new_stack.is_empty())


if __name__ == "__main__":
	unittest.main()