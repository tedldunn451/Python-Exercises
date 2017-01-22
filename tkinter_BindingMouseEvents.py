# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Binding Mouse Events

from tkinter import *
from tkinter import ttk
root = Tk()

canvas = Canvas(root, width = 640, height = 480, background = 'white')
canvas.pack()

# on a mouse, 1 represents left, 2 represents center (scroll wheel), and 3 represents right

'''Mouse events: click-related
<Button>, <ButtonPress> : any button was pressed
<Button-1>, <ButtonPress-1>, <1> : Button 1 pressed
<ButtonRelease-1> : Button 1 released
<Double-Button-1> or <Triple-Button-1> : Button 1 double or triple clicked

Mouse events: movement-related
<Enter> : mouse entered widget area
<Leave> : mouse left widget area
<Motion> : mouse was moved
<B1-Motion> : mouse was moved w/ button one pressed
'''

def mouse_press(event):
    global prev
    prev = event
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num)) # returns mouse button that was pressed
    print('x: {}'.format(event.x)) # returns x coordiante of where mouse was clicked
    print('y: {}'.format(event.y)) # returns y coordinate of where mouse was clicked
    print('x_root: {}'.format(event.x_root)) # returns x coordinate relative to screen
    print('y_root: {}'.format(event.y_root)) # returns y coordinate relative to screen

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev = event
    
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)
    
root.mainloop()

