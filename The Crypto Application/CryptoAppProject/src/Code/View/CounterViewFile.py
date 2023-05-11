# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:43:50 2023

@author: joaquin
"""

import tkinter as tk

class CounterView(object):
    def __init__(self, root, controller):
        self.controller = controller
        
        self.my_frame = tk.Frame(root, padx=0, pady=100)
        self.my_frame.pack()
        
        # var1 = controller.get_window_color()
        self.my_frame.configure(bg="blue")
        
        
        self.counter_label = tk.Label(self.my_frame, text="Counter: 0")
        self.counter_label.pack()
        self.counter_button = tk.Button(self.my_frame, text="Increment Counter", command=self.controller.increment_counter)
        self.counter_button.pack()

    def update_counter_label(self, counter_value):
        self.counter_label.configure(text="Counter: {}".format(counter_value))
        
        
