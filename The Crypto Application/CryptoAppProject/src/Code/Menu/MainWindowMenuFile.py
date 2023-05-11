# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:26:36 2023

@author: joaquin
"""

from tkinter import Menu

class MainWindowMenu(object):
    def __init__(self, root):
        # self.root = root
    
        # create menubar from Menu Tkinter
        menubar = Menu(root)
        root.config(menu=menubar)
        
        
        ### ADD MENU ITEMS
        # create a file_menu from Menu Tkinter
        file_menu = Menu(menubar)
        # add the File menu to the menubar
        menubar.add_cascade(label="File", menu=file_menu)
        
        # add the Edit menu to the menubar
        edit_menu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        # add the Search menu to the menubar
        search_menu = Menu(menubar)
        menubar.add_cascade(label="Search", menu=file_menu)
        
        # add the Option menu to the menubar
        option_menu = Menu(menubar)
        menubar.add_cascade(label="Option", menu=option_menu)
        
        
        ### ADD ITEM DROP-DOWNS
        # add a menu item to file_menu
        file_menu.add_command(label='Open', command=None)
        file_menu.add_command(label='Save', command=None)
        file_menu.add_command(label='Save as', command=None)
        file_menu.add_command(label='Exit', command=root.destroy)
        
        edit_menu.add_command(label='Undo', command=None)
        
        option_menu.add_command(label='Settings', command=None)
        
