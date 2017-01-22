# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Place Geometry Manager

from tkinter import *
from tkinter import ttk
root = Tk()

# locates widgets relative to parent as opposed to other widgets (as is the case with pack and grid geometry managers)

root.geometry('640x480+200+200') # 640 x 480 pixels at coordinates (200,200) relative to top left corner of screen 

label1 = ttk.Label(root, text = "Yellow", background = 'yellow')
label1.place(x = 100, y = 50, width = 100, height = 50) # width and height are in pixels
label2 = ttk.Label(root, text = "Blue", background = 'blue')
label2.place(relx = .5, rely = .5. anchor = 'center', relwidth = 0.5, relheight = 0.5) # relx/rely and relwidth/relheight= % of parent window, default anchor is 'nw'
label3 = ttk.Label(root, text = "Green", background = 'green')
label3.place(relx = 0.5, x = 100, rely = 0.5, y = 50) # finds rel location first and then moves additional specified pixels in x and y direction
label4 = ttk.Label(root, text = "Orange", background = 'orange')
label4.place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

'''other grid methods:
place_slaves()
place_configure()
place_info()
place_forget()
'''

root.mainloop()
