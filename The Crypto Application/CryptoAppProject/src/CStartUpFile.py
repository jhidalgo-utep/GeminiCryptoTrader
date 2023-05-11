# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:52:47 2023

@author: joaquin
"""

from BMainWindowFile import MainWindow

mainWindow = MainWindow()

class StartUp(object):
    def __init__(self):
        self.custom = True

    def execute_code(self):
        mainWindow.start()
        

    
        
        
