#!/usr/bin/env python
#-*- coding: utf-8 -*-


import os 

curr_dir = os.getcwd()

print(curr_dir)

chng_dir = os.chdir('/home/')
curr_dir = os.getcwd()

print(curr_dir)

