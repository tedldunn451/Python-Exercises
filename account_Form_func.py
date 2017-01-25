# Author: Kristen Findley
# Date: 22 January 2017
# Python: Version 3.5.2
# Description: Account Information Form - the purpose of this form is to provide a way to organize, edit, display, and retrieve information about the various accounts

import os
from tkinter import *
import tkinter as tk
import sqlite3

import account_Form_gui
import account_Form_main

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def create_db(self):
    conn = sqlite3.connect('db_account.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_account_info( \
             ID INTEGER PRIMARY KEY AUTOINCREMENT, \
             store_name TEXT, \
             website TEXT, \
             email TEXT, \
             phone TEXT, \
             address TEXT, \
             city TEXT, \
             distance TEXT, \
             owner TEXT, \
             manager TEXT, \
             m_email TEXT, \
             buyer TEXT, \
             b_email TEXT, \
             other_emps TEXT, \
             fb TEXT, \
             twitter TEXT, \
             ig TEXT, \
             quadrant TEXT, \
             status TEXT, \
             priority TEXT, \
             last_contact TEXT , \
             ecommerce TEXT, \
             social_cap TEXT, \
             comp_brands TEXT, \
             comm_partnerships TEXT, \
             product_mix TEXT, \
             other TEXT \
             );")
        conn.commit()
    conn.close()
    first_run(self) # call this function (defined below) to fill dummy data so that the table isn't completely empty and runs smoothly

def first_run(self):
    conn = sqlite3.connect('db_account.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_account_info (store_name, \
            website, \
            email, \
            phone, \
            address, \
            city, \
            distance, \
            owner, \
            manager, \
            m_email, \
            buyer, \
            b_email, \
            other_emps, \
            fb, \
            twitter, \
            ig, \
            quadrant, \
            status, \
            priority, \
            last_contact, \
            ecommerce, \
            social_cap, \
            comp_brands, \
            comm_partnerships, \
            product_mix, \
            other) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        ('store name',
                        'www.storename.com',
                        'storename@storename.com',
                        'xxx-xxx-xxxx',
                        'address',
                        'city',
                        'distance',
                        'owner',
                        'manager',
                        'manager email',
                        'buyer',
                        'buyer email',
                        'other emps',
                        'https://www.facebook.com/storename',
                        'https://www.twittercom/storename',
                        'https://www.instagram.com/storename',
                        '1/2/3/4/5',
                        'active/inactive/pending',
                        'low/medium/high',
                        'mm/dd/yyyy',
                        'ecommerce',
                        'social capitol',
                        'competitive brands',
                        'community partnerships',
                        'product mix',
                        'other'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = "" # create empty variable
    cur.execute("""SELECT COUNT(*) FROM tbl_account_info""") 
    count = cur.fetchone()[0] # extracts count data using first index of tuple
    return cur,count

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_account.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT website,email,phone,address,city,distance,owner,manager,m_email,buyer,b_email,other_emps,fb,twitter,ig,quadrant,status,priority,last_contact,ecommerce,social_cap,comp_brands,comm_partnerships,product_mix,other FROM tbl_account_info WHERE store_name = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_storename.delete(0,END)
            self.txt_storename.insert(0,value)
            self.txt_website.delete(0,END)
            self.txt_website.insert(0,data[0])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_address.delete(0,END)
            self.txt_address.insert(0,data[3])
            self.txt_city.delete(0,END)
            self.txt_city.insert(0,data[4])
            self.txt_distance.delete(0,END)
            self.txt_distance.insert(0,data[5])
            self.txt_owner.delete(0,END)
            self.txt_owner.insert(0,data[6])
            self.txt_manager.delete(0,END)
            self.txt_manager.insert(0,data[7])
            self.txt_memail.delete(0,END)
            self.txt_memail.insert(0,data[8])
            self.txt_buyer.delete(0,END)
            self.txt_buyer.insert(0,data[9])
            self.txt_bemail.delete(0,END)
            self.txt_bemail.insert(0,data[10])
            self.txt_otheremps.delete(0,END)
            self.txt_otheremps.insert(0,data[11])
            self.txt_fb.delete(0,END)
            self.txt_fb.insert(0,data[12])
            self.txt_twitter.delete(0,END)
            self.txt_twitter.insert(0,data[13])
            self.txt_ig.delete(0,END)
            self.txt_ig.insert(0,data[14])
            self.txt_quadrant.delete(0,END)
            self.txt_quadrant.insert(0,data[15])
            self.txt_status.delete(0,END)
            self.txt_status.insert(0,data[16])
            self.txt_priority.delete(0,END)
            self.txt_priority.insert(0,data[17])
            self.txt_lastcontact.delete(0,END)
            self.txt_lastcontact.insert(0,data[18])
            self.txt_ecommerce.delete(0,END)
            self.txt_ecommerce.insert(0,data[19])
            self.txt_socialcapitol.delete(0,END)
            self.txt_socialcapitol.insert(0,data[20])
            self.txt_compbrands.delete(0,END)
            self.txt_compbrands.insert(0,data[21])
            self.txt_commpartnerships.delete(0,END)
            self.txt_commpartnerships.insert(0,data[22])
            self.txt_productmix.delete(0,END)
            self.txt_productmix.insert(0,data[23])
            self.txt_other.delete(0,END)
            self.txt_other.insert(0,data[24])

def addToList(self):
    var_storename = self.txt_storename.get().strip().title()
    var_website = self.txt_website.get().strip()
    var_email = self.txt_email.get().strip()
    var_phone = self.txt_phone.get().strip()
    var_address = self.txt_address.get().strip()
    var_city = self.txt_city.get().strip()
    var_distance = self.txt_distance.get().strip()
    var_owner = self.txt_owner.get().strip().title()
    var_manager = self.txt_manager.get().strip().title()
    var_memail = self.txt_memail.get().strip()
    var_buyer = self.txt_buyer.get().strip().title()
    var_bemail = self.txt_bemail.get().strip()
    var_otheremps = self.txt_otheremps.get().strip()
    var_fb = self.txt_fb.get().strip()
    var_twitter = self.txt_twitter.get().strip()
    var_ig = self.txt_ig.get().strip()
    var_quadrant = self.txt_quadrant.get().strip()
    var_status = self.txt_status.get().strip()
    var_priority = self.txt_priority.get().strip()
    var_lastcontact = self.txt_lastcontact.get().strip()
    var_ecommerce = self.txt_ecommerce.get().strip()
    var_socialcapitol = self.txt_socialcapitol.get().strip()
    var_compbrands = self.txt_compbrands.get().strip()
    var_commpartnerships = self.txt_commpartnerships.get().strip()
    var_productmix = self.txt_productmix.get().strip()
    var_other = self.txt_other.get().strip()
    if (len(var_storename) > 0) and (len(var_phone) > 0) and (len(var_address) > 0): # enforce user input of required info
        conn = sqlite3.connect('db_account.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(store_name) FROM tbl_account_info WHERE store_name = '{}'""".format(var_storename)) # verify that account storename has not already been entered
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if storename has not been entered, insert new values into DB
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_account_info (store_name,
                     website,
                     email,
                     phone,
                     address,
                     city,
                     distance,
                     owner,
                     manager,
                     m_email,
                     buyer,
                     b_email,
                     other_emps,
                     fb,
                     twitter,
                     ig,
                     quadrant,
                     status,
                     priority,
                     last_contact,
                     ecommerce,
                     social_cap,
                     comp_brands,
                     comm_partnerships,
                     product_mix,
                     other) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(var_storename,
                          var_website,
                          var_email,
                          var_phone,
                          var_address,
                          var_city,
                          var_distance,
                          var_owner,
                          var_manager,
                          var_memail,
                          var_buyer,
                          var_bemail,
                          var_otheremps,
                          var_fb,
                          var_twitter,
                          var_ig,
                          var_quadrant,
                          var_status,
                          var_priority,
                          var_lastcontact,
                          var_ecommerce,
                          var_socialcapitol,
                          var_compbrands,
                          var_commpartnerships,
                          var_productmix,
                          var_other))
                self.lstList1.insert(END, var_storename) # update listbox with storename
                onClear(self) # call function to clear all textboxes
            else:
                messagebox.showerror("Storename Error","'{}' already exists in the database. Please enter a new storename.".format(var_storename))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing data", "Please fill in 'Store Name', 'Phone Number', and 'Address' fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('db_account.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_account_info""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete confirmation", "All information associated with ({}) \nwill be permanently deleted from the database. \n\nProceed with delete request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_account.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_account_info WHERE store_name = '{}'""".format(var_select))
                onDeleted(self) # call function to clear all textboxes and selected index of listbox
                # onRefresh(self)
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time.".format(var_select))
    conn.close()

def onDeleted(self):
    self.txt_storename.delete(0,END)
    self.txt_website.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_address.delete(0,END)
    self.txt_city.delete(0,END)
    self.txt_distance.delete(0,END)
    self.txt_owner.delete(0,END)
    self.txt_manager.delete(0,END)
    self.txt_memail.delete(0,END)
    self.txt_buyer.delete(0,END)
    self.txt_bemail.delete(0,END)
    self.txt_otheremps.delete(0,END)
    self.txt_fb.delete(0,END)
    self.txt_twitter.delete(0,END)
    self.txt_ig.delete(0,END)
    self.txt_quadrant.delete(0,END)
    self.txt_status.delete(0,END)
    self.txt_priority.delete(0,END)
    self.txt_lastcontact.delete(0,END)
    self.txt_ecommerce.delete(0,END)
    self.txt_socialcapitol.delete(0,END)
    self.txt_compbrands.delete(0,END)
    self.txt_commpartnerships.delete(0,END)
    self.txt_productmix.delete(0,END)
    self.txt_other.delete(0,END)
    # onRefresh(self)
    try: # remove storename from listbox
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_storename.delete(0,END)
    self.txt_website.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_address.delete(0,END)
    self.txt_city.delete(0,END)
    self.txt_distance.delete(0,END)
    self.txt_owner.delete(0,END)
    self.txt_manager.delete(0,END)
    self.txt_memail.delete(0,END)
    self.txt_buyer.delete(0,END)
    self.txt_bemail.delete(0,END)
    self.txt_otheremps.delete(0,END)
    self.txt_fb.delete(0,END)
    self.txt_twitter.delete(0,END)
    self.txt_ig.delete(0,END)
    self.txt_quadrant.delete(0,END)
    self.txt_status.delete(0,END)
    self.txt_priority.delete(0,END)
    self.txt_lastcontact.delete(0,END)
    self.txt_ecommerce.delete(0,END)
    self.txt_socialcapitol.delete(0,END)
    self.txt_compbrands.delete(0,END)
    self.txt_commpartnerships.delete(0,END)
    self.txt_productmix.delete(0,END)
    self.txt_other.delete(0,END)

def onRefresh(self):
    self.lstList1.delete(0,END) # populate listbox coinciding with database
    conn = sqlite3.connect('db_account.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_account_info""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT store_name FROM tbl_account_info""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of list selection
        var_value = self.lstList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection", "No store name was selected from the list box. \nCancelling 'Update' request.")
        return
    # user may only update entry fields other than the storename. To update storename, entry must be deleted and reentered.
    var_website = self.txt_website.get().strip()
    var_email = self.txt_email.get().strip()
    var_phone = self.txt_phone.get().strip()
    var_address = self.txt_address.get().strip()
    var_city = self.txt_city.get().strip()
    var_distance = self.txt_distance.get().strip()
    var_owner = self.txt_owner.get().strip().title()
    var_manager = self.txt_manager.get().strip().title()
    var_memail = self.txt_memail.get().strip()
    var_buyer = self.txt_buyer.get().strip().title()
    var_bemail = self.txt_bemail.get().strip()
    var_otheremps = self.txt_otheremps.get().strip()
    var_fb = self.txt_fb.get().strip()
    var_twitter = self.txt_twitter.get().strip()
    var_ig = self.txt_ig.get().strip()
    var_quadrant = self.txt_quadrant.get().strip()
    var_status = self.txt_status.get().strip()
    var_priority = self.txt_priority.get().strip()
    var_lastcontact = self.txt_lastcontact.get().strip()
    var_ecommerce = self.txt_ecommerce.get().strip()
    var_socialcapitol = self.txt_socialcapitol.get().strip()
    var_compbrands = self.txt_compbrands.get().strip()
    var_commpartnerships = self.txt_commpartnerships.get().strip()
    var_productmix = self.txt_productmix.get().strip()
    var_other = self.txt_other.get().strip
    if (len(var_website) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(website) FROM tbl_account_info WHERE website = '{}'""".format(var_website))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_website,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET website = '{0}' WHERE store_name = '{1}'""".format(var_website, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_website))
            onClear(self)
        conn.close()
    elif (len(var_email) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(email) FROM tbl_account_info WHERE email = '{}'""".format(var_email))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_email,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET email = '{0}' WHERE store_name = '{1}'""".format(var_email, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_email))
            onClear(self)
        conn.close()
    elif (len(var_phone) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(phone) FROM tbl_account_info WHERE phone = '{}'""".format(var_phone))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET phone = '{0}' WHERE store_name = '{1}'""".format(var_phone, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_phone))
            onClear(self)
        conn.close()
    elif (len(var_address) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(address) FROM tbl_account_info WHERE address = '{}'""".format(var_address))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_address,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET address = '{0}' WHERE store_name = '{1}'""".format(var_address, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_address))
            onClear(self)
        conn.close()
    elif (len(var_city) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(city) FROM tbl_account_info WHERE city = '{}'""".format(var_city))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_city,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET city = '{0}' WHERE store_name = '{1}'""".format(var_city, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_city))
            onClear(self)
        conn.close()
    elif (len(var_distance) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(distance) FROM tbl_account_info WHERE distance = '{}'""".format(var_distance))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_distance,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET distance = '{0}' WHERE store_name = '{1}'""".format(var_distance, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_distance))
            onClear(self)
        conn.close()
    elif (len(var_owner) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(owner) FROM tbl_account_info WHERE owner = '{}'""".format(var_owner))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_owner,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET owner = '{0}' WHERE store_name = '{1}'""".format(var_owner, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_owner))
            onClear(self)
        conn.close()
    elif (len(var_manager) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(manager) FROM tbl_account_info WHERE manager = '{}'""".format(var_manager))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_manager,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET manager = '{0}' WHERE store_name = '{1}'""".format(var_manager, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_manager))
            onClear(self)
        conn.close()
    elif (len(var_memail) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(m_email) FROM tbl_account_info WHERE m_email = '{}'""".format(var_memail))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_memail,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET m_email = '{0}' WHERE store_name = '{1}'""".format(var_memail, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_memail))
            onClear(self)
        conn.close()
    elif (len(var_buyer) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(buyer) FROM tbl_account_info WHERE buyer = '{}'""".format(var_buyer))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_buyer,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET buyer = '{0}' WHERE store_name = '{1}'""".format(var_buyer, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_buyer))
            onClear(self)
        conn.close()
    elif (len(var_bemail) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(b_email) FROM tbl_account_info WHERE b_email = '{}'""".format(var_bemail))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_bemail,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET b_email = '{0}' WHERE store_name = '{1}'""".format(var_bemail, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_bemail))
            onClear(self)
        conn.close()
    elif (len(var_otheremps) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(other_emps) FROM tbl_account_info WHERE other_emps = '{}'""".format(var_otheremps))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_otheremps,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET other_emps = '{0}' WHERE store_name = '{1}'""".format(var_otheremps, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_otheremps))
            onClear(self)
        conn.close()
    elif (len(var_fb) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(fb) FROM tbl_account_info WHERE fb = '{}'""".format(var_fb))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_fb,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET fb = '{0}' WHERE store_name = '{1}'""".format(var_fb, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_fb))
            onClear(self)
        conn.close()
    elif (len(var_twitter) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(twitter) FROM tbl_account_info WHERE twitter = '{}'""".format(var_twitter))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_twitter,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET twitter = '{0}' WHERE store_name = '{1}'""".format(var_twitter, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_twitter))
            onClear(self)
        conn.close()
    elif (len(var_ig) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(ig) FROM tbl_account_info WHERE ig = '{}'""".format(var_ig))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_ig,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET ig = '{0}' WHERE store_name = '{1}'""".format(var_ig, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_ig))
            onClear(self)
        conn.close()
    elif (len(var_quadrant) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(quadrant) FROM tbl_account_info WHERE quadrant = '{}'""".format(var_quadrant))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_quadrant,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET quadrant = '{0}' WHERE store_name = '{1}'""".format(var_quadrant, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_quadrant))
            onClear(self)
        conn.close()
    elif (len(var_status) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(status) FROM tbl_account_info WHERE status = '{}'""".format(var_status))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_status,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET status = '{0}' WHERE store_name = '{1}'""".format(var_status, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_status))
            onClear(self)
        conn.close()
    elif (len(var_priority) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(priority) FROM tbl_account_info WHERE priority = '{}'""".format(var_priority))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_priority,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET priority = '{0}' WHERE store_name = '{1}'""".format(var_priority, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_priority))
            onClear(self)
        conn.close()
    elif (len(var_lastcontact) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(last_contact) FROM tbl_account_info WHERE last_contact = '{}'""".format(var_lastcontact))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_lastcontact,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET last_contact = '{0}' WHERE store_name = '{1}'""".format(var_lastcontact, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_lastcontact))
            onClear(self)
        conn.close()
    elif (len(var_ecommerce) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(ecommerce) FROM tbl_account_info WHERE ecommerce = '{}'""".format(var_ecommerce))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_ecommerce,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET ecommerce = '{0}' WHERE store_name = '{1}'""".format(var_ecommerce, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_ecommerce))
            onClear(self)
        conn.close()
    elif (len(var_socialcapitol) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(social_cap) FROM tbl_account_info WHERE social_cap = '{}'""".format(var_socialcapitol))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_socialcapitol,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET social_cap = '{0}' WHERE store_name = '{1}'""".format(var_socialcapitol, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_socialcapitol))
            onClear(self)
        conn.close()
    elif (len(var_compbrands) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(comp_brands) FROM tbl_account_info WHERE comp_brands = '{}'""".format(var_compbrands))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_compbrands,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET comp_brands = '{0}' WHERE store_name = '{1}'""".format(var_compbrands, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_compbrands))
            onClear(self)
        conn.close()
    elif (len(var_commpartnerships) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(comm_partnerships) FROM tbl_account_info WHERE comm_partnerships = '{}'""".format(var_commpartnerships))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_commpartnerships,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET comm_partnerships = '{0}' WHERE store_name = '{1}'""".format(var_commpartnerships, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_commpartnerships))
            onClear(self)
        conn.close()
    elif (len(var_productmix) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(product_mix) FROM tbl_account_info WHERE product_mix = '{}'""".format(var_productmix))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_productmix,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET product_mix = '{0}' WHERE store_name = '{1}'""".format(var_productmix, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_productmix))
            onClear(self)
        conn.close()
    elif (len(var_other) > 0):
        conn = sqlite3.connect('account.db')
        with conn:
            c = conn.cursor()
            cur.execute("""SELECT COUNT(other) FROM tbl_account_info WHERE other = '{}'""".format(var_other))
            count = c.fetchone()[0]
            print (count)
            if count == 0:
                response = messagebox.askokcancel("Update Request", "The following changes ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_other,var_value))
                print (response)
                if response:
                    with conn:
                        c = conn.cursor()
                        c.execute("""UPDATE tbl_account_info SET other = '{0}' WHERE store_name = '{1}'""".format(var_other, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "({}) already exists in the database for this name. \n\nYour update request has been cancelled.".format(var_other))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information", "Please select a storename from the list. \nThen edit the desired information.")
    onClear(self)

if __name__ == "__main__":
    pass
