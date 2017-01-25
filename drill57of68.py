# Author: Kristen Findley
# Date: 23 January, 2017
# Python: Version 3.5.2
# Description: Notes for SQLite3 with Python tutorial series (https://www.youtube.com/watch?v=o-vsdfCBpsU&feature=youtu.be&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo)

import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db') # if sqlite attempts to create to a db that doesn't exist, it creates it
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tbl_plot(unix INT, datestamp TEXT, keyword TEXT, value INT)') # the REAL datatype in SQL is the equivalent of float in Python

def data_entry():
    c.execute("INSERT INTO tbl_plot VALUES (14514145, '2017-01-23', 'Python', 5)") # you can change these values and re-run to enter new entry
    conn.commit() # saves info
    c.close()
    conn.close() # closes connection

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO tbl_plot (unix,datestamp,keyword,value) VALUES (?,?,?,?)",
              (unix,date,keyword,value))
    conn.commit() # don't need to close because it would have to close and reopen for every entry

def read_from_db():
    c.execute("SELECT * FROM tbl_plot WHERE unix > 1452618731") # this is essentially the same as highlighting or selecting text, but not doing anything with it
    data = c.fetchall() # use to copy selection or you could fetch one if you only want one
    print (data)
    # or to better visualize data use:
    for row in c.fetchall():
        print(row) # returns tuples of data... can use print(row[0]) to print only column in first index 

def graph_data():
    c.execute('SELECT unix, value FROM tbl_plot')
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[0])

    plt.plot_date(dates,values, '-')
    plt.show()

def del_and_update():
    c.execute('SELECT * FROM tbl_plot')
    [print(row) for row in c.fetchall()] # view all data

##    c.execute('UPDATE tbl_plot SET value = 99 WHERE value = 8')
##    conn.commit()
##    
##    c.execute('SELECT * FROM tbl_plot')
##    [print(row) for row in c.fetchall()] # view all data with changes implemented

##    c.execute('DELETE FROM tbl_plot WHERE value = 99') # 
##    conn.commit()
##    print(50 *'#') # use to create a line of # for visualization purposes

    c.execute('SELECT * FROM tbl_plot WHERE value = 2')
    [print(row) for row in c.fetchall()] # use to view all selected data so that you have a record prior to deleting since delete is irreversible
    c.execute('SELECT * FROM tbl_plot WHERE value = 2')
    print(len(c.fetchall())) # use to view number of rows prior to deleting so that you have a record since delete is irreversible
    c.execute('DELETE FROM tbl_plt WHERE value = 2 LIMIT 7')    
    
 
##create_table() # usually only run once
### data_entry()
##
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1) # so time stamp can go up one sec

##read_from_db()
del_and_update()
c.close()
conn.close()
