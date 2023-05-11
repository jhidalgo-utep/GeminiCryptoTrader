# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:42:26 2023

@author: joaquin
"""

import tkinter as tk

from Code.Controller.CounterControllerFile import CounterController  
from Code.Controller.NameControllerFile import NameController
from Code.Menu.MainWindowMenuFile import MainWindowMenu
from Code.Setting.MainWindowSettingFile import MainWindowSetting

class MainWindow(object):
    def __init__ (self):
        self.custom_main = True
        
    def start(self):
        root = tk.Tk()
        
        mainWindowSetting = MainWindowSetting(root) # SET Window 
        
        myMenuBar = MainWindowMenu(root) # SET Menu
        
        counter_controller = CounterController(root) # SET Counter
        
        name_controller = NameController(root) # SET Name
        # color_controller = ColorController(root)
        
        root.mainloop()