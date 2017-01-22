# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Binding Virtual Events

from tkinter import *
from tkinter import ttk
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy')) # prints Copy when ctrl+c is pressed
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>')) # prints info about virtual event OddNumber

entry.event_generate('<<OddNumber>>') # triggers OddNumber event
entry.event_generate('<<Paste>>')

entry.event_delete('<<OddNumber>>') # deletes virtual event OddNumber

root.mainloop()
