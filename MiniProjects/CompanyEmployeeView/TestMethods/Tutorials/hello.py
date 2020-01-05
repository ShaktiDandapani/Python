#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Filenam: hello.py

""" 

Simple Hello World example with PyQt5

CamelCase is disregarded, though consistency is 
preferred over purity. The reason is using snake case
allows us to discern between the QT library commands
and our own code (just a preference).

"""
import sys 

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# Initialise an instance of the application
app = QApplication(sys.argv)

# Create an instance of the application's GUI
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
hello_msg = QLabel('<h1> Hello World! </h1>', parent=window)
hello_msg.move(60, 15)

# SHow GUI
window.show()

# Run the app's event loop/ main loop
# Wrapped within sys.exit() allows the app to cleanly exit
# and release memory resources on termination.
sys.exit(app.exec_())

