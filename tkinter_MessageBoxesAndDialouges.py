# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Messageboxes / Dialogs

from tkinter import messagebox # don't need entire tkinter module
messagebox.showinfo('A Friendly Message', message = 'Hello, Tkinter!') # automatically creates root window in background
# creates modal which means that execution of program is paused until action is taken to address messagebox

''' 3 variations of message box
showinfo()
showwarning()
showerror()
'''

messagebox.askyesno(title = "Hungry?", message = "Do you want SPAM?") # returns True if yes, and False if no

''' variations of question messagebox
askyesno()
askokcancel()
askretrycancel()
askyesnocancel() # true if yes, false if no or cancel
askquestion()
'''
from tkinter import filedialog
filename = filedialog.askopenfile() # returns IO object w/ filepath
filename.name() # displays filepath

''' filedialog types 
askdirectory()
asksaveasfile(mode)
asksaveasfilename()

askopenfile(mode)
askopenfiles(mode)
askopenfilename()
askopenfilenames()

*these filedialogs do not acutally open or save anything, then just return information to program about file or directory user selected
'''

from tkinter import colorchooser
colorchooser.askcolor(initialcolor = '#FFFFFF') # color chooser return RGB and hex representations of color selected (returned values will be empty if user hits cancel instead of choosing a color)

