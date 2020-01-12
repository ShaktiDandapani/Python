#!/usr/bim/env python
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton

class STGRFArgumentsWindow(QWidget):
    """
    This class is for creating a window (tabbed preferably)
    which takes in the arguments for the FEA model,
    i.e. for either the custom workflows, input parameters
    like material parameters for HGO model etc.
    
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setStyleSheet("background-color: #ebf0eb;")
        self.grid = QGridLayout(self)
        
        arg1hbox = QHBoxLayout()
        arg2hbox = QHBoxLayout()
        arg3hbox = QHBoxLayout()
        arg4hbox = QHBoxLayout()
        
        # RightSide
        rs_vbox = QVBoxLayout()
        ls_vbox = QVBoxLayout()
        
        # Widgets for the grid
        argument1 = QLabel("Arg 1")
        argument2 = QLabel("Arg 2")
        argument3 = QLabel("Arg 3")
        argument4 = QLabel("Arg 4")
        
        
        # LineEdits 
        arg1Edit = QLineEdit()
        arg2Edit = QLineEdit()
        arg3Edit = QLineEdit()
        arg4Edit = QLineEdit()
        
        arg1hbox.addWidget(argument1)
        arg1hbox.addWidget(arg1Edit)
        
        arg2hbox.addWidget(argument2)
        arg2hbox.addWidget(arg2Edit)
        
        arg3hbox.addWidget(argument3)
        arg3hbox.addWidget(arg3Edit)
        
        arg4hbox.addWidget(argument4)
        arg4hbox.addWidget(arg4Edit)        
        
        # RS widgets
        qlabel_1 = QLabel("Hi Label 1 here")
        qlabel_argtips = QLabel("Arg Tips")
        
        rs_vbox.addWidget(qlabel_1)
        rs_vbox.addWidget(qlabel_argtips)
        
        self.grid.setSpacing(10)              
        # addLayout(layout, grow, gcol, growspan, gcolspan)
        
        # Add all of these to ls_vbox
        ls_vbox.addLayout(arg1hbox)#, 0, 0, 1, 1)
        ls_vbox.addLayout(arg2hbox)#, 0, 1, 1, 1)
        ls_vbox.addLayout(arg3hbox)#, 1, 0, 1, 1)
        ls_vbox.addLayout(arg4hbox)#, 1, 1, 1, 1)
        
        self.grid.addLayout(ls_vbox, 0, 0, 4, 4)
        self.grid.addLayout(rs_vbox, 0, 10, 4, 4)
        
        self.setLayout(self.grid)
        
    # Methods for buttons 
    
    # Controller file to write to files for input 
    
    # Think how you would incorporate this in 
    # the file/ folder structure of your STGRF
    # Application.
        
        
class STGRFExecutionWindow(QWidget):
    """
    
    This window will be available after the arguments 
    for the simulation are set and would use the perl 
    automation cycle to run FEA simulations on soft tissue 
    growth and remodelling, which would then produce 
    results -> to be shown either in paraview, 
    or a separate results window .
    
    """
    
    pass 

class STGTFResultsWindow(QWidget):
    """
    
    The resultant vtk files will be read in using 
    functions and via the controller be used to obtain 
    the required result as per the button pressed. 
    (use vtk library).
    
    """
    
    pass 