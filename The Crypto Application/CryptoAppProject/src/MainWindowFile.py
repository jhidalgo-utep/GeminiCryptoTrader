# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:42:26 2023

@author: joaquin
"""

import tkinter as tk



class NextFrame(object):
    def __init__(self, parent):
        print('AT next frame')
        # self.root = tk.Frame()  # TRY THIS LINE OF CODE TOO
        self.root = tk.Frame(parent) 
        self.parent = parent
        
        self.create_all_widgets()
        
        #display my tk.frame 'root'
        self.root.pack()
        
        

    def create_all_widgets(self):
        self.next_frame_label_widget()
        self.next_frame_button_widget()
        
    def next_frame_label_widget(self):
        self.button = tk.Label(self.root, text="Start Developing application here", font=("Arial", 16), fg="green")
        self.button.pack()
        
    
    def next_frame_button_widget(self):
        self.button =  tk.Button(self.root, text="NEXT", command=None )
        self.button.pack()
        
    


class MainFrame(object):
    def __init__(self, parent):
        # self.root is the current frame (i think?) && to create a new frame you need the parent frame or window frame
        self.root = tk.Frame(parent)
        self.parent = parent
        print('created main frame - 1 button')
        
        
        self.create_all_widgets()
        
        #display my tk.frame 'root'
        self.root.pack()
        
    def create_all_widgets(self):
        self.welcome_button_widget()
    
    def welcome_button_widget(self):
        self.button = tk.Button(self.root, text="ENTER", command=self.segue_frame )
        self.button.pack()
        
    def button_cliked_message(self):
        print('Enter Clicked. Go to Next Frame')
        
        
    
    def segue_frame(self):
        self.root.forget() #IF i dont do this, EVEY TIME I CLICK BUTTON, I ADD A LABEL TO THE Current FRAME
        
        # 'self.parent' is the MyMainWindow main window parameter (this comes from prior page)
        self.next_frame = NextFrame(self.parent)
        
        

class MyMainWindow(object):
    # Init Controller #8 Obj as 'self.root'
    def __init__(self):
        self.root = tk.Tk() # create main window
        self.root.title('The Crypto Application')
        
        # Once main window was created, i am going to show a frame called 'main_frame' and when you create tk.Frame, you need to pass the root widget  
        self.main_frame = MainFrame(self.root)  #The main frame 'MainFrame' is aggregated to the main window 'self.root'
        

    def start_main_loop(self):
        self.root.mainloop()
        
    def is_main_window(self):
        return self.is_main_window


class MainWindow(object):
    def __init__ (self):
        self.custom_main = True
        
    def start(self):
        
        my_app = MyMainWindow()
        my_app.start_main_loop()
        
        print('GOOD-BYE')
        #END
        
        
