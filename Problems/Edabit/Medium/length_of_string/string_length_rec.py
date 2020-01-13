#!/usr/bin/env python
#-*- coding: utf-8 -*-

def length(input_string):

	lc = 1
	if input_string == "":
		return 0
	else:
		return lc + length(input_string[:-1])

if __name__ == '__main__':
	str_length = length("apple")
	print(str_length)