# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 18, 2017
# Description: Combobox and Spinbox Widgets

from tkinter import *
from tkinter import ttk
root= = Tk()

# combo box is displayed as a dropdown menu
# spin box shows only one option at a time and you can scroll up and down the options

# combobox example
month = StringVar() # create variable to store selection of combo box
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = 'January', 'February', 'March', 'April', 'May', 'June')
month.get() # to see what month has been selected
month.set() # if you set month to an option that isn't a configured value on the list, then the user can type whatever they want into the box and it will be set as the month

# spinbox example
year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack() # no ttk option for this widget... from_ must have an underscore since 'from' is a keyword in Python
year.get() # same as above
year.set() # same as above
