#!/usr/bin/env python
#-*- coding: utf-8 -*-
from collections import Counter

"""

Problem taken from:
https://edabit.com/challenge/tfbKAYwHq2ot2FK3i

Non Repeating integers
----------------------

Let's define a non-repeating integer as one whose digits are all distinct. 
97653 is non-repeating while 97252 is not (it has two 2's). 
Among the binary numbers, there are only two positive non-repeating integers: 
1 and 10. Ternary (base 3) has ten: 1, 2, 10, 20, 12, 21, 102, 201, 120, 210.

Write a function that has as it's argument the base or radix and returns 
the number of non-repeating positive integers in that base.


Examples
--------

non_repeats(2) ➞ 2

non_repeats(4) ➞ 48

non_repeats(5) ➞ 260

non_repeats(6) ➞ 1630


Notes
-----

Assume a radix of 1 is not legitimate.

"""

__author__ = 'Shaktidhar Dandapani'

def non_repeating_identifier(number):
    
    """
    
    Return True if the input number has non 
    repeating integers 
    
    """
    
    number = str(number)
    #number = list(number)
    number = [int(x) for x in number]
    
    digit_count = Counter(number)
    
    for count in digit_count.values():
        #print(values)
        if count > 1:
            return False
    
    return True 
    

def non_repeats(radix):
    
    if radix < 1:
        return 0
    else:
        # Algorithm goes here 
    
    result = non_repeating_identifier(None)
    
    return result


if __name__ == '__main__':
    print(non_repeating_identifier(123))