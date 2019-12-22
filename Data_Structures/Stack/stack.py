#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack():

	# def __init__(self, initial_input): -- if stack_size = None create empty list 
	# or execute with initial input
	# initialise a list with a size

	def __init__(self, stack_size):
		# Create a stack of a given stack_size
	    self.stack_array = [None] * stack_size
	    self.top = -1 

	def peek(self):
		print("Top of the stack is: {}".format(self.top))

	def push(self, item):
		if self.is_full():
			print("Oops stack is full")
		else:
			print("Item {} has been pushed onto the stack".format(item))
			self.top += 1
			self.stack_array[self.top] = item

	def pop(self):
		# pop the top of the stack
		if self.is_empty():
			print("It is an empty empty stack !")
		else:
			print("Item {} has been removed".stack_array[0])
			del(stack_array[self.top])
			self.top -= 1

	def is_empty(self):
		if None in self.stack_array:
			print("The stack is empty")
			self.print_stack()
			return True 
		else:
			print("The stack is not at all empty")
			self.print_stack()
			return False

	def is_full(self):
		if None in self.stack_array:
			print("The stack is not full")
			self.print_stack()
			return False
		else:
			print("The stack is full")
			self.print_stack()
			return True

	def print_stack(self):
		print("Stack contains the following {}".format(self.stack_array[::-1]))

	def get_size(self):
		stack_size = len(self.stack_array)
		print("Size of the stack is: {}".format(stack_size))
		return stack_size 



