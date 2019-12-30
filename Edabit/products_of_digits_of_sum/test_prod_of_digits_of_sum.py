import unittest 
from prod_of_digits_of_sum import sum_dig_prod



class TestProdOfDigitsOfSum(unittest.TestCase):
	"""
	Passed the Edabit test checker :D
	"""
	def test_functionality(self):
		self.assertEqual(sum_dig_prod(1, 2, 3, 4, 5, 6), 2)
		self.assertEqual(sum_dig_prod(0), 0)
		self.assertEqual(sum_dig_prod(16, 28), 6)


if __name__ == '__main__':
	unittest.main()

