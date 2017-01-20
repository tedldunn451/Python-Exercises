#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import * # imports tkinter module (functions and variables used in tkinter)

root = Tk() # create new top-level widget
Label(root, text="Hello, Tkinter!").pack() # child of root window that exists on top of the root window
root.mainloop() # used to display/run widget
