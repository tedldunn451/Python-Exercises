# Python 2.7.12
# Author: Kristen Findley
# Date: 18 December 2016
# Description: instructions for interfacing with sqlite database in Python

import sqlite3 # import sql module
connection = sqlite3.connect("test_database.db") # test_database.db can be replaced with an existing database OR a new database

c = connection.cursor() # create a means of communicating across the connection

# once the c cursor has been established, the database can be manipulated as shown in this example
c.execute("CREATE TABLE Coaches(FirstName TEXT, LastName TEXT, Team TEXT, Location TEXT)")
c.execute("INSERT INTO Coaches VALUES('Ian','Wilson','Dhahran Wellness','Dhahran, Saudi Arabia')")
connection.commit()
connection.close()

# to create/use a temporary database use the following:
connection = sqlite3.connect(':memory:')

with sqlite3.connect("test_database.db") as connection: # another way of accessing database using 'with' keyword
# perform SQL operations using connection here
# commit not required when using this syntax

# to execute multiple commands at once refer to the following example:
c.executescript("""
DROP TABLE IF EXISTS People;
CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
INSERT INTO People VALUES('Kristen','Findley',26);
""")

# to execute many similar statements refer to the following example
peopleValues = (
    ('Kristen','Findley',26),
    ('Elizabeth','Findley',27),
    ('Teresa','Findley',24)
    )
c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues) # parameterized statement using tuples

# example script using parameterized statements
import sqlite3
firstName = raw_input("Enter your first name: ")
lastName = raw_input("Enter your last name: ")
age = int(raw_input("Enter your age: "))
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES("'+ firstName +'","'+ lastName +'","+ str(age) +")"
c.execute(line)
c.execute("UPDATE People SET Age=? WHERE firstName=? AND lastName=?, (60, 'Jim', 'Findley')
          
# example of information retrieval
import sqlite3
peopleValues = (('Kristen','Findley',26),
                ('Elizabeth','Findley',27),
                ('Teresa','Findley',24),
                ('Cora','Findley',57),
                ('Jim','Findley',60))
with sqlite3.connect('test_database.db') as connection:
          c = connection.cursor()
          c.execute("DROP TABLE IF EXISTS People")
          c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
          c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)
          c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
          for row in c.fetchall():
              print row # the u that displays in the results stands for unicode
