# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Grid Geometry Manager

from tkinter import *
from tkinter import ttk
root = Tk()

# used to organize in 2 dimensional layouts
# used with modern GUI layouts

root.rowconfigure(0, weight = 1) # params: index, weight
root.rowconfigure(1, weight = 3)
# row 1 expands at 3 times the rate row 0 expands

root.columnconfigure(0, weight = 1)

# rows and columns are indexed beginning with 0
yellowlabel = ttk.Label(root, text = "Yellow", background = 'yellow')
yellowlabel.grid(row = 0, column = 2, rowspan = 2, stick = 'nsew') # use param 3 to span 2 rows and param 4 to stretch the label to fill its cell size
bluelabel = ttk.Label(root, text = "Blue", background = 'blue')
bluelabel.grid(row = 1, column = 0, columnspan = 2, stick = 'e') # use param 3 to span 2 columns and param 4 to anchor
greenlabel = ttk.Label(root, text = "Green", background = 'green')
greenlabel.grid(row = 0, column = 0,stick = 'nsew', padx = 10, pady = 10) # adds 10 px padding to the outside of the label (or ipad to add internal padding)
orangelabel = ttk.Label(root, text = "Orange", background = 'orange')
orangelabel.grid(row = 0, column = 1, stick = 'nsew')

'''other grid method (see tkinter_PackGeometryManager for examples)
grid_slave()
grid_configure()
grid_info()
grid_forget()
'''

root.mainloop()
