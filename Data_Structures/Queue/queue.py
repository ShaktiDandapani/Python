#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Queue():

	def __init__(size):
		self.queue_array = [None for x in range(0, size)]
		self.front = -1
		self.rear  = 0

		pass 

	def enqueue(item):
		"""
		Add item to the queue from the rear.
		"""

		pass 

	def dequeue():
		"""
		Remove item from the queue,
		as it was inserted, i.e. 
		from the front of the queue.
		"""

		pass 

	def front(item):
		"""
		Get the front item in the queue
		"""

		pass 

	def rear(item):
				"""
		Get the last item in the queue
		"""

		pass 

	def is_full():
		"""
		Return True/ False based on whether the queue
		is full/not full.
		"""

		pass 

	def is_empty():
		"""
		Return True/ False based on whether the queue
		is empty/not empty.
		"""
		pass 