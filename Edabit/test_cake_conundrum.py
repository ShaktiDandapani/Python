import unittest
from unittest import mock
from cake_conundrum import get_total_cost

# The input needs to be checked so that it 
# is taken in as an integer.

class TestCakeConundrum(unittest.TestCase):
	
	def test_total_cost(self):
		number_of_cakes = 10
		self.assertEqual(get_total_cost(number_of_cakes), number_of_cakes*2)


if __name__ == "__main__":
	unittest.main()