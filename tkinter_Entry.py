# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 18, 2017
# Description: Entry Widget

from tkinter import *
from tkinter import ttk
root= = Tk()

entry = ttk.Entry(root, width = 30)
entry.pack()
entry.get() # use to return contents of entry field

entry.delete(0, 1) # deletes from index 1 to index 2 (non-inclusive)
entry.delete(0, END) # deletes all from entry field
entry.insert(0, 'Enter your password')
entry.config(show = '*') # take string that's entered and replace with astericks
entry.get() # returns what's been entered even if only astericks are displayed
entry.state(['disabled']) # grays out entry field
entry.state(['readonly']) # users can copy but not enter anything new into the field
