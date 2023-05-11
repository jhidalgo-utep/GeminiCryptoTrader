# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:44:46 2023

@author: joaquin
"""

import tkinter as tk

class NameView(object):
    def __init__(self, root, controller):
        self.controller = controller
        self.name_label = tk.Label(root, text="Name: ")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_name)
        self.submit_button.pack()

    def submit_name(self):
        name = self.name_entry.get()
        self.controller.set_name(name)

    def update_name_label(self, name_value):
        self.name_label.configure(text="Name: {}".format(name_value))
