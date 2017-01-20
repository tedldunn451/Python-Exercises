# Author: Kristen Findley
# Version: Python 3.5.2
# Date: 16 January 2017
# Description: tkinter tutorial

import tkinter # imports tkinter module
import _tkinter # imports compiled binary associated w/ tkinter package
tkinter._test() # use to test tkinter and show you which version of tck/tk is on your comp

from tkinter import * # imports everything
from tkinter import ttk # imports themed tkinter from separate module

root = Tk() # create root window
button = ttk.Button(root, text = 'Click Me') # creates themed button, but doesn't add to window
button.pack() # packs button in root window
button['text'] # use to view text property of button
button['text'] = 'Press Me' # use to change property of button
button.config(text = 'Push Me') # other way to modify property
button.config() # returns all properties of button in the form of tuples

ttk.Label(root, text = 'Hello, Tkinter!').pack() # creates label with text property under root window and immediately packs it


