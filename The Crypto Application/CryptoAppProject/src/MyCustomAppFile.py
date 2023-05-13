# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:42:26 2023

@author: joaquin
"""
import tkinter as tk

###########################################################################    
class PageTwo(object):
    def __init__(self, parent):
        self.root = tk.Frame(parent) 
        self.parent = parent
        print('at page twooopo')
        self.button = tk.Label(self.root, text="Page Two", font=("Arial", 16), fg="orange")
        self.button.pack()
        self.button =  tk.Button(self.root, text="Go to One", command=self.go_to_one_clicked )
        self.button.pack()
        self.root.pack()
        self.root.tkraise()
        
    def go_to_one_clicked(self):
        print('go to one clicked clicked')
        self.root.forget() 
        # 'self.parent' is the MyMainWindow main window parameter (this comes from prior page)
        PageOne(self.parent)





###########################################################################
class PageOne(object):
    def __init__(self, parent):
        self.root = tk.Frame(parent) 
        self.parent = parent
        print('at page oneee')
        self.button = tk.Label(self.root, text="Page One", font=("Arial", 16), fg="red")
        self.button.pack()
        self.button =  tk.Button(self.root, text="Go to Two", command=self.go_to_two_clicked )
        self.button.pack()
        self.root.pack()
        self.root.tkraise()
        
    def go_to_two_clicked(self):
        print('go to two clicked clicked')
        self.root.forget() 
        # 'self.parent' is the MyMainWindow main window parameter (this comes from prior page)
        PageTwo(self.parent)
        
        



        
###########################################################################
class NextFrame(object):
    def __init__(self, parent):
        print('AT next frame')
        # self.root = tk.Frame()  # TRY THIS LINE OF CODE TOO
        self.root = tk.Frame(parent) 
        self.parent = parent

        self.create_all_widgets()
        
        #display my tk.frame 'root'
        self.root.pack()
        self.root.tkraise()
        
    def create_all_widgets(self):
        self.next_frame_label_widget()
        self.next_frame_button_widget()
        
    def next_frame_label_widget(self):
        self.button = tk.Label(self.root, text="Start Developing application here", font=("Arial", 16), fg="green")
        self.button.pack()
    
    def next_frame_button_widget(self):
        self.button =  tk.Button(self.root, text="NEXT", command=self.next_clicked )
        self.button.pack()
        
    def next_clicked(self):
        print('next clicked')
        self.root.forget() 
        # 'self.parent' is the MyMainWindow main window parameter (this comes from prior page)
        PageOne(self.parent)
        




###########################################################################
class MainFrame(object):
    def __init__(self, parent):
        # self.root is the current frame (i think?) && to create a new frame you need the parent frame or window frame
        self.root = tk.Frame(parent)
        self.parent = parent
        print('created main frame - 1 button')
        self.create_all_widgets()
        
        #display my tk.frame 'root'
        self.root.pack()
        self.root.tkraise()
        
        
    def create_all_widgets(self):
        self.welcome_button_widget()
    
    def welcome_button_widget(self):
        self.button = tk.Button(self.root, text="ENTER", command=self.segue_frame )
        self.button.pack()
        
    def button_cliked_message(self):
        print('Enter Clicked. Go to Next Frame')
    
        
    def segue_frame(self):
        self.root.forget() 
        # 'self.parent' is the MyMainWindow main window parameter (this comes from prior page)
        NextFrame(self.parent)
        
        



###########################################################################
class MyMainWindow(object):
    # Init Controller #8 Obj as 'self.root'
    def __init__(self):
        
        self.root = tk.Tk() # create main window
        self.root.title('The Crypto Application')
        
        # Once main window was created, i am going to show a frame called 'main_frame' and when you create tk.Frame, you need to pass the root widget  
        MainFrame(self.root)  #The main frame 'MainFrame' is aggregated to the main window 'self.root'
        
    def start_main_loop(self):
        self.root.mainloop()
        
    def is_main_window(self):
        return self.is_main_window






###########################################################################
class MyCustomApplication(object):
    def __init__ (self):
        self.custom_main = True
        
    def start(self):
        main_window = MyMainWindow()
        main_window.start_main_loop()
        
        print('GOOD-BYE')
        #END