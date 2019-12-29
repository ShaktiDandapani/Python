#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Queue():

	def __init__(self, size):

		self.queue_array = [None for x in range(0, size)]
		self.front = -1
		self.rear  = 0

	def enqueue(self, item):
		"""
		Add item to the queue from the rear.
		"""
		self.front += 1
		self.queue_array[self.front] = item
		print("Item {} added to the queue".format(item))

	def dequeue(self):

		"""
		Remove item from the queue,
		as it was inserted, i.e. 
		from the front of the queue.
		"""

		self.queue_array.pop(self.front)
		self.front -= 1


	def front(self, item):

		"""
		Get the front item in the queue
		"""

		return self.queue_array[self.front] 

	def rear(self, item):
		"""
		Get the last item in the queue
		"""
		return self.queue_array[self.rear]

	def is_full(self):

		"""
		Return True/ False based on whether the queue
		is full/not full.
		"""
		if None in self.queue_array:
			print("The queue is not full")
			return False
		else:
			print("The queue is full")
			return True

	def is_empty(self):
		"""
		Return True/ False based on whether the queue
		is empty/not empty.
		"""
		empty_bool = True

		# First check is to see if the queue is an 
		# empty list, a result of popping.
		if self.queue_array != []:
			for item in self.queue_array:
				# Here, check if it's the origial 
				# queue with None items else it's not
				# empty
				if item != None:
					empty_bool = False
					return empty_bool
		else:
			return empty_bool
