# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Pack Geometry Manager

from tkinter import *
from tkinter import ttk
root = Tk()

# 3 types of geometry managers: pack() grid() place()... pack() is easiest to use
''' benefits of pack()
simplest
widget expands to fill its parent
easily stacks multiple widgets vertically or horizontally
'''

label1 = ttk.Label(root, text = "Hello, Tkinter!", background = 'yellow')
label1.pack(fill = BOTH, expand = True) # pack automatically places at top and centers (padding added as window resizes)... fill property can be configured i.e. fill = BOTH fills in the x and y directions (other options are X or Y)
label2 = ttk.Label(root, text = "Hello, Tkinter!", background = 'blue')
label2.pack(fill = BOTH)
label3 = ttk.Label(root, text = "Hello, Tkinter!", background = 'green')
label3.pack(fill = BOTH, expand = True)

# pack(side = LEFT) packs all widgets in order to the left
# pack(anchor = 'nw') causes label to anchor to nw corner of the box
# pack(padx = 10, pady = 10) pads the labels with 10 pixels on the outside of the label
# pack(ipadx = 10, ipady = 10) pad the labels with 10 pixels on the inside of the label

for widget in root.pack_slave(): # returns list of all labels managed by the pack manager
    widget.pack_configure(fill = BOTH, exapnd = True)
    print(widget.pack_info()) # returns dictionary of properties that exist for each widget

label1.pack_forget() # label 1 is not deleted, but does not display
    
root.mainloop()
