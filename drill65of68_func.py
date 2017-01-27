# Author: Kristen Findley
# Date: 26 January 2017
# Python: Version 3.5.7
# Description: script that allows a user to browse for and select a folder that the program will scan for files edited in the previous 24 hrs and copy them into a second folder

from tkinter import *
from tkinter import filedialog
import os
import shutil
import time
import sqlite3
import datetime

import drill65of68_main
import drill65of68_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit program","Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def create_db(self):
    conn = sqlite3.connect('db_copy_timestamp.db')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS tbl_copy_timestamp(ID INTEGER PRIMARY KEY AUTOINCREMENT,date TEXT,time TEXT,files_copied INT);")
        conn.commit()
    conn.close()

def disp_last_timestamp(self):
    conn = sqlite3.connect('db_copy_timestamp.db')
    with conn:
        c = conn.cursor()
        c,count = count_records(c)
        if count >= 1:
            c.execute("SELECT * FROM tbl_copy_timestamp ORDER BY ID DESC LIMIT 1")
            last_timestamp = c.fetchall()
            last_timestamp_list = last_timestamp[0]
            last_date = last_timestamp_list[1]
            last_time_unix = last_timestamp_list[2]
            last_time = datetime.datetime.fromtimestamp(int(round(float(last_time_unix)))).strftime("%H:%M:%S")
            last_copies = str(last_timestamp_list[3])
            last_timestamp = "This application was last run on "+last_date+" at "+last_time+" and "+last_copies+" files were copied."
            messagebox.showinfo("Last timestamp",last_timestamp)
        else:
            messagebox.showinfo("Last timestamp","There are no records of this program being previously run.")
    conn.close()

def count_records(c):
    count = "" 
    c.execute("SELECT COUNT(*) FROM tbl_copy_timestamp") 
    count = c.fetchone()[0]
    return c,count

def select_origin(self):
    global origin_dir
    origin_dir = ""
    origin_dir = filedialog.askdirectory()+"/"
    self.entry_origin.insert(0,origin_dir)

def select_destination(self):
    global destination_dir
    destination_dir = ""
    destination_dir= filedialog.askdirectory()+"/"
    self.entry_destination.insert(0,destination_dir)

def copy_files(self):
    global current_time
    current_time = time.time()
    global current_date
    current_date = time.strftime("%d/%m/%Y")
    folderA = origin_dir
    folderB = destination_dir
    original_dest_files = len(os.listdir(folderB))
    for i in os.listdir(folderA):
        time_file = os.path.getmtime(folderA+i)
        if current_time - 86400 <= time_file:
            shutil.copy(folderA+i,folderB)
    final_dest_files = len(os.listdir(folderB))
    global files_copied
    files_copied = final_dest_files - original_dest_files
    if files_copied > 0:
        messagebox.showinfo("Files copied","All recently modified files were successfully copied.")
    elif files_copied == 0:
        messagebox.showinfo("Files not copied","There were no recently modified files.")
    add_timestamp(self)

def add_timestamp(self):
    conn = sqlite3.connect('db_copy_timestamp.db')
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO tbl_copy_timestamp (date,time,files_copied) VALUES (?,?,?)",(current_date,current_time,files_copied))
        conn.commit()
    conn.close()
