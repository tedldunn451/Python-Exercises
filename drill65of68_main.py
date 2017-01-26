# Author: Kristen Findley
# Date: 26 January 2017
# Python: Version 3.5.7
# Description: script that allows a user to browse for and select a folder that the program will scan for files edited in the previous 24 hrs and copy them into a second folder

from tkinter import *
from tkinter import filedialog

import drill65of68_func
import drill65of68_gui

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master 
        self.master.title("CopyCat") 
        arg = self.master

        drill65of68_gui.load_gui(self)

if __name__ == "__main__":
    root = Tk() 
    App = ParentWindow(root) 
    root.mainloop() 

            
