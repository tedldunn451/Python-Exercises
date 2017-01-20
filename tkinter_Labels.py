# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 16, 2017
# Description: Labels

from tkinter import *
from tkinter import ttk
root = Tk()
label = ttk.Label(root, text = "Hello, Tkinter!") # Use label constructor method to create label with root as parent and text property
label.pack() # Use pack geometry method to display label
label.config(text = "Howdy, Tkinter.") # use config to change property of label
label.config(wraplength = 150) # use to control width of root window
label.config(justify = CENTER) # use to justify center
label.config(forground = 'blue', background = 'yellow') # config background
label.config(font = ('Courier', 18, 'bold')) # configure font

logo = PhotoImage(file = 'filepath') # use to dispaly image in window.. make sure you store image to variable that will not be garbage collected!
label.config(image = logo)

label.config(compound = 'text') # use compound to change window content back to text
label.config(compound = 'center') # centers the text atop the image... you can also use left or right to locate the text relative to the image

# use these two lines of code to store reference to image object in tkinter label object avoid image being garbage collected
label.img = logo 
label.config(image = label.img) # since photo image is now stored within the label, it will exist as long as the label does
