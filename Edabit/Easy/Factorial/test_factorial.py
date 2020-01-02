import unittest 
from factorial import factorial, factorial_iterative


class TestFactorialFunctionas(unittest.TestCase):

	def setUp(self):
		self.number_1 = 1
		self.number_2 = 0 
		self.number_3 = 21
		self.number_4 = 71
		self.number_5 = 11 # for testing equality in both implementations

		# An important note
		# Recursive method produces a:
		# RecursionError: maximum recursion depth exceeded in comparison
		# as the limit is 2000 from python 3.x.x

	def test_recursive(self):
		self.assertEqual(factorial(self.number_1), 1)
		self.assertEqual(factorial(self.number_2), 1)
		self.assertEqual(factorial(self.number_3), 51090942171709440000)

	def test_iterative(self):
		self.assertEqual(factorial_iterative(self.number_1), 1)
		self.assertEqual(factorial_iterative(self.number_2), 1)
		self.assertEqual(factorial_iterative(self.number_3), 51090942171709440000)


	def test_implementations(self):
		self.assertEqual(factorial(self.number_1), factorial_iterative(self.number_1))
		self.assertEqual(factorial(self.number_2), factorial_iterative(self.number_2))
		self.assertEqual(factorial(self.number_3), factorial_iterative(self.number_3))
		self.assertEqual(factorial(self.number_4), factorial_iterative(self.number_4))
		self.assertEqual(factorial(self.number_5), factorial_iterative(self.number_5))


if __name__ == '__main__':
	unittest.main()