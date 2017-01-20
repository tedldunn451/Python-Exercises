# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 19, 2017
# Description: Paned Windows

from tkinter import *
from tkinter import ttk
root= = Tk()

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill, BOTH, expand = True) # expand = fill if window size is changed

frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)

pandedwindow.add(frame1, weight = 1) # weight property specifies how much the frame will be scaled when pane window is resized
pandedwindow.add(frame2, weight = 4) # thus frame 2 expands 4 times more than frame 1

frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)
panedwindow.insert(1, frame3) # paramenter 1 is index, so 1 is between the 0th and 1st frames.. parameter 2 is the name of the frame

panedwindow.forget(1) # use to remove the frame existing at position 1

