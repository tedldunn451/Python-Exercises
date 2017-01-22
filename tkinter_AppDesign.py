# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 20, 2017
# Description: Example of App Design 

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

'''

Feedback form for people who have gone on 'From Desert to Sea' trip:

Define form requirements...
    Display
         logo and instructions
         input fields for Name, e-mail address, multi-line comments
         Submit and Clear buttons
    Print input to console, clear input, notify user of success upon clicking Submit
    Empty input fields upon clicking Clear

Draft general picture of what GUI will look like (see TkinterAppExampleGUIDraft in Python folder)
2 subregions: 1 for the logo and header and 1 for the input and submit fields/buttons

widgets involved and parent/child relationships
TopLevel: master
    Frame: header
         Label: logo (image)
         Label: header
         Label: message
    Frame: contents
         Label: name
         Label: email
         Label: comments
         Entry: name
         Entry: email
         Text: comments
         Button: submit
         Button: clear

'''

class Feedback:

    def __init__(self, master): # master is the top-level tk widget

        master.title('Explore CA Feedback')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')

        self.style = ttk.Style() # use to configure default styles so that they apply to all themed widgets
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master) # first frame with header, logo, and instructions
        self.frame_header.pack()
        
        self.logo = PhotoImage(file = 'tour_logo.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Thanks for Exploring!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master) # second frame for input fields and buttons
        self.frame_content.pack()
        
        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 57, height = 10, font = ('Arial', 10))

        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')
                            
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end') # line 1 character 0

def main():            
    
    root = Tk()
    feedback = Feedback(root) # passed to feedback constructor to be used as master widget
    root.mainloop()
    
if __name__ == "__main__": main() # will only call main function if python file is run as main script
