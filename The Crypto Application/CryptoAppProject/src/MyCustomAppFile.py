# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:42:26 2023

@author: joaquin
"""
import tkinter as tk
from tkinter import Menu


########################################################################### 
class MyMenuClass(object):
    def __init__(self, parent, curr):
        self.menubar = Menu(parent)
        self.parent = parent
        self.parent.config(menu=self.menubar)
        self.curr = curr
        
        self.test = 101
        
        ### ADD MENU ITEMS
        # create a file_menu from Menu Tkinter
        self.file_menu = Menu(self.menubar)
        self.home_menu = Menu(self.menubar)
        
        # add the File menu to the menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        # add the Home menu to the menubar
        self.menubar.add_cascade(label="Home", menu=self.home_menu)


        ### ADD ITEM DROP-DOWNS
        # add a menu item to file_menu
        self.file_menu.add_command(label='Open', command=None)
        self.file_menu.add_command(label='Save', command=None)
        self.file_menu.add_command(label='Save as', command=None)
        self.file_menu.add_command(label='Exit', command=self.parent.destroy)
        
        self.home_menu.add_command(label='Go Home', command=self.func1 )
        
        
    def func1(self):
        # print(self.root)
        print('go home... ')
        # p1 = PageOne(self.curr)
        # p1.create()
        home_click_counter = 1
        self.curr.root.forget()
        HomePage(self.parent, home_click_counter)



###########################################################################    
class PageThree(object):
    def __init__(self, parent):
        self.root = tk.Frame(parent) 
        self.parent = parent
        print('at page 3tres')
        self.button = tk.Label(self.root, text="Page Three", font=("Arial", 16), fg="grey")
        self.button.pack()
        self.button =  tk.Button(self.root, text="Go to One", command=self.go_to_one_clicked )
        self.button.pack()
        
    def create(self):
        self.root.pack()
        # self.root.tkraise()
        
    def go_to_one_clicked(self):
        print('go to one clicked clicked')
        self.root.forget() 
        # 'self.parent' is the MyMainWindow main window parameter (this comes from prior page)
        p1 = PageOne(self.parent)
        p1.create()

###########################################################################    
class PageTwo(object):
    def __init__(self, parent):
        self.root = tk.Frame(parent) 
        self.parent = parent
        print('at page twooopo')
        self.button = tk.Label(self.root, text="Page Two", font=("Arial", 16), fg="orange")
        self.button.pack()
        self.button =  tk.Button(self.root, text="Go to Three", command=self.go_to_one_clicked )
        self.button.pack()
        
    def create(self):
        self.root.pack()
        # self.root.tkraise()
        
    def go_to_one_clicked(self):
        print('go to one clicked clicked')
        self.root.forget() 
        # 'self.parent' is the MyMainWindow main window parameter (this comes from prior page)
        p1 = PageThree(self.parent)
        p1.create()




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
        
    def create(self):
        self.root.pack()
        # self.root.tkraise()
        
    def go_to_two_clicked(self):
        print('go to two clicked clicked')
        self.root.forget() 
        # 'self.parent' is the MyMainWindow main window parameter (this comes from prior page)
        p2 = PageTwo(self.parent)
        p2.create()
        
        
        
  
########################################################################
class HomePage(object):
    def __init__(self, parent=None, counter = None):
        self.root = tk.Frame(parent) 
        self.parent = parent
        print('at home page')
        
        if counter == None or counter % 2 == 0:
            self.label = tk.Label(self.root, text="we are shoing home", font=("Arial", 16), fg="blue")
            self.label.pack()
        else:
            self.label = tk.Label(self.root, text="home reloded at least once", font=("Arial", 16), fg="pink")
            self.label.pack()
        
        MyMenuClass(self.parent, self)
        
        # Packing matters, make sure to pack before packing pageone
        self.root.pack()
        # self.root.tkraise()
        
        self.frames = {}
        for F in (PageOne, PageTwo, PageThree):
            frame = F(self.root)
            self.frames[F] = frame
        
        self.show_frame(PageOne)
        
    def show_frame(self, go_to_frame):
        curr = self.frames[go_to_frame]
        curr.create()
        # curr.pack()
        
    def create(self):
        print('create: ')
        self.forget()
        self.root.pack()

        
        
        
        

###########################################################################
class NextFrame(object):
    def __init__(self, parent):
        print('AT next frame')
        # self.root = tk.Frame()  # TRY THIS LINE OF CODE TOO
        self.root = tk.Frame(parent) 
        self.parent = parent

        self.create_all_widgets()
        
        self.write_to_file()
            
        
        #display my tk.frame 'root'
        self.root.pack()
        # self.root.tkraise()
        
    def write_to_file(self):
        with open('../data/account_name.txt', 'a') as file2:
            file2.write('entered this line.. \n' )
            file2.close()
        
        
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
        
        # PageOne(self.parent)
        HomePage(self.parent)
        




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
        # self.root.tkraise()
        
        
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