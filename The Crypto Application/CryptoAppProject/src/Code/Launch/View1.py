# -*- coding: utf-8 -*-
"""
Created on Wed May 10 00:25:30 2023

@author: joaqu
"""
import tkinter as tk

# For method 1 & 2 - I use tk.Frame as obj param but because app = Controller(root) is called
# For method 3 - I use Frame as obj param but because Controller(root) is called. Thus I use Label and Button instead of tk'.Label' or tk'.Button' preface

class View1(tk.Frame):
    # For ONLY 2 VIEWS - Method 1
    # def __init__(self, parent, controller):
    #     super().__init__(parent)
    #     self.controller = controller
    #     self.label = tk.Label(self, text="")
    #     self.label.pack()
    #     self.button = tk.Button(self, text="Next", command=self.controller.show_view2)
    #     self.button.pack()

    # def update_label(self, message):
    #     self.label.config(text=message)
###################################################
    # # Method 2
    # def __init__(self, parent, controller):
    #     super().__init__(parent)
    #     self.controller = controller
    #     self.label = tk.Label(self, text="")
    #     self.label.pack()
    #     self.button1 = tk.Button(self, text="Next", command=self.controller.show_view2)
    #     self.button1.pack()
    #     self.button2 = tk.Button(self, text="Go to View 3", command=self.controller.show_view3)
    #     self.button2.pack()

    # def update_label(self, message):
    #     self.label.config(text=message)
###################################################
    # Method 3
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="View 1")
        label.pack()
        button = tk.Button(self, text="Go to View 2", command=self.controller.show_view2)
        button.pack()