# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 18, 2017
# Description: Scale/Progress Widgets

from tkinter import *
from tkinter import ttk
root= = Tk()

progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()

# 2 modes of determinate and indeterminate... use determinate for known number of steps
progressbar.config(mode = 'indeterminate')
progressbar.start() # use start to turn on progress bar
progressbar.stop() # use when operation is completed

progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2) # default max is 100
progressbar.config(value = 8.0)
progressbar.step() # use to step up value of progressbar
progressbar.step(5) # increments value by 5 and wraps around if 100% is exceeded

# scale
value = DoubleVar() 
progressbar.config(variable = value)
scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)
scale.pack() # when scale is changed by the user, the progress bar automatically updates accordingly
scale.set(4.2)
scale.get()
# might be useful to include a label above or below to reflect scale values to user

