#!/usr/bin/env python
#-*- coding: utf-8 -*-
import unittest
from cons_vowels_substrings import get_consonant_substrings, get_vowel_substrings


class TestConsVowSubstrings(unittest.TestCase):

	def setUp(self):

		self.word1 = "apple"
		self.word2 = "aviation"
		self.word3 = "hmm"
		self.word4 = "people"

	def test_vowel_subs(self):

		self.assertEqual(get_vowel_substrings(self.word1), )