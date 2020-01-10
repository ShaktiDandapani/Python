#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""

The base class for the GUI to be developed.
Contains the initialisation code using 
various components/windows/widgets from the
PyQt5 library

"""
# Os for file paths etc -> keep a track sir
import sys, os 

from PyQt5.QtWidgets import QApplication
from main_window import CDSMainWindow  
import cdatsoftlib

if __name__ == '__main__':
	# Any extra arguments or CLI arguments 
	# to be handled here - use modules 
	# for command line argument execution
	
	cdatsoft_app = QApplication(sys.argv)
	# define what the view is 
	view = CDSMainWindow()
	view.show()
	# model = ?
	#controller_class(model=model, view=view)
	# execute the view
	sys.exit(cdatsoft_app.exec_())