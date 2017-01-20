# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 19, 2017
# Description: Cascading Menus

from tkinter import *

root = Tk()
root.option_add('*tearOff', False) # tells tk menu to not create a tearable menu

menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu = file, label = "File")
menubar.add_cascade(menu = edit, label = "Edit")
menubar.add_cascade(menu = help_, label = "Help")

file.add_command(label = 'New', command = labmda: print('New File'))
file.add_separator() # inserts line under first command of file menu
file.add_command(label = 'Open...', command = labmda: print('Opening File...'))
file.add_command(label = 'Save', command = lambda: print('Save File'))

file.entryconfig('New', accelerator = 'Ctrl + N') # dispalys shortcut, but does not actually provide the shortcut functionality

logo = PhotoImage(file = 'filepath').subsample(10, 10)
file.entryconfig('Open...', image = logo, compound = 'left') # sets python logo next to 'open' option on file menu
file.entryconfig('Open...', state = 'disabled')

# submenus
file.delete('Save')
save = Menu(file)
file.add_cascade(menu = save, label = "Save")
save.add_command(label = 'Save As', command = lambda: print('Saving As...'))
save.add_command(label = 'Save All', command = lambda: print('Saving All...'))

# radio buttons in menus (you can use the same technique to add check buttons)
choice = IntVar()
edit.add_radiobutton(label = 'One', variable = choice, value = 1) # will assign a value of 1 if selected
edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
edit.add_radiobutton(label = 'Three', variable = choice, value = 3)

file.post(400,300) # use to create a pop-up menu at 400 x and 300 y pixels (with relation to the entire screen, not the tk window)

