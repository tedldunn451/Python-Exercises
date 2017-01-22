# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Binding Multiple Events

from tkinter import *
from tkinter import ttk
root = Tk()

label1 = ttk.Label(root, text = 'Label 1')
label2 = ttk.Label(root, text = 'Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label'))
label1.bind('<1>', lambda e: print('<1> Label')) # when left click <1> Label prints, but right click <PressButton> Label prints

root.bind('<1>', lambda e: print('<1> Root')) # when Label 2 is clicked, triggers print <1> Root, but when Label 1 is clicked triggers both print <1> Root AND <1> Label

# unbinding events
label1.unbind('<1>') 
label1.unbind('<ButtonPress>')

# bind all method used to bind event to all widgets
root.bind_all('<Escape>', lambda e: print('Escape!'))

root.mainloop()
