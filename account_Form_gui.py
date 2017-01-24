# Author: Kristen Findley
# Date: 22 January 2017
# Python: Version 3.5.2
# Description: Account Information Form - the purpose of this form is to provide a way to organize, edit, display, and retrieve information about the various accounts

from tkinter import *
from tkinter import ttk
import tkinter as tk # creates shortcut to reference tkinter as tk in subseqent code

# import other modules to enable interaction
import account_Form_func
import account_Form_main

def load_gui(self): # must pass in self to access all ParentWindow widgets
    # GENERAL information
    self.lbl_general = tk.Label(self.master, text = 'GENERAL')
    self.lbl_general.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = (15,0), sticky = 'nw')
    self.lbl_storename = tk.Label(self.master, text = 'Store Name: ')
    self.lbl_storename.grid(row = 1, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_storename = tk.Entry(self.master, text = '', width = 50)
    self.txt_storename.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_website = tk.Label(self.master, text = 'Website: ')
    self.lbl_website.grid(row = 3, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_website = tk.Entry(self.master, text = '', width = 50)
    self.txt_website.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_email = tk.Label(self.master, text = 'Email: ')
    self.lbl_email.grid(row = 5, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_email = tk.Entry(self.master, text = '', width = 50)
    self.txt_email.grid(row = 6, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_phone = tk.Label(self.master, text = 'Phone: ')
    self.lbl_phone.grid(row = 7, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_phone = tk.Entry(self.master, text = '', width = 50)
    self.txt_phone.grid(row = 8, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_address = tk.Label(self.master, text = 'Address: ')
    self.lbl_address.grid(row = 9, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_address = tk.Entry(self.master, text = '', width = 50)
    self.txt_address.grid(row = 10, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_city = tk.Label(self.master, text = 'City: ')
    self.lbl_city.grid(row = 11, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_city = tk.Entry(self.master, text = '', width = 50)
    self.txt_city.grid(row = 12, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_distance = tk.Label(self.master, text = 'Distance From Home: ')
    self.lbl_distance.grid(row = 13, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_distance = tk.Entry(self.master, text = '', width = 50)
    self.txt_distance.grid(row = 14, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')

    # PERSONNEL information
    self.lbl_personnel = tk.Label(self.master, text = 'PERSONNEL')
    self.lbl_personnel.grid(row = 16, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.lbl_owner = tk.Label(self.master, text = 'Owner: ')
    self.lbl_owner.grid(row = 17, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_owner = tk.Entry(self.master, text = '', width = 50)
    self.txt_owner.grid(row = 18, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_manager = tk.Label(self.master, text = 'Manager: ')
    self.lbl_manager.grid(row = 19, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_manager = tk.Entry(self.master, text = '', width = 50)
    self.txt_manager.grid(row = 20, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_memail = tk.Label(self.master, text = 'Manager Email: ')
    self.lbl_memail.grid(row = 21, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_memail = tk.Entry(self.master, text = '', width = 50)
    self.txt_memail.grid(row = 22, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_buyer = tk.Label(self.master, text = 'Buyer: ')
    self.lbl_buyer.grid(row = 23, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_buyer = tk.Entry(self.master, text = '', width = 50)
    self.txt_buyer.grid(row = 24, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_bemail = tk.Label(self.master, text = 'Buyer Email: ')
    self.lbl_bemail.grid(row = 25, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_bemail = tk.Entry(self.master, text = '', width = 50)
    self.txt_bemail.grid(row = 26, column = 0, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_otheremps = tk.Label(self.master, text = 'Other Employees: ')
    self.lbl_otheremps.grid(row = 27, column = 0, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_otheremps = tk.Entry(self.master, text = '', width = 50)
    self.txt_otheremps.grid(row = 28, column = 0, columnspan = 2, padx = 5, pady = (0,15), sticky = 'nw')

    # SOCIAL MEDIA information
    self.lbl_social = tk.Label(self.master, text = 'SOCIAL MEDIA')
    self.lbl_social.grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = (15,0), sticky = 'nw')
    self.lbl_fb = tk.Label(self.master, text = 'Facebook: ')
    self.lbl_fb.grid(row = 1, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_fb = tk.Entry(self.master, text = 'https://www.facebook.com/', width = 50)
    self.txt_fb.grid(row = 2, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_twitter = tk.Label(self.master, text = 'Twitter: ')
    self.lbl_twitter.grid(row = 3, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_twitter = tk.Entry(self.master, text = 'https://www.twitter.com/', width = 50)
    self.txt_twitter.grid(row = 4, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_ig = tk.Label(self.master, text = 'Instagram: ')
    self.lbl_ig.grid(row = 5, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_ig = tk.Entry(self.master, text = "https://www.instagram.com/", width = 50)
    self.txt_ig.grid(row = 6, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')

    # STANDING information
    self.lbl_standing = tk.Label(self.master, text = 'STANDING')
    self.lbl_standing.grid(row = 8, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.lbl_quadrant = tk.Label(self.master, text = 'Quadrant: ')
    self.lbl_quadrant.grid(row = 9, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_quadrant = tk.Entry(self.master, text = '', width = 50)
    self.txt_quadrant.grid(row = 10, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_status = tk.Label(self.master, text = 'Status: ')
    self.lbl_status.grid(row = 11, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_status = tk.Entry(self.master, text = '', width = 50)
    self.txt_status.grid(row = 12, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_priority = tk.Label(self.master, text = 'Priority: ')
    self.lbl_priority.grid(row = 13, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_priority = tk.Entry(self.master, text = '', width = 50)
    self.txt_priority.grid(row = 14, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_lastcontact = tk.Label(self.master, text = 'Last Contact: ')
    self.lbl_lastcontact.grid(row = 15, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_lastcontact = tk.Entry(self.master, text = "mm/dd/yy", width = 50)
    self.txt_lastcontact.grid(row = 16, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')

    # FINGERPRINT information
    self.lbl_fingerprint = tk.Label(self.master, text = 'FINGERPRINT')
    self.lbl_fingerprint.grid(row = 18, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.lbl_ecommerce = tk.Label(self.master, text = 'ECommerce: ')
    self.lbl_ecommerce.grid(row = 19, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_ecommerce = tk.Entry(self.master, text = '', width = 50)
    self.txt_ecommerce.grid(row = 20, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_socialcapitol = tk.Label(self.master, text = 'Social Capitol: ')
    self.lbl_socialcapitol.grid(row = 21, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_socialcapitol = tk.Entry(self.master, text = '', width = 50)
    self.txt_socialcapitol.grid(row = 22, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_compbrands = tk.Label(self.master, text = 'Competitor Brands Carried: ')
    self.lbl_compbrands.grid(row = 23, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_compbrands = tk.Entry(self.master, text = '', width = 50)
    self.txt_compbrands.grid(row = 24, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_commpartnerships = tk.Label(self.master, text = 'Community Partnerships: ')
    self.lbl_commpartnerships.grid(row = 25, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_commpartnerships = tk.Entry(self.master, text = '', width = 50)
    self.txt_commpartnerships.grid(row = 26, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')
    self.lbl_productmix = tk.Label(self.master, text = 'Product Mix: ')
    self.lbl_productmix.grid(row = 27, column = 2, columnspan = 2, padx = 5, sticky = 'nw')
    self.txt_productmix = tk.Entry(self.master, text = '', width = 50)
    self.txt_productmix.grid(row = 28, column = 2, columnspan = 2, padx = 5, pady = (0,5), sticky = 'nw')

    # OTHER information
    self.lbl_other = tk.Label(self.master, text = 'Additional Information: ')
    self.lbl_other.grid(row = 30, column = 0, columnspan = 4, padx = 5, sticky = 'nw')
    self.txt_other = tk.Entry(self.master, text = '', width = 102)
    self.txt_other.grid(row = 31, column = 0, columnspan = 4, padx = 5, pady = (0,15))

    # scrollbar
    self.scrollbar1 = Scrollbar(self.master,orient = VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand = self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: account_Form_func.onSelect(self,event))
    self.scrollbar1.config(command = self.lstList1.yview)
    self.scrollbar1.grid(row = 0, column = 7, rowspan = 34)
    self.lstList1.grid(row = 0, column = 4, rowspan = 34, columnspan = 3)

    # Buttons
    self.btn_add = tk.Button(self.master, width = 12, height = 2, text = 'Add', command = lambda: account_Form_func.addToList(self))
    self.btn_add.grid(row = 33, column = 0, padx = 5, pady = (0,15))
    self.btn_update = tk.Button(self.master, width = 12, height = 2, text = 'Update', command = lambda: account_Form_func.onUpdate(self))
    self.btn_update.grid(row = 33, column = 1, padx = 5, pady = (0,15))
    self.btn_delete = tk.Button(self.master, width = 12, height = 2, text = 'Delete', command = lambda: account_Form_func.onDelete(self))
    self.btn_delete.grid(row = 33, column = 2, padx = 5, pady = (0,15))
    self.btn_close = tk.Button(self.master, width = 12, height = 2, text = 'Close', command = lambda: account_Form_func.ask_quit(self))
    self.btn_close.grid(row = 33, column = 3, padx = 5, pady = (0,15))

    account_Form_func.create_db(self)
    account_Form_func.onRefresh(self)

if __name__ == "__main__":
    pass
    

    
