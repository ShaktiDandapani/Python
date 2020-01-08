import unittest
from dupwords import find_dupped_words_expanded_version, find_dupped_words_pythonic



class TestDupWordsProblem(unittest.TestCase):


	def setUp(self):
		self.phrase1 = "Fortune favours the bold."
		self.phrase2 = "You can lead a horse to water, but you can't make him drink."
		self.phrase3 = "Look before you leap."
		self.phrase4 = "An apple a day keeps the doctor away."

	def test_dupwords_in_phrases(self):

		self.assertEqual(find_dupped_words_expanded_version(self.phrase1), True)
		self.assertEqual(find_dupped_words_expanded_version(self.phrase2), True)
		self.assertEqual(find_dupped_words_expanded_version(self.phrase3), False)
		self.assertEqual(find_dupped_words_expanded_version(self.phrase4), False)

	# def test_dupwords_implemtations(self):
	# 	self.assertEqual(find_dupped_words_expanded_version(self.phrase1), find_dupped_words_pythonic(self.phrase1))
	# 	self.assertEqual(find_dupped_words_expanded_version(self.phrase2), find_dupped_words_pythonic(self.phrase2))
	# 	self.assertEqual(find_dupped_words_expanded_version(self.phrase3), find_dupped_words_pythonic(self.phrase3))
	# 	self.assertEqual(find_dupped_words_expanded_version(self.phrase4), find_dupped_words_pythonic(self.phrase4))



if __name__ == '__main__':
	unittest.main()