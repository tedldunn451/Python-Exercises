# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Scroll Bars

from tkinter import *=
from tkinter import ttk
root = Tk()

text = Text(root, width = 40, height = 10, wrap = 'word')
text.grid(row = 0, column = 0)
scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview) # root, not text used as parents because master (not slave text) will handle geometry management of scrollbar... also yview method tells  how far scrollbar has been moved so view changes accordingly
scrollbar.grid(row = 0, column = 1, sticky = 'ns') # column 1 places just to right of text widget, and sticky is 'ns' north/south to be streched vertically within cell

# must configure text widget to tell scrollbar where it is within the text
text.config(yscrollcommand = scrollbar.set) # tells scrollbar %-wise where to place scrollpad

'''scroll-enabled widgets
x-scroll: text, canvas, treeview, entry, spinbox, combobox
y-scroll: text, canvas, treeview
'''

# example
canvas = Canvas(root, scrollregion = (0,0,640,480), bg = 'white')
xscroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = canvas.xview)
yscroll = ttk.Scrollbar(root, orient = VERTICAL, command = canvas.yview)
canvas.config(xscrollcommand = xscroll.set, yscrollcommand  = yscroll.set)

canvas.grid(row = 1, column = 0)
xscroll.grid(row = 2, column = 0, sticky = 'ew')
yscroll.grid(row = 1, column = 1, sticky = 'ns')

def canvas_click(event):
    x = canvas.canvasx(event.x) # canvas.canvasx() communicates the new x location if the canvas has been scrolled in the x-direction
    y = canvas.canvasy(event.y) # canvas.canvasy() communicates the new y location if the canvas has been scrolled in the y-direction
    canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

canvas.bind('<1>', canvas_click)
root.mainloop()
