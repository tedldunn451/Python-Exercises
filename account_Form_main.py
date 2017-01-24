# Author: Kristen Findley
# Date: 22 January 2017
# Python: Version 3.5.2
# Description: Account Information Form - the purpose of this form is to provide a way to organize, edit, display, and retrieve information about the various accounts

from tkinter import *
import tkinter as tk # creates shortcut to reference tkinter as tk in subseqent code

# import other modules to enable interaction
import account_Form_func
import account_Form_gui

class ParentWindow(Frame): # tkinter 'Frame' inherited into 'ParentWindow' class
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        # define master frame config
        self.master = master # self refers to ParentWindow class and master refers to Frame
        self.master.title('Account Form') # title of form window
        self.master.configure(background = '#f0f0f0') # sets background color
        arg = self.master

        # load gui from separate module to keep code clean
        account_Form_gui.load_gui(self)

if __name__ == "__main__": # syntax required by Tkinter to create window and pass to ParentWindow
    root = tk.Tk() # creates window
    App = ParentWindow(root) # attach root to ParentWindow
    root.mainloop() # loops to remain on screen until closed or cancelled
    
