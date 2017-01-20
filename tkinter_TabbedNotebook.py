# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 19, 2017
# Description: Tabbed Notebook

from tkinter import *
from tkinter import ttk
root= = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two') # add methods adds to the right of the previously added tab

# you can add widgets other than frames

ttk.Button(frame1, text = 'Click Me').pack() # frame 2 expanded to fill frame 1's contents

frame3 = ttk.Frame(notebook)
notebook.insert(1,frame3, text = 'Three') # should be tab one, tab three, tab 2
notebook.forget(1) # removes tab from position passed into the method
notebook.add(frame3, text = 'Three') # added at the end since the add method was used

notebook.select() # returns ID of the widget
notebook.index(notebook.select()) # the index of whichever tab is selected will be returned
notebook.select(2) # selects the tab at the index listed (tab three in this example)

notebook.tab(1, state = 'disabled') # grays out the tab at the first index
notebook.tab(1, state = 'hidden') # hides tab at index 1
notebook.tab(1, state = 'normal') # returns to normal state
notebook.tab(1, 'text') # returns property of tab at index one
notebook.tab(1) # returns all properties of tab at index one



