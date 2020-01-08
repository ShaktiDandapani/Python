#/usr/bin/env python
#-*- coding: utf-8 -*-

import sys 

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel 
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit


class CDatBaseWindow(QMainWindow):
	""" Main Intro Window """
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("ABC Company Information")

		# Size of the Main Window
		self.setFixedSize(1024, 768)
		
		# Set layout
		self.core_layout = QVBoxLayout()
		
		# Set this as the central widget
		self._central_widget = QWidget(self)
		self._central_widget.setLayout(self.core_layout)
		self.setCentralWidget(self._central_widget)

	

def main():
	company_database = QApplication(sys.argv)

	view = CDatBaseWindow()
	view.show()

	sys.exit(company_database.exec_())

if __name__ == '__main__':
	main()