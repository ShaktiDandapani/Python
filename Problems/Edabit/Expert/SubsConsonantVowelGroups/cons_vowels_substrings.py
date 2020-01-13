#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

Problem Taken from:
https://edabit.com/challenge/BcjsjPPmPEMQwB86Y

Substring Consonant-Vowel Groups
--------------------------------

Write two functions:

    One to retrieve all unique substrings that start and end with a vowel.
    One to retrieve all unique substrings that start and end with a consonant.

The resulting array should be sorted in lexicographic ascending order (same order as a dictionary).

Examples
--------

get_vowel_substrings("apple")
➞ ["a", "apple", "e"]

get_vowel_substrings("hmm") ➞ []

get_consonant_substrings("aviation")
➞ ["n", "t", "tion", "v", "viat", "viation"]

get_consonant_substrings("motor")
➞ ["m", "mot", "motor", "r", "t", "tor"]

Notes
-----

* Remember the output array should have unique values.
* The word itself counts as a potential substring.
* Exclude the empty string when outputting the array.

# Code Passed Edabit Tests :)

"""

_vowels = ["a", "e", "i", "o", "u"]


def get_vowel_substrings(o_input_word):
	unique_word_list = []

	# 1. Convert input word into a list of characters
	input_word = list(o_input_word) # is this necessary ?
	word_found = False

	# Looping to obtain all substrings	
	for i in range(0, len(input_word)):
		u_word = []
		if input_word[i] in _vowels:
			while word_found == False:
				for j in range(i, len(input_word)):
					u_word.append(input_word[j])
					if input_word[j] in _vowels:
						# Stop 
						word = "".join(u_word)
						unique_word_list.append(str(word))
						word_found = True 
		word_found = False

	# To add the character if it is in the vowels list
	for character in input_word:
		if character in _vowels:
			unique_word_list.append(character)

	unique_word_list = sorted(list(set(unique_word_list)))
	return unique_word_list

def get_consonant_substrings(o_input_word):

	"""

	First try with splitting the word into 
	an array, and later try using regex.

	"""
	unique_word_list = []
	# 1. Convert input word into a list of characters
	input_word = list(o_input_word) # is this necessary ?


	# 2. Looping to obtain all substrings
	word_found = False
	for i in range(0, len(input_word)):
		u_word = []
		if input_word[i] not in _vowels:
			while word_found == False:
				for j in range(i, len(input_word)):
					u_word.append(input_word[j])
					if input_word[j] not in _vowels:
						# Stop 
						word = "".join(u_word)
						unique_word_list.append(str(word))
						word_found = True 
		word_found = False

	# To add the character if it is in the cons list
	for character in input_word:
		if character not in _vowels:
			unique_word_list.append(character)

	unique_word_list = sorted(list(set(unique_word_list)))
	return unique_word_list

if __name__ == '__main__':
	word = "carrot"
	get_vowel_substrings(word)