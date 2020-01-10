#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

class CDSMainWindow(QMainWindow):
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CDatSoft")
        self.setFixedSize(1024, 768)
        
        self._central_widget_layout = QVBoxLayout()
        self._central_widget = QWidget(self)
        self._central_widget.setLayout(self._central_widget_layout)
        self.setCentralWidget(self._central_widget)
        
        # add the menu bar
        self.create_menu_bar()
        self.create_status_bar()
        self.create_tool_bar()
        
        
    # methods to create menus toolbars
    # methods to create more windows through either
    # dialog boxes or tabs :)
    
    def create_menu_bar(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)
        
    
    def create_tool_bar(self):
        
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)
        tool_bar.addAction('Exit', self.close)
    
    def create_status_bar(self):
        
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)