# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:44:07 2023

@author: joaquin
"""

from Code.Model.NameModelFile import NameModel
from Code.View.NameViewFile import NameView

class NameController(object):
    def __init__(self, root):
        self.model = NameModel()
        self.view = NameView(root, self)

    def set_name(self, name):
        self.model.set_name(name)
        self.view.update_name_label(self.model.name)