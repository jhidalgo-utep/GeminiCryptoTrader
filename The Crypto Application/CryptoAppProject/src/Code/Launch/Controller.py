# -*- coding: utf-8 -*-
"""
Created on Wed May 10 00:22:11 2023

@author: joaqu
"""
from Code.Launch.Model import Model
from Code.Launch.View1 import View1
from Code.Launch.View2 import View2
from Code.Launch.View3 import View3

class Controller:
    # # For ONLY 2 Views - Method 1
    # def __init__(self, parent):
    #     self.model = Model()
    #     self.parent = parent
    #     self.view1 = View1(parent, self)
    #     self.view2 = View2(parent, self)
        
    #     self.show_view2()
        

    # def show_view1(self):
    #     self.view2.pack_forget()
    #     self.view1.update_label(self.model.message)
    #     self.view1.pack()

    # def show_view2(self):
    #     self.view1.pack_forget()
    #     self.view2.pack()
###################################################
    # # # Method 2
    # def __init__(self, parent):
    #     self.model = Model()
    #     self.parent = parent
    #     self.view1 = View1(parent, self)
    #     self.view2 = View2(parent, self)
    #     self.view3 = View3(parent, self)
    #     self.show_view1()

    # def show_view1(self):
    #     self.view2.pack_forget()
    #     self.view3.pack_forget()
    #     self.view1.update_label(self.model.message)
    #     self.view1.pack()

    # def show_view2(self):
    #     self.view1.pack_forget()
    #     self.view3.pack_forget()
    #     self.view2.update_label("This is View 2")
    #     self.view2.pack()

    # def show_view3(self):
    #     self.view1.pack_forget()
    #     self.view2.pack_forget()
    #     self.view3.update_label("This is View 3")
    #     self.view3.pack()
###################################################
    def __init__(self, parent):
        self.parent = parent
        self.model = Model()
        self.views = []
        self.current_view = None
        self.create_views()
        self.show_view1()

    def create_views(self):
        view1 = View1(self.parent, self)
        view2 = View2(self.parent, self)
        view3 = View3(self.parent, self)
        self.views.append(view1)
        self.views.append(view2)
        self.views.append(view3)

    def show_view1(self):
        self.show_view(0)

    def show_view2(self):
        self.show_view(1)

    def show_view3(self):
        self.show_view(2)

    def show_view(self, index):
        if self.current_view:
            self.current_view.pack_forget()
        self.current_view = self.views[index]
        self.current_view.pack()
        