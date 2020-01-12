#!/usr/bim/env python
#-*- coding: utf-8 -*-

import sys 

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMenuBar

import inner_windows as invy

class STGRFMainWindow(QMainWindow):
    """
    The main window class for STGRF, 
    
    this serves as the main window definition 
    for the software and contains all sub windows,
    for 
    a. Argument Listings.
    b. Execution of Custom Workflows.
    c. Result Viewing.
    
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.init_ui()
        
    def init_ui(self):
        
        self.setWindowTitle("STGRF")
        self.setFixedSize(1366, 768)
        
        # Adding menu bar 
        self.create_menu_bar()
        
        # Add the tabs to the main window
        self.window_tabs = STGRFTabsWindow(self)
        self.setCentralWidget(self.window_tabs)

    def create_menu_bar(self):
        # Adding menus
        self.menu_bar = self.menuBar().addMenu("&File")
        self.edit_bar = self.menuBar().addMenu("&Edit")
        
        self.menu_bar.addAction('Open File') # add function
        
        self.menu_bar.addSeparator()
        self.menu_bar.addAction('&Exit', self.close)

#  class below can be put in a separate file if need be.
class STGRFTabsWindow(QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        
        # initialise the tab screen 
        self.tabs = QTabWidget()
        # import from other file 
        # Import tabs from inner_windows.py 
        # File.
        
        self.tab2 = QWidget()

        args_window = invy.STGRFArgumentsWindow(parent)        
        # Add the tabs 
        self.tabs.addTab(args_window, "Arguments/ Input Parameters")
        self.tabs.addTab(self.tab2, "Tab 2")
        
        # Add tabs to QTabWidget  
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

if __name__ == '__main__':
    
    stgrf_main = QApplication(sys.argv)
    view = STGRFMainWindow()
    view.show()
    sys.exit(stgrf_main.exec_())