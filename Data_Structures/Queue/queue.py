#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Queue():

<<<<<<< HEAD
	def __init__(self, size):
=======
	def __init__(size):
>>>>>>> a17c8c67296eaab636eb52ff773c85be1ebcc73a
		self.queue_array = [None for x in range(0, size)]
		self.front = -1
		self.rear  = 0

<<<<<<< HEAD
	def enqueue(self, item):
		"""
		Add item to the queue from the rear.
		"""
		self.front += 1
		self.queue_array[self.front] = item
		print("Item {} added to the queue".format(item))


	def dequeue(self):
=======
		pass 

	def enqueue(item):
		"""
		Add item to the queue from the rear.
		"""

		pass 

	def dequeue():
>>>>>>> a17c8c67296eaab636eb52ff773c85be1ebcc73a
		"""
		Remove item from the queue,
		as it was inserted, i.e. 
		from the front of the queue.
		"""
<<<<<<< HEAD
		self.queue_array.pop(self.front)
		self.front -= 1
		 
	def front(self, item):
=======

		pass 

	def front(item):
>>>>>>> a17c8c67296eaab636eb52ff773c85be1ebcc73a
		"""
		Get the front item in the queue
		"""

<<<<<<< HEAD
		return self.queue_array[self.front] 

	def rear(self, item):
		"""
		Get the last item in the queue
		"""
		return self.queue_array[self.rear]

	def is_full(self):
=======
		pass 

	def rear(item):
				"""
		Get the last item in the queue
		"""

		pass 

	def is_full():
>>>>>>> a17c8c67296eaab636eb52ff773c85be1ebcc73a
		"""
		Return True/ False based on whether the queue
		is full/not full.
		"""
<<<<<<< HEAD
		if None in self.queue_array:
			print("The queue is not full")
			return False
		else:
			print("The queue is full")
			return True

	def is_empty(self):
=======

		pass 

	def is_empty():
>>>>>>> a17c8c67296eaab636eb52ff773c85be1ebcc73a
		"""
		Return True/ False based on whether the queue
		is empty/not empty.
		"""
<<<<<<< HEAD
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

=======
		pass 
>>>>>>> a17c8c67296eaab636eb52ff773c85be1ebcc73a
