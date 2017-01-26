# Author: Kristen Findley
# Date: 26 January 2017
# Python: Version 3.5.7
# Description: script that allows a user to browse for and select a folder that the program will scan for files edited in the previous 24 hrs and copy them into a second folder

from tkinter import *
from tkinter import filedialog
import os
import shutil
import datetime
import time

import drill65of68_main
import drill65of68_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit program","Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def select_origin(self):
    global origin_dir
    origin_dir = filedialog.askdirectory()+"/"
    self.entry_origin.insert(0,origin_dir)

def select_destination(self):
    global destination_dir
    destination_dir= filedialog.askdirectory()+"/"
    self.entry_destination.insert(0,destination_dir)

def copy_files(self):
    current_time = time.time()
    folderA = origin_dir
    folderB = destination_dir
    original_dest_files = len(os.listdir(folderB))
    for i in os.listdir(folderA):
        time_file = os.path.getmtime(folderA+i)
        if current_time - 86400 <= time_file:
            shutil.copy(folderA+i,folderB)
    final_dest_files = len(os.listdir(folderB))
    files_copied = final_dest_files - original_dest_files
    if files_copied > 0:
        messagebox.showinfo("Files copied","All recently modified files were successfully copied.")
    elif files_copied == 0:
        messagebox.showinfo("Files not copied","There were no recently modified files.")
    

