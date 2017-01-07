# Python 2.7.12
# Author: Kristen Findley
# Date: 03 January, 2017
# Description: Drill 38 of 68 SQL and Python

import sqlite3 #import sql module
connection = sqlite3.connect(":memory:") #use temporary RAM as DB
c = connection.cursor() #create a means of communicating across the connection

c.execute("DROP TABLE IF EXISTS Roster")
c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
rosterValues = (
    ("Jean-Baptiste Zorg","Human",122),
    ("Korben Dallas","Meat Popsicle",100),
    ("Ak'not","Mangalore",-5)
    )
c.executemany("INSERT INTO Roster VALUES(?,?,?)", rosterValues) #parameterized statement using tuples
c.execute("UPDATE Roster SET Species=? WHERE Name=?",("Human","Korben Dallas")) #update species of Korben Dallas
c.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
for row in c.fetchall():
    print row


