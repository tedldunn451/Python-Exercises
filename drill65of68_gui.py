# Author: Kristen Findley
# Date: 26 January 2017
# Python: Version 3.5.7
# Description: script that allows a user to browse for and select a folder that the program will scan for files edited in the previous 24 hrs and copy them into a second folder

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

import drill65of68_main
import drill65of68_func

def load_gui(self):
    self.frame_header = ttk.Frame(self.master)
    self.frame_header.pack()
    
    self.lbl_introhead = ttk.Label(self.frame_header,text = "Welcome to CopyCat")
    self.lbl_introhead.grid(row = 0,column = 0,columnspan = 4,padx = 5,pady = 10,sticky='w')
    self.lbl_intro = ttk.Label(self.frame_header,wrap=510,text = "This application is used to copy files modified within the last 24 hours from an 'origin folder' to a 'destination folder'. Please browse to inside of the respective 'origin' and 'destination' folders of choice.")
    self.lbl_intro.grid(row = 1,column = 0,padx = 5,pady = (0,15),sticky = 'w')


    self.frame_main = ttk.Frame(self.master)
    self.frame_main.pack()
    
    self.lbl_origin = ttk.Label(self.frame_main,text = "Origin Folder: ")
    self.lbl_origin.grid(row = 1,column = 0,padx = (15,10),sticky = 'w')
    self.entry_origin = ttk.Entry(self.frame_main,text = "",width = 50)
    self.entry_origin.grid(row = 2,column = 0,columnspan = 2,padx = (15,10),pady = (0,10))
    self.lbl_destination = ttk.Label(self.frame_main,text = "Destination Folder: ")
    self.lbl_destination.grid(row = 4,column = 0,padx = (15,10),sticky = 'w')
    self.entry_destination = ttk.Entry(self.frame_main,text = "",width = 50)
    self.entry_destination.grid(row = 5,column = 0,columnspan = 2,padx = (15,10),pady = (0,10))

    self.btn_browse1 = tk.Button(self.frame_main,width = 10,height = 2,text = "Browse",command = lambda: drill65of68_func.select_origin(self))
    self.btn_browse1.grid(row = 2,column = 3,padx = (10,15))
    self.btn_browse2 = tk.Button(self.frame_main,width = 10,height = 2,text = "Browse",command = lambda: drill65of68_func.select_destination(self))
    self.btn_browse2.grid(row = 5,column = 3,padx = (10,15),pady = (0,15))

    self.btn_copy = tk.Button(self.frame_main,width = 10,height = 2,text = "Copy Files",command = lambda: drill65of68_func.copy_files(self))
    self.btn_copy.grid(row = 7,column = 0,padx = 10,pady = (0,15))
    self.btn_cancel = tk.Button(self.frame_main,width = 10,height = 2,text = "Cancel",command = lambda: drill65of68_func.ask_quit(self))
    self.btn_cancel.grid(row = 7,column = 1,padx = 10,pady = (0,15))

if __name__ == "__main__":
    pass
