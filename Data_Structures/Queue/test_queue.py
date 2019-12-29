import unittest
from queue import Queue


class TestQueueOperations(unittest.TestCase):

	def setUp(self):
		self.size = 5
		self.sample_q = Queue(self.size)

		for i in range(0, self.size):
			self.sample_q.enqueue(i)

	def test_full_queue(self):
		
		is_full_bool = self.sample_q.is_full()

		self.assertTrue(is_full_bool, True)

	def test_empty_queue(self):

		for i in range(0, self.size):
			self.sample_q.dequeue()
			print(self.sample_q.queue_array)
		is_empty_bool = self.sample_q.is_empty()
		self.assertTrue(is_empty_bool, True)

		pass 


if __name__ == '__main__':
	unittest.main()