#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Node():
    
    def __init__(self, value=None):
        
        # List of children nodes
        self.children_nodes = []
        self.value = value
        
    def check_child_nodes_list(self):
        
        
        pass 
    
    def number_of_children(self):
        
        
        return len(self.children_nodes) 
    
    