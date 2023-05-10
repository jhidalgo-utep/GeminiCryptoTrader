# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:52:47 2023

@author: joaquin
"""

from tkinter import Tk
# from Code.Launch.MainApplication import MainApp
from Code.Launch.Controller import Controller




class StartUp(object):
    def __init__(self):
        self.custom = True


    def execute_code(self):
        root = Tk()
        app = Controller(root)
        root.mainloop()

    
        
        
