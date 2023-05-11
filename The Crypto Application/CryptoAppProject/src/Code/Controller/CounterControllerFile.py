# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:43:01 2023

@author: joaquin
"""

from Code.Model.CounterModelFile import CounterModel
from Code.View.CounterViewFile import CounterView

class CounterController(object):
        def __init__(self, root):
            self.model = CounterModel()
            self.view = CounterView(root, self)

        def increment_counter(self):
            self.model.increment_counter()
            self.view.update_counter_label(self.model.counter)
