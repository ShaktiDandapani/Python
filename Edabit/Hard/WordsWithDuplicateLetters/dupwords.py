"""

Taken from: https://edabit.com/challenge/WS6hR6b9EZzuDTD26

Given a common phrase, return False if any individual 
word in the phrase contains duplicate letters. Return True otherwise.

"""
import collections, string

def find_dupped_words_expanded_version(input_phrase:str) -> bool:
	"""
	The function/ method reads in an input phrase
	and returns False, if any of the words in 
	the phrase contain repeating letters :)
	(using sentences without punctuation for now) 
	"""

	# 1. Removing punctuations 
	input_phrase = input_phrase.translate(str.maketrans('', '', string.punctuation))

	# 2. Split the input phrase into a list of strings
	input_phrase_words = input_phrase.split()

	# 3. Counting the repeated letters in each word 
	#    in the input phase
	letter_freq_check = 2						# Might need a better one 
	for word in input_phrase_words:
		# split each word into individual letters
		# First without collections.Counter
		letter_dict = {}
		letters = list(word)
		for letter in letters:
			# dictionary ?
			if letter not in letter_dict.keys():
				letter_dict[letter] = 1
			else:
				letter_dict[letter] += 1 
		for freq in letter_dict.values():
			if freq > 1:
				return False

	return True

def find_dupped_words_pythonic(input_phrase:str) -> bool:
	"""
	A different version of the same function, using collections
	"""
	# Test Fails ma dude --- check

	# 1. Removing punctuations 
	input_phrase = input_phrase.translate(str.maketrans('', '', string.punctuation))

	# 2. Split the input phrase into a list of strings
	input_phrase_words = input_phrase.split()

	# 3. Counting the repeated letters in each word 
	let_freq_list = [character for character, count in collections.Counter(x for x in str(input_phrase_words).split()).items() if count > 1]

	if let_freq_list != []:
		return False 

	return True 
