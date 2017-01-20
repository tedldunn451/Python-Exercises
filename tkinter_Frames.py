# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 19, 2017
# Description: Frames

from tkinter import *
from tkinter import ttk
root= = Tk()

# frames are subdivisions of the parent that can act as a parents themselves and geometry managers to hold and organize other widgets
# allows each frame to have unique geometry management best suited for the widget within

frame = ttk.Frame(root)
frame.pack() # default height and width of 0 unless widget is contianed within at which time it autosizes
frame.config(height = 100, width = 200) # size in pixels

# 'frame relief' used to customize look of border including FLAT, RAISED, SUNKEN, SOLID, RIDGE, or GROOVE
frame.config(relief = RIDGE)
ttk.Button(frame, text = 'Click Me').grid() # use frame instead of root and grid instead of pack
frame.config(padding = (30, 150)) # configures padding using pixels in x and y directions
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack() # use pack when child of root and grid when child of frame


