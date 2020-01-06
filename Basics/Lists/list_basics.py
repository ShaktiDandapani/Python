#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""

Basics on lists, the various methods involved 
in  the default python library.

The details for each method can be found in:
https://docs.python.org/3/tutorial/datastructures.html

"""

def list_basic_methods():

	# Defining a list
	list_1 = [] 
	list_2 = list()


	# Append method .append(x) - equivalent to list_1[len(list_1):] = [x]
	# add an item to the end of the list

	for i in range(0, 10):
		list_1.append(i) 


	for i in range(0, 5):
		list_2.append(i)

	# Shallow copies
	list_3 = list_1.copy()   # without copy list_3 just acts as a pointer to list_1
	list_4 = list_1.copy()
	# Extend method
	list_3.extend(list_2)
	list_4.append(list_2)
	

	list_4.insert(len(list_4), 59)
	list_4.append(38)



	print("List 1: ", list_1)
	print("List 2: ",list_2)
	print("List 3: ",list_3)
	print("List 4: ",list_4)

	# pop an item
	print("List 4 popped: ",list_4.pop())
	print("List 4 popped(3): ",list_4.pop(3))
	print("List 4: ",list_4)
	print("List 1 cleared : ", list_1.clear())
	print("List 3 counts, number 3 : ", list_3.count(3))
	print(list_3.index(3))	


	# remaining -> sort, reverse

	return 1 



if __name__ == '__main__':
	list_basic_methods()