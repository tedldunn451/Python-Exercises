# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 19, 2017
# Description: Treeview

from tkinter import *
from tkinter import ttk
root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('', '0', 'item1', text = 'First Item') # first param = root (empty strings works as default root), second = index, third = name, fourth = properties
treeview.insert('', '1', 'item2', text = 'Second Item')
treeview.insert('', 'end', 'item3', text = 'Third Item')

logo = PhotoImage(file = 'filepath').subsample(10,10)
treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)

treeview.config(height = 5) # number of entries you want to display
treeview.move('item2','item1','end') # parameters = (element, new parent, index wihtin new parent) **you cannot move an item to be under one of its own children

treeview.item('item1', open = True) # use to cause the item to automatically open (default is closed)
treeview.item('item1', 'open') # should return 1 indicating that the parameters are true

treeview.detach('item3') # detatches item from treeview
treeview.move('item3', 'item2', '0') # reinserts third item into second item
treeview.delete('item3') # deletes completely and cannot be readded...

treeview.config(columns = ('version')) # added a second column
treeview.column('version', width = 50, anchor = 'center') # use to configure column properties

treeview.column('#0', width = 150) # configures main treeview
treeview.heading('version', text = 'Version')
treeveiw.set('python', 'version', '3.4.1') # use to display version 3.4.1 corresponding to Python within the main tree
treeview.item('python', tags = ('software'))
treeview.tag_configure('software', background = 'yellow')

def callback(event):
    print(treeview.selection())

treeview.bind('<<TreeviewSelect>>', callback) # you can use the ctrl key to select multiple items and return them
treeview.config(selectmode = 'browse') # allows only one item to be selected at a time
treeview.config(selectmode = 'none')
treeview.selection_add('python') # programmatically selects items in addition to whichever one the use selects
treeveiw.selection_remove('python') # programmatically unselects and item
treeview.selection_toggle('python') # toggles to select or unselect depending on which mode is active

