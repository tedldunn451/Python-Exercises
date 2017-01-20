# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Widget Styles

from tkinter import *=
from tkinter import ttk
root = Tk()

'''Widget states:
active
disabled
focus
pressed
selected
background
readonly
alternate
invalid
hover
see http://www.tkdocs.com/widgets/index.html for more detail
'''

button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')
button1.pack()
button2.pack()
style = ttk.Style() # create style object using ttk style constructor method
style.theme_names() # displays available styles
style.theme_use() # displays which theme is currently being used
style.theme_use('classic') # use theme_use method with arguement to change theme
style.theme_use('vista')

# usually widget style names follow the convention of 'T' in front of widget names e.g. TButton (exceptions exist such as Treeview)
button1.winfo_class() # shows style of widget
style.configure('TButton', foreground = 'blue') # changes text to be blue

# you can create custom styles in addition to changing existing styles
style.configure('Alarm.TButton', foreground = 'orange', font = ('Arial', 24, 'bold')) # Alarm is the new style name and TButton is what it is derived from, the rest of the parameters are custumzied properties of the button
button2.config(style = 'Alarm.TButton')
style.map('Alarm.TButton', foreground = [('pressed', 'pink'), ('disabled', 'grey')]) # use map method to configure style settings for different states of the object
button2.state(['disabled'])

# each tk style is composed of one or more elements... to view, use layout method
style.layout('TButton') # returns elements within style
''' there is a hierarchy of 4 elements in the TButton style as follows:
Button element
    Focus element
         Padding element
              Label element
All have sticky set to nswe to stretch to fill the available space in all directions
'''
style.element_options('Button.label') # returns list of options available for that element
style.lookup('TButton', 'foreground') # returns current value of that property
