# -*- coding: utf-8 -*-
"""
Created on Wed May 10 00:41:09 2023

@author: joaqu
"""
import tkinter as tk


class View3(tk.Frame):
    # Method 2
    # def __init__(self, parent, controller):
    #     super().__init__(parent)
    #     self.controller = controller
    #     self.label = tk.Label(self, text="")
    #     self.label.pack()
    #     self.button1 = tk.Button(self, text="Go to View 2", command=self.controller.show_view2)
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
        label = tk.Label(self, text="View 3")
        label.pack()
        button = tk.Button(self, text="Go to View 1", command=self.controller.show_view1)
        button.pack()
        
