# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Binding Keyboard Events

from tkinter import *
from tkinter import ttk
root = Tk()

# tkinter can bind to events with specific handlers

'''Tk event types
ButtonPress
ButtonRelease
Enter
Leave
Motion
KeyPress
KeyRelease
FocusIn
FocusOut
more detail at http://www.tkdocs.com/tutorial/canvas.html#bindings
'''

def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}'.format(event.keycode))

def shortcut(action):
    print(action)
    
root.bind('<KeyPress>', key_press)
root.bind('<Control-c>', lambda: shortcut('Copy')) # error occurs because the event handler is trying to pass object with even info as arguement to lambda function though lambda is expecting any arguements... fix as shown below
root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.mainloop()

'''Keyboard Events
<Key> or <KeyPress> : user pressed ANY key
<KeyPress-Delete> : user pressed Delete key
<KeyRelease-Right> : user released right arrow key
a, b, c, 1, 2, 3... (except <space> and <less>) : user pressed a 'printable' key
<Shift_L>, <Control_R>, <F5>, <Up> : user pressed a 'special' key 
<Return> : user pressed enter key
<Control-Alt-Next> : user pressed Ctrl+Alt+Page Down keys
'''

