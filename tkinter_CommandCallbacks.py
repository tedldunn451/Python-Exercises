# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Command Callbacks

from tkinter import *
from tkinter import ttk
root = Tk()

def callback(number):
    print(number)
    
ttk.Button(root, text = "Click Me 1", command = callback(1)).pack() # rather than passing the name callback to the command property, it is executing the callback and returning the value to the commant property... to fix, use lambda as shown below
ttk.Button(root, text = "Click Me 2", command = lambda: callback(2)).pack()
ttk.Button(root, text = "Click Me 3", command = lambda: callback(3)).pack()

root.mainloop()

'''other widgets with command callbacks include:
Button
Checkbutton
Radiobutton
Spinbox
Scale
Scrollbar
'''


