# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 17, 2017
# Description: Buttons

from tkinter import *
from tkinter import ttk
root= = Tk()

# radio button (one selection from a series) and check button (binary choice)
checkbutton = kkt.Checkbutton(root, text = 'SPAM')
checkbutton.pack()

# you can use all same configs demonstrated in the tkinter_Buttons.py file

''' tkinter variable classes to used enable tracking changes to variables include:
1) BooleanVar
2) DoubleVar
3) IntVar
4) StringVar
'''

# check button example
spam = StringVar()
spam.set('SPAM!')
spam.get() # returns string stored within variable
checkbutton.config(variable = spam, onvalue = 'SPAM Please', offvalue = 'Boo SPAM') # by default, check button assumes value of 1 when selected and 0 when not selected, but since this doesn't make sense for a string variable, you can reset them using onvalue and offvalue

# radio button example
breakfast = StringVar()
ttk.Radiobutton(root, text = 'Spam', variable = breakfast, value = 'Spam').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast, value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Oatmeal', variable = breakfast, value = 'Oatmeal').pack()
