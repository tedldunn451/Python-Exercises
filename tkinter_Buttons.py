# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 17, 2017
# Description: Buttons

from tkinter import *
from tkinter import ttk
root= = Tk()
button = ttk.Button(root, text = "Click Me")
button.pack() # use pack geometry manager to display button with text
def callback():
    print('Clicked!')
button.config(command = callback) # command property is used to pass in function name that contains actions

button.invoke() # simulate command property

button.state(['disabled']) # use this to grey out buttons to make them unclickable
button.instate(['disabled']) # returns true or false depending on if button is disabled or not
button.state(['!disabled']) # use this to re-enable a button
# other button widget states include 'active' and 'focus'

logo = PhotoImage(file = 'filepath')
button.config(image = logo, compound = LEFT) # config image to exist alongside button
small_logo = logo.subsample(5,5) # takes every 5th pixel in the x and y directions to create a smaller image
