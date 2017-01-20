# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 19, 2017
# Description: Top-level Windows

from tkinter import * # no need to import ttk 
root= = Tk()
window = Toplevel(root) # appears as a separate window, but is still a slave to the original tk window
window.title('New Window')

window.lower() # sends to bottom of stack of windows # use lift to bring it to the front
window.lift(root)

window.state('zoomed') # expands window to max allowed size
window.state('withdrawn') # hides window from user
window.state('iconic')
window.state('normal') # returns window to state it was in before it was withdrawn or iconicized, in this example zoomed
window.state('normal') # when called a second time, it returns it to the original size
window.state() # with no argument returns the current state of the window
window.iconify() # sends window down so that it is visible in the task bar (appears to be the same as minimized)
window.deiconify() # reopens window

window.geometry('640x480+50x100') # width, height, and position in pixels relative to top left corner of the screen 
# user can clicked and drag to resize window by default
window.resizable(False,False) # used to prevent resizing
window.maxsize(640, 480)
window.minsize(200, 200)
window.resizable(True,True) # can resize, but only within constraints specified

# destroy methods will destroy window + all children
root.destroy() # destroys all




