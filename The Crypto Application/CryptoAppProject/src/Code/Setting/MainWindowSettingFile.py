# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:26:19 2023

@author: joaquin
"""


OPEN_APP_WIDTH = 1400
OPEN_APP_HEIGHT = 680

OPEN_X_OFFSET = 70
OPEN_Y_OFFSET = 50

MY_APPLICATION_NAME = "The Crypto Application"

MAIN_WINDOW_COLOR_BG = "#e8f4f8"

class MainWindowSetting(object):
    def __init__(self, root):
        self.set_window_size(root)
        self.set_window_name(root)
        self.set_window_color(root)
    
    def set_window_size(self, root):
        open_size = ""
        open_size += str(OPEN_APP_WIDTH) + "x" + str(OPEN_APP_HEIGHT) + "+" + str(OPEN_X_OFFSET) + "+" + str(OPEN_Y_OFFSET)  
        root.geometry(open_size)
        
    def set_window_name(self, root):
        root.title(MY_APPLICATION_NAME)
        
    def set_window_color(self, root):
        root.configure(bg=MAIN_WINDOW_COLOR_BG)
        
    def get_window_color(self):
        return MAIN_WINDOW_COLOR_BG
        
    
    
    