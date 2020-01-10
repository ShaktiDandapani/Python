#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

File to add the cdatsoftlib to the PYTHONPATH
(need to understand adding modules properly
and permanently to the PYTHONPATH:
1. Either manually doing it
2. automating it
3. Creating a setup.py 

"""
import os, sys 

# Get the paths 
#python_path = sys.path
curr_dir = os.getcwd()
library_name = curr_dir+'/'

sys.path.insert(0, library_name)