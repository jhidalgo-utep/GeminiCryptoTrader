# -*- coding: utf-8 -*-
"""
Created on Wed May 10 00:26:37 2023

@author: joaqu
"""

import tkinter as tk


class View2(tk.Frame):
    # # For ONLY 2 VIEWS - Method 1
    # def __init__(self, parent, controller):
    #     super().__init__(parent)
    #     self.controller = controller
    #     self.label = tk.Label(self, text="This is View 2")
    #     self.label.pack()
    #     self.button = tk.Button(self, text="Back", command=self.controller.show_view1)
    #     self.button.pack()
        
###################################################
    # # Method 2
    # def __init__(self, parent, controller):
    #     super().__init__(parent)
    #     self.controller = controller
    #     self.label = tk.Label(self, text="")
    #     self.label.pack()
    #     self.button1 = tk.Button(self, text="Next", command=self.controller.show_view3)
    #     self.button1.pack()
    #     self.button2 = tk.Button(self, text="Back", command=self.controller.show_view1)
    #     self.button2.pack()

    # def update_label(self, message):
    #     self.label.config(text=message)
###################################################
    # Method 3
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="View 2")
        label.pack()
        button = tk.Button(self, text="Go to View 3", command=self.controller.show_view3)
        button.pack()
        